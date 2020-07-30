from django.shortcuts import render,redirect
from rest_framework import viewsets
from  .serializers import CultivoSerializer
from .models import Cultivo
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
# Create your views here.
class CultivoAppView():
    def index(self,request):
        return render(request,'api_rest/index.html')

class UsersAppView():
    def welcome(self,request):
        if request.user.is_authenticated:
            return render(request,'api_rest/users/welcome.html')
        return redirect('/login')
    
    def register(self,request):
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    do_login(request, user)
                    return redirect('/')
        return render(request,'api_rest/users/register.html',{'form':form})
    
    def login(self,request):
        form =AuthenticationForm()
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password) 
                if user is not None:
                    do_login(request, user)
                    return redirect('/')    
        return render(request,'api_rest/users/login.html',{'form':form})
    
    def logout(self,request):
        do_logout(request)
        return redirect('/')


class CultivoViewSet(viewsets.ModelViewSet):
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()
