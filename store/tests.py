from django.test import TestCase
from .models import *
# Create your tests here.
class ProfileTest(TestCase):
    self.user = User.objects.create(id = 1, username='userone')
    self.profile = Profile.objects.create (user = self.user, email = 'userone@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

class ProductsTest(TestCase):
    def setUp(self):

        self.products = Products.objects.create(profile = self.profile, category = 'shoes', name= 'black shoes', description = 'new shoes', price = '30')

    def test_instance(self):
        self.assertTrue(isinstance(self.products,Products))

    def test_get_products(self):
        self.products.save()
        products = Products.get_products()
        self.assertTrue(len(products) == 1)

    def test_find_products(self):
        self.products.save()
        products = Products.find_products('blog')
        self.assertTrue(len(products) > 0)
