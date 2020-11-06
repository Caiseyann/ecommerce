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

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):

    profile = Profile.objects.get(pk = profile_id)
    projects = Project.objects.filter(profile_id=profile).all()

    return render(request,"profile.html",{"profile":profile})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

