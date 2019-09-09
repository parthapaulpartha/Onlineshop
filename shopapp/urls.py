"""online_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^registration/', views.registration, name='registration'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^change_password/', views.change_password, name='change_password'),
    url(r'^man/', views.man_image, name='man_images'),
    url(r'^woman/', views.woman_image, name='woman_images'),
    url(r'^kids_boy/', views.kidsboy_image, name='kids_boy'),
    url(r'^kids_girl/', views.kidsgirl_image, name='kids_girl'),
    url(r'^e_phone/', views.electronic_phone, name='e_phone'),
    url(r'^e_desktop/', views.electronic_desktop, name='e_desktop'),
    url(r'^e_laptop/', views.electronic_laptop, name='e_laptop'),
    url(r'^e_head_phone/', views.electronic_head_phone, name='e_head_phone'),
    url(r'^w_man/', views.watch_mans, name='w_man'),
    url(r'^w_woman/', views.watch_womans, name='w_woman'),
    url(r'^w_kid/', views.watch_kid, name='w_kid'),
    url(r'^gift/', views.gifts, name='gift'),
    url(r'^order/', views.order_products, name='order'),
    url(r'^my_order/', views.my_order_list, name='my_order'),
    url(r'^delete/(?P<id>\w{0,50})/$', views.order_delete, name='delete'),
    url(r'^edit/(?P<id>\w{0,50})/$', views.order_edit, name='edit'),
    url(r'^contact/', views.contact_us, name='contact'),
    url(r'^about/', views.about_us, name='about')


]
