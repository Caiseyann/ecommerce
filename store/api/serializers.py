from rest_framework import serializers

from store.models import Products


class ProductsSerializer(serializers.ModelSerializer): # forms.ModelForm
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Products
        fields = [
            'url',
            'id',
            'user',
            'name',
            'category',
            'price',
            'description',
            'timestamp',
        ]
        read_only_fields = ['id', 'user']

    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        qs = Products.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value