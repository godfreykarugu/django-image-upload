from django.shortcuts import render,redirect
from . forms import ProductForm
from . models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def insert_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('display-products')
    else:
        form=ProductForm()


    return render(request,'insert_product.html',{'form':form})


def display_products(request):
    products = Product.objects.all()
    return render(request, 'display_products.html',{'products':products})

def product_details(request,id):
    product = Product.objects.get(id=id)
    return render(request,'product_details.html',{'product':product})

def update_product(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('display-products')
    else:
        return render(request,'update_product.html',{'form':form})


def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('display-products')

def add_student(request):
    return render(request, 'home.html',{})


def view_details(request,id):
    product = Product.objects.get(id=id)
    return render(request,'view_details.html',{'product':product})