"""user_authentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from api_rest.views import CultivoAppView,UsersAppView

cultivo_app_view = CultivoAppView()
user_view = UsersAppView()
urlpatterns = [
    path('api/',include('api_rest.urls')),
    # path('', cultivo_app_view.index, name ='index'),
    # path('index.htm',cultivo_app_view.index, name = 'index')
    path('', user_view.welcome),
    path('register', user_view.register),
    path('login', user_view.login),
    path('logout', user_view.logout),
    path('admin/', admin.site.urls),
]
