from django.db import models

# Create your models here.

class Spot(models.Model):
    post = models.CharField(max_length=500)
    photo_url=models.TextField()
    spot_time=models.DateField()
    
    def __str__(self):
        return self.post
    
class Comments(models.Model):
    post =models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='comments')
    comment_time =models.DateField()
    
    