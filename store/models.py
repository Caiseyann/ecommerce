from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.urlresolvers import reverse
from rest_framework.reverse import reverse as api_reverse

# django hosts --> subdomain for reverse
# UserProfile class
class UserProfile(models.Model):

    USER_TYPES = (
        ('c', 'Customer'),
        ('a', 'Admin')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    profile_image = models.ImageField(upload_to = 'activis/', null=True)
    about = models.TextField(blank=True)
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default='c')


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.id and self.image:
            current_image = UserProfile.objects.get(pk=self.id).image
            if current_image != self.image:
                current_image.delete()
        super(UserProfile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        target = reverse('authapp:profile', args=[self.user.username])
        return target

    def is_customer(self):
        return self.user_type == 'c'

    def is_admin(self):
        return self.user_type == 'a'

class Products(models.Model):
    # pk aka id --> numbers
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    category      = models.TextField(max_length=30, null=True, blank=True)
    name       = models.CharField(max_length=120, null=True, blank=True)
    price =  models.IntegerField(default=0)
    description     = models.TextField(max_length=120, null=True, blank=True)

    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-store:post-rud", kwargs={'pk': self.pk}) '/api/store/1/'
    
    def get_api_url(self, request=None):
        return api_reverse("api-store:post-rud", kwargs={'pk': self.pk}, request=request)