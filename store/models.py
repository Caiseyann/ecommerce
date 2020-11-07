from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
#     profile_photo = models.ImageField(upload_to = 'profile/', null=True)
#     email = models.CharField(max_length=60, null=True)

#     def __str__(self):
#         return str(self.user.username)

  
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#         post_save.connect(create_user_profile, sender=User)

#     def save_profile(self):
#         self.save()

#     @classmethod
#     def get_profile(cls):
#         profile = Profile.objects.all()

#         return profile

# class Products(models.Model):
#     category = models.CharField(max_length=100, null=True)
#     product_image = models.ImageField(upload_to = 'products/', null=True)
#     description = models.CharField(max_length=200,null=True)

#     @classmethod
#     def get_products(cls):
#         products = Products.objects.all()
#         return products
    
#     @classmethod
#     def find_products(cls,search_term):
#         products = Products.objects.filter(title_icontains=search_term)
#         return products 
#     def update_products(self):
#         self.update_products()























class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update_category()



class Image(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    category_image = models.ImageField(upload_to = 'products/', null=True)
    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()


    @classmethod
    def search_by_category(cls,search_term):
        store = cls.objects.filter(category__name__icontains=search_term)
        return store

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images


    @classmethod
    def get_image_by_id(cls,id):
        img_id = cls.objects.get(pk=id)
        return img_id

