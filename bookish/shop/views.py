from django.core import paginator
from django.shortcuts import render
from .models import *
from typing import ContextManager
from django.shortcuts import render,redirect,HttpResponse

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from datetime import datetime



# Create your views here.
def books(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_item
    product_objects=Product.objects.all()

    #filter code
    genre=request.GET.get('genre')
    if genre!='' and genre is not None:
        product_objects=product_objects.filter(category__icontains=genre)
    


    #search code
    book_name=request.GET.get('book_name')
    if book_name!='' and book_name is not None:
        product_objects=product_objects.filter(title__icontains=book_name)

    #paginator code
    paginator=Paginator(product_objects,12)
    page=request.GET.get('page')
    product_objects=paginator.get_page(page)

    context={'product_objects':product_objects,'cartItems':cartItems}
    return render(request,'books.html',context)

def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_item
    

    context = {'items':items, 'order':order,'cartItems':cartItems}
    return render(request, 'cart.html', context)





def checkout(request):
	
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	items = order.orderitem_set.all()
    
	
	context = {'items':items, 'order':order}
	return render(request, 'checkout.html', context)



        
def updateItem(request):
    data = json.loads(request.body.decode("utf-8"))
    productId=data['productId']
    action=data['action']
    print('Id:',productId)
    print('Action:',action)

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)

    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('Item added',safe=False)

def processOrder(request):
    transaction_id=datetime.now().timestamp()
    data=json.loads(request.body)
    customer=request.user.customer
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    total=float(data['form']['total'])
    order.transaction_id=transaction_id
    if total==order.get_cart_total:
        order.complete=True
    order.save()
    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
    )
    return JsonResponse("Order Placed",safe=False)

def detail(request,id):
    product_object=Product.objects.get(id=id)
    return render(request,'detail.html',{'product_object':product_object})



def index(request):
    
        return render(request,'index.html')

def about(request):
    return render(request, 'about.html')
def sell(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=request.POST.get('price')
        category=request.POST.get('category')
        description=request.POST.get('description')
        condition=request.POST.get('condition')
        sell=Sell(contact=contact,name=name,title=title,author=author,price=price,category=category,description=description,condition=condition)
        sell.save()
        messages.success(request,"Book is registered")
    return render(request,'sell.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        password=request.POST.get('password')
        signup=Signup(name=name,email=email,contact=contact,password=password,date=datetime.today())
        signup.save()
        messages.success(request,"Sign Up successful")
    return render(request,'signup.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None :
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect("/books")
        else:
            messages.info(request,"invalid credentials")
            return render(request,"login.html")
            
    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('/home')



