from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Model field

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="token")
    token = models.CharField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string(length=64)
        return super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        UserToken.objects.create(user=instance)

# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.crypto import get_random_string

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=100)
#     bio = models.CharField(max_length=100)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Model field

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username

# class UserToken(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
#     token = models.CharField(max_length=64, unique=True)

#     def save(self, *args, **kwargs):
#         if not self.token:
#             self.token = get_random_string(length=64)
#         return super().save(*args, **kwargs)
