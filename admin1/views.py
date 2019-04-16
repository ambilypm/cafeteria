from __future__ import unicode_literals
from register.models import Items,Order
from forms import items,Reg
from register.models import Register
from admin1.models import Admin
from django.shortcuts import render,redirect
from django.http import HttpResponse

def check(request):
    status='fail'
    if request.method == 'POST':
        temp=items(request.POST,request.FILES)
        if temp.is_valid():
            i=Items()
            i.logo=temp.cleaned_data['logo']
            i.name=temp.cleaned_data['name']
            i.price=temp.cleaned_data['price']
            i.quantity=request.POST.get('quantity')
            i.id=request.POST.get('val')
            i.save()
            status='succses'
    else:
        temp=items()
    if status =='fail':
        return  HttpResponse(status)
    elif status == 'succses':
        return render(request,'additem.html')

def edit(request):
    ob=Items.objects.all()
    return render(request,'edit.html',{'object_list':ob})
def update(request,id):
    ob=Items.objects.filter(id=id)
    return render(request,'update.html',{'object_list':ob})
def delete(request):
    ob=Items.objects.all()
    return render(request,'delete.html',{'object_list':ob})
def deleted(request,id):
    ob =Items.objects.filter(id=id)
    ob.delete()
    return render(request,'admin1.html')
def view(request):
    ob=Items.objects.all()
    return render(request,'view.html',{'object_list':ob})
def users(request):
    ob=Register.objects.all()
    return render(request,'userview.html',{'object_list':ob})
def adminlogin(request):

    status='not logged'
    if request.method == "POST":
        mylogin=Reg(request.POST)
        if mylogin.is_valid():
            user=mylogin.cleaned_data['username']
            passw=mylogin.cleaned_data['password']
            l=Admin.objects.filter(username=user)
            for i in l:
                u=i.username
                p=i.password
                print u,p
            if user==u and passw==p:
                print "loged"
                return render(request,'admin1.html')
    else:
        return render(request,'adminlogin.html',{'message':'username or password is error'})
def orderview(request):
    ob=Order.objects.all()
    return render(request,'adminorderv.html',{'object_list':ob})
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
    return render(request,'admin1.html')
def dele(request,id):
    ob=Register.objects.filter(id=id)
    ob.delete()
    return redirect('/admin1/users/')