"""pet_adoption URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('master/',views.Master,name ='master'),
    path('',views.Index,name ='index'),
    # path('index',views.Index,name ='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    # path('signup', views.signup, name='signup'),
    path('/login1',include('django.contrib.auth.urls')),
    path('signin', views.signin, name='signin'),
    path('signin_2', views.signin_2, name='signin_2'),
    path('login1', views.login1, name='login1'),
    path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('product',views.product_page,name='product'),
    path('product/',views.product_page,name='product'),
    path('product/<str:id>',views.product_details,name='product_details'),
    path('service/',views.service,name='service'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),     

    path('adopt/',views.adopt,name='adopt'),
    path('adopt/<str:id>',views.adopt_details,name='adopt_details'),
    path('adopt_page',views.adopt_page,name='adopt_page'),
    path('adoptform',views.adoptform,name='adoptform'),
    path('formsubmition',views.formsubmition,name='formsubmition'),
    path('Servicesumbit',views.Servicesumbit,name='Servicesumbit'),
    path('checkout/',views.CheckOut,name='checkout'),
    path('success', views.success, name='success'),
#   blog start
    path('try1',views.try1,name='try1'),

#     cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/',views.cart_detail,name='cart_detail'),
    path('search/', views.Search, name='search'),
    path('contact_us',views.contact_page,name='contact_page'),
    # path('video', views.video, name='video'),
    # path('audio', views.audio, name='audio'),

#   blog start
    path('blog', views.blog, name='blog'),
    path('blog', views.blog, name='blog'),
    path('trainpuppy', views.trainpuppy, name='trainpuppy'),
    path('nerdycat', views.nerdycat, name='nerdycat'),
    path('catbreed', views.catbreed, name='catbreed'),
    path('dogbreeder', views.dogbreeder, name='dogbreeder')
    # later delete(only for testing)
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
