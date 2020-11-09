from django.conf.urls import url


from .views import ProductsRudView, ProductsAPIView

urlpatterns = [
    url(r'^$', ProductsAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', ProductsRudView.as_view(), name='post-rud')
]   