from django.db import models

# Create your models here.
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    publication = models.ForeignKey(
        'publications.Publication', on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} -> {}'.format(self.created_by, self.publication)