from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.product_list, name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]