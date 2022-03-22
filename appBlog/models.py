from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Blog_post')
    blog_title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(unique=True)
    blog_content = models.TextField(blank=False, null=False)
    blog_images = models.ImageField(upload_to='blog_images')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =['-publish_date']
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_commnet')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Blog_commnet')
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Blog_like')

    def __str__(self):
        return self.user+ "Likes" +self.blog
