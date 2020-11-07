from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo = models.ImageField(upload_to = 'profile/', null=True)
    email = models.CharField(max_length=60, null=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def owner(self):
        return self.user


    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

class Products(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    category = models.CharField(max_length=100, null=True)
    name = models.TextField()
    product_image = models.ImageField(upload_to = 'products/', null=True)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200,null=True)

    @classmethod
    def get_products(cls):
        products = Products.objects.all()
        return products
    
    @classmethod
    def find_products(cls,search_term):
        products = Products.objects.filter(title_icontains=search_term)
        return products 
    def update_products(self):
        self.update_products()

