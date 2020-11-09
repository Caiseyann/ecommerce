from django.shortcuts import render
from .models import UserProfile
from django.views.generic import DetailView, ListView, UpdateView
from django.db.models import Prefetch
from .forms import UserForm, UserProfileForm

# Create your views here.
class UserProfileView(DetailView):
    template_name = 'authapp/user_profile.html'
    model = UserProfile
    context_object_name = 'profile'
    slug_url_kwarg = 'username'
    slug_field = 'user__username'


@login_required
def profile_redirector(request):
    return redirect('authapp:profile', username=request.user.username)
