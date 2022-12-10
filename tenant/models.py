from django.db import models

# Create your models here.
class Tenant(models.Model):
    id_number = models.CharField( max_length = 255 )
    gender = models.CharField( max_length = 255 )
    last_name = models.CharField( max_length = 255 )
    first_name = models.CharField( max_length = 255 )
    id_card_back_image = models.ImageField( upload_to='id_card' )
    id_card_front_image = models.ImageField( upload_to='id_card' )
    middle_name = models.CharField( max_length = 255, null = True )
    passport_size_photo = models.ImageField( upload_to='passport' )
    phone_number = models.CharField( max_length = 255, null = True )
    email_address = models.CharField( max_length = 255, null = True )
    
    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        full_name = self.first_name + " " + self.middle_name + " " + self.last_name
        return self.full_name

