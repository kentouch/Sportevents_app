from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=PROTECT, default=1)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    post_image = models.ImageField(upload_to='images/', blank= True,  default='images/default.png')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='posts_likes')
    

    # counting the number of likes
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    body = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return '%s - %s' %(self.post, self.name)