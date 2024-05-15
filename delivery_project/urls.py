"""delivery_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from customers import views as customer_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delivery.urls')),
    path('register/', customer_views.register, name='register'),
    path('activate/<uidb64>/<token>/', customer_views.activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='customers/logout.html'), name='logout'),
    path('profile/', customer_views.profile, name='profile'),
    path('confirm_logout/', customer_views.confirm_logout, name='confirm_logout'),
    path('account_activation_sent/', customer_views.account_activation_sent, name='account_activation_sent' ),
    path('account_activation_successful/', customer_views.account_activation_successful, name='account_activation_successful'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='customers/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='customers/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='customers/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='customers/password_reset_complete.html'), name='password_reset_complete.html'),
]
