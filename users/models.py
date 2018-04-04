from django.db import models

#
# user123
#
# admin123
#
# example@example.com
#

# Create your models here.
class User(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female')
    ]
    
    created_at = models.DateField(auto_now=True)
    name = models.CharField(max_length=80)
    slug = models.SlugField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

class ImageUser(models.Model):
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE,
        related_name = 'images'
    )
    image = models.ImageField()
