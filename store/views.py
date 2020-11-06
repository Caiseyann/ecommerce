from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http  import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    products = Project.get_products()
    profile = Profile.get_profile()
    return render(request, 'products/products.html', {"products": products})
