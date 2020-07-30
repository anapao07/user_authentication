from django.shortcuts import render
from rest_framework import viewsets
from  .serializers import CultivoSerializer
from .models import Cultivo
# Create your views here.
class CultivoAppView():
    def index(self,request):
        return render(request,'api_rest/index.html')


class CultivoViewSet(viewsets.ModelViewSet):
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()
