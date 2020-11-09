from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    url(r'^registerPage/$', views.signUp, name='signPage'),
    url(r'^$', views.home,name='home'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^all/(?P<pk>\d+)', views.all, name='all'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url(r'^api/products/$', views.ProductsList.as_view()),
    url(r'api/products/products-id/(?P<pk>[0-9]+)/$',views.ProductsDescription.as_view()),
    url(r'api/products/products-id/delete(?P<pk>[0-9]+)/$',views.ProductsDescription.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
