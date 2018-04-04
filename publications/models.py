from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Publication(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    stars = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.title
