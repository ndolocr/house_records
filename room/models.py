from django.db import models
from house.models import House
# Create your models here.
class RoomType(models.Model):
    name = models.CharField( max_length = 255 )

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.name  

class Room(models.Model):
    room_name = models.CharField( max_length = 255 )
    room_description = models.TextField( null = True)
    kplc_meter_number = models.CharField( max_length = 255 )    
    room_type = models.ForeignKey( RoomType, on_delete = models.CASCADE, null = False)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null = False)

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.room_name + " - " + str(self.house)