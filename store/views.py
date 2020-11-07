from .models import *
from .serializer import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from rest_framework import status
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm, NewProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.http import JsonResponse

# Create your views here.
def signUp(request):
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home.html')
     else:
        form = SignUpForm()
        return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def home(request):
    products = Products.get_products()
    profile = Profile.get_profile()
    return render(request, 'products/products.html', {"products": products})

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):

    profile = Profile.objects.get(pk = profile_id)
    products = Project.objects.filter(profile_id=profile).all()

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
    return render(request, 'add_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_project = Project.find_project(search_term)
        message = search_term

        return render(request,'search.html',{"message":message, "searched_products":searched_products})
    else:
        message = "You haven't searched for any products"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def all(request, pk):
    profile = Products.objects.get(pk=pk)
    content = {
        "profile": profile,
        'products': products,
    }
    return render(request, 'products/products.html', content)


class ProfileList(APIView):

    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductsList(APIView):

    def get(self, request, format=None):
        all_products = Products.objects.all()
        serializers = ProductsSerializer(all_products, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProductsSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_products(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        products= self.get_products(pk)
        serializers = ProductsSerializer(products)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        products = self.get_products(pk)
        serializers = ProductsSerializer(products, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        products = self.get_products(pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
