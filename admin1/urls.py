from django.conf.urls import url
from django.contrib import admin
from admin1 import views
from django.views.generic import TemplateView
app_name='admin1'
urlpatterns = [
               url(r'^add/',TemplateView.as_view(template_name='additem.html'),name='add'),
               url(r'check/',views.check,name='check'),
               url(r'^edit/',views.edit,name='edit'),
               url(r'^update/(\d+)/',views.update,name='update'),
               url(r'^change/',views.check,name='change'),
               url(r'^delete/',views.delete,name='delete'),
               url(r'^deleted/(\d+)/',views.deleted,name='deleted'),
               url(r'^view/',views.view,name='view'),
               url(r'^users/',views.users,name='users'),
               url(r'^admin/(\d+)',TemplateView.as_view(template_name='adminlogin.html'),name='admin'),
               url(r'^log/',views.adminlogin,name='log'),
               url(r'^orders/',views.orderview,name='orders'),
               url(r'^cancel/(\d+)/',views.cancel,name='cancel'),
               url(r'^del/(\d+)/',views.dele,name='del'),
               ]