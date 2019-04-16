# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import Reg
import time
from register.models import Register,Items,Order
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.

def registe(request):
    status='fail'
    if request.method == "POST":
        reg=Reg(request.POST)
        if reg.is_valid():
            r = Register()
            r.username=reg.cleaned_data['username']
            r.password=reg.cleaned_data['password']
            r.name=request.POST.get('name')
            r.phonenumber=request.POST.get('phonenumber')
            r.save()
            status='success'
    else:
        reg=Reg()
    return render(request,'main.html')
def login(request):
    status='not logged'
    if request.method == "POST":
        mylogin=Reg(request.POST)
        if mylogin.is_valid():
            user=mylogin.cleaned_data['username']
            passw=mylogin.cleaned_data['password']
            l=Register.objects.filter(username=user)
            for i in l:
                u=i.username
                p=i.password
                # print u,p
            if user==u and p==passw:
                print "loged"
                return render(request,'loggedin.html')
    else:
        mylogin=Reg()
        return render(request,'login.html',{'message':'username or password is incorrect'})
def items(request):
    ob = Items.objects.all()
    print ob
    return render(request,'itemview.html',{'object_list': ob})
def itemsview(request):
    ob=Items.objects.all()
    return render(request,'itemsview.html',{'object_list':ob})
def order(request,id):
    ob=Items.objects.filter(id=id)
    return render(request,'order.html',{'object_list':ob})
def place(request,id):
    ob=Items.objects.filter(id=id)
    status='some issues in placing order'
    for i in ob:
        n=i.name
        q=i.quantity
        l=i.logo
        print n,q,l
        status='placed successfuly'
    if request.method == 'POST':
        print "enter"
        price=request.POST.get('total')
        quan=request.POST.get('quantity')
        status = 'Your order is placed'
        print price,quan
    a=int(q)-int(quan)
    ob2=Order()
    ob2.name=n
    ob2.logo=l
    ob2.price=price
    ob2.quantity=quan
    ob2.date=time.asctime(time.localtime(time.time()))
    ob2.save()
    for i in ob:
        i.quantity=a
        i.save()
        status = 'placed successfuly'
    return render(request,'message.html',{'status':status})
def orderview(request):
    ob1=Order.objects.all()
    return render(request,'orderview.html',{'object_list':ob1})
def cancel(request,id):
    ob=Order.objects.filter(id=id)
    for i in ob:
        n=i.name
        q=i.quantity
    ob.delete()
    print n,q
    ob1=Items.objects.filter(name=n)
    for i in ob1:
        i.quantity=i.quantity+q
        i.save()
    return render(request,'loggedin.html')