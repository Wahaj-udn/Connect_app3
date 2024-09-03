# connect_app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_alumni = models.BooleanField(default=False)
    roll_number = models.CharField(max_length=20, blank=True, null=True)
    current_job = models.CharField(max_length=100, blank=True, null=True)
    areas_of_expertise = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    POST_TYPES = [
        ('query', 'Query'),
        ('update', 'Update'),
        ('announcement', 'Announcement'),
        ('internship', 'Internship'),
        ('workshop', 'Workshop'),
    ]

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    post_type = models.CharField(max_length=50, choices=POST_TYPES, default='update')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.get_post_type_display()}"

    class Meta:
        ordering = ['-created_at']
