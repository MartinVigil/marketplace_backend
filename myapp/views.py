from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth import login, logout, authenticate
from .models import Category, Product
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

def get_user_by_id(id_):
    user = User.objects.get(id=id_)
    return user.username

def get_user_by_sessionid(request):
    session_id = request.COOKIES.get('sessionid', None)
    try:
        session = Session.objects.get(session_key=session_id)
    except Session.DoesNotExist:
        return {'error':'sesion expirada'}

    uid = session.get_decoded().get('_auth_user_id')
    if uid:
        user = User.objects.get(id=uid)
        return user
    
def mark_as_selled(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = get_user_by_sessionid(request)
    if user.id != product.user_id:
        product.selled = True
        product.buyer_id = user.id
        product.save()
        return redirect('index')  
    else:
        return HttpResponse('no puede comprar su propio producto')  

#ruta del login
def render_login(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])

        if not user: 
            return render(request, 'login.html', {'form': AuthenticationForm, 'response' : 'usuario o contraseña incorrectos'})  
        else:
            login(request,user)
            return redirect('index')  
         
    return render(request, 'login.html', {'form': AuthenticationForm})   
 
#ruta del registro
def render_register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('login')
            except:
                return render(request, 'register.html',{'form':UserCreationForm, 'response': 'el usuario ya existe'})
        else:
            return render(request, 'register.html',{'form':UserCreationForm, 'response': 'las contraseñas no coinciden'})          
    return render(request, 'register.html',{'form':UserCreationForm})

#ruta del myproducts
def render_myproducts(request):
    user = get_user_by_sessionid(request)
    products = Product.objects.all()
    products_names = [product for product in products if user.id == product.user_id]


    return render(request,'myproducts.html',{'products_names':products_names})

#ruta de addproducts
def render_addproducts(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        user = get_user_by_sessionid(request)
        if form.is_valid():
            product = form.save(commit=False)
            product.user_id = user.id
            product.save()
            return redirect('my_products')
    else:
        form = ProductForm(request.POST, request.FILES)
        return render(request,'addproducts.html',{'form': form})
    return render(request,'addproducts.html',{'form': form})

#ruta de updateproducts
@login_required
def render_updateproduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('my_products')  
    else:
        form = ProductForm(instance=product)

    return render(request,'updateproducts.html',{'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('my_products')

#ruta del buys
def render_buys(request):
    products = Product.objects.all()
    user = get_user_by_sessionid(request)
    products_names = [product for product in products if user.id == product.buyer_id]
    return render(request,'buys.html', {'products_names':products_names})

#logout 
def signout(request):
    logout(request)
    return redirect('login') 


#ruta del marketplace
def render_index(request):
    categories = Category.objects.all()
    category_names = [category.name for category in categories]
    products = Product.objects.all()
    products_names = [{'product': product,'username': get_user_by_id(product.user_id)} for product in products]
    return render(request,'index.html', {'category_names': category_names, 'products_names':products_names})






