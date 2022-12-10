from django.db import models
from plot.models import Plot

# Create your models here.
class HouseType(models.Model):
    name = models.CharField( max_length = 255 )

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.name

class House(models.Model):
    house_name = models.CharField( max_length = 255 )    
    plot_number = models.ForeignKey( Plot, on_delete = models.CASCADE, null = False )
    house_type = models.ForeignKey( HouseType, on_delete = models.CASCADE, null = False)

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.house_name