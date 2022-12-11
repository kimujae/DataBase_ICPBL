from django.db import models
from common.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=200, unique = True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/board/category/{self.slug}/'
    class Meta:
        verbose_name_plural = 'Categories'

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_NULL)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


# Create your models here.
class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Photo(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

