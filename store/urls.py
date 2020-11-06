from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^all/(?P<pk>\d+)', views.all, name='all'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url(r'^api/product/$', views.ProductList.as_view()),
    url(r'api/product/product-id/(?P<pk>[0-9]+)/$',views.ProductDescription.as_view()),
    url(r'api/product/product-id/delete(?P<pk>[0-9]+)/$',views.ProductDescription.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)