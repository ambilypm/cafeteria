from django.conf.urls import url
from django.views.generic import TemplateView,ListView
from register  import views
from register.models import Items,Order
app_name='register'

urlpatterns=[url(r'^reg/',TemplateView.as_view(template_name='reg.html'),name='reg'),
             url(r'^regcheck/',views.registe,name='regcheck'),
             url(r'^login/',TemplateView.as_view(template_name='login.html'),name='login'),
             url(r'^logincheck/',views.login,name='logincheck'),
             url(r'^itemv/',views.items,name='itemv'),
             url(r'^itemview/',views.itemsview,name='itemview'),
             url(r'^order/(\d+)/',views.order,name='order'),
             url(r'^placeorder/(\d+)/',views.place,name='placeorder'),
             url(r'^orders/',views.orderview,name='orders'),
             url(r'^cancel/(\d+)/',views.cancel,name='cancel'),
             url(r'^about1/',TemplateView.as_view(template_name='about1.html'),name='about1'),
             url(r'^home/',TemplateView.as_view(template_name='loggedin.html'),name='home'),
             url(r'^about/',TemplateView.as_view(template_name='about.html'),name='about'),
             url(r'^contact/',TemplateView.as_view(template_name='contact.html'),name='contact'),
             ]
