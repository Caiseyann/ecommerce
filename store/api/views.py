# generic

from django.db.models import Q
from rest_framework import generics, mixins

from store.models import Products
from .permissions import IsAuthenticated
from .serializers import ProductsSerializer


class ProductsAPIView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = ProductsSerializer
    permission_classes      = [IsAuthenticated]
    #queryset                = Products.objects.all()

    def get_queryset(self):
        qs = Products.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ProductsRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = ProductsSerializer
    permission_classes      = [IsAuthenticated]
    #queryset                = Products.objects.all()

    def get_queryset(self):
        return Products.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Products.objects.get(pk=pk)
