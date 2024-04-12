from django.db import models
from django.conf import settings

'''
 In order to keep your code generic, use the get_user_model() method to retrieve the user 
model and the AUTH_USER_MODEL setting to refer to it when defining a model’s relationship 
with the user model, instead of referring to the auth user model directly.
'''


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
