from rest_framework import serializers
from .models import User, Spot, Commments

class SpotSerializer(serializers.ModelSerializer):
    class Mets:
        model = Spot
        fields = ('name','post','photo_url')
        
        
        


# guidance of serializers in part byL: https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react