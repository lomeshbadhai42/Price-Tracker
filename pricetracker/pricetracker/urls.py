"""
URL configuration for pricetracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from user.views import register
from django.contrib.auth.views import LoginView, LogoutView
from main_app.views import search, home, contact ,tracking ,remove_from_tracking

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path("search/", search, name="search"),
    path("register/", register, name="register-view"),
    path("login/", LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("tracking/", tracking, name="tracking"),
    path("contact/", contact, name="contact"),
    path('remove_from_tracking/<int:pk>/', remove_from_tracking, name='remove_from_tracking'),
]