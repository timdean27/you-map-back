from django.db import models

# Create your models here.

class User(models.Model):
    user_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name

class Spot(models.Model):
    user_name=models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=500)
    name=models.CharField(max_length=200)
    coordinates_lat=models.CharField(max_length=100)
    coordinates_lng=models.CharField(max_length=100)
    photo_url=models.TextField()
    spot_time=models.DateField()
    
    def __str__(self):
        return self.post
    
class Comments(models.Model):
    post =models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='comments')
    comment_content = models.CharField(max_length=500, default='no comment')
    comment_time =models.DateField()
    
    def __str__(self):
        return self.post
    