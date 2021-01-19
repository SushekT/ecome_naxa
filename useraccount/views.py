from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from product.models import Product

# Create your views here.

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    context = {
    }

    return render(request,'account/login.html',context)

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form,

    }

    return render(request, 'account/signup.html', context)

def homepage(request):

    product = Product.objects.all()
    context={
       'product': product,
    }
    return render(request, 'index.html', context)

def product_detail(request, id):

    product_details = Product.objects.get(id=id)

    context = {
        'product_detail': product_details,
    }

    return render(request,'shop-item.html', context)
