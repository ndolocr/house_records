from django.db import models

# Create your models here.

class Plot(models.Model): 
    COUNRY_LIST_CHOICES = [        
        ("Lamu", "Lamu"),
        ("Meru", "Meru"),
        ("Embu", "Embu"),
        ("Kisii", "Kisii"),
        ("Bomet", "Bomet"),
        ("Narok", "Narok"),
        ("Nyeri", "Nyeri"),
        ("Kitui", "Kitui"),
        ("Kwale", "Kwale"),
        ("Wajir", "Wajir"),
        ("Nandi", "Nandi"),
        ("Busia", "Busia"),
        ("Siaya", "Siaya"),
        ("Kiambu", "Kiambu"),
        ("Isiolo", "Isiolo"),
        ("Kilifi", "Kilifi"),
        ("Nakuru", "Nakuru"),
        ("Vihiga", "Vihiga"),
        ("Kisumu", "Kisumu"),
        ("Migori", "Migori"),
        ("Nairobi", "Nairobi"),
        ("Nyamira", "Nyamira"),
        ("Baringo", "Baringo"),
        ("Samburu", "Samburu"),
        ("Turkana", "Turkana"),
        ("Garissa", "Garissa"),
        ("Mombasa", "Mombasa"),
        ("Mandera", "Mandera"),
        ("Makueni", "Makueni"),
        ("Kajiado", "Kajiado"),
        ("Kericho", "Kericho"),
        ("Bungoma", "Bungoma"),
        ("Homa Bay", "Homa Bay"),
        ("Kakamega", "Kakamega"),
        ("Laikipia", "Laikipia"),
        ("Marsabit", "Marsabit"),
        ("Machakos", "Machakos"),
        ("Murang’a", "Murang’a"),        
        ("Kirinyaga", "Kirinyaga"),
        ("Nyandarua", "Nyandarua"),        
        ("Tana River", "Tana River"),
        ("West Pokot", "West Pokot"),
        ("Trans-Nzoia", "Trans-Nzoia"),
        ("Uasin Gishu", "Uasin Gishu"),
        ("Tharaka-Nithi", "Tharaka-Nithi"),
        ("Taita Taveta", "Taita Mak Taveta"),
        ("Elgeyo-Marakwet", "Elgeyo-Marakwet"),
        
    ]
    street = models.CharField( max_length = 255 )
    section = models.CharField( max_length = 255 )
    location = models.CharField( max_length = 255)
    plot_number = models.CharField( max_length = 255 )
    land_reference = models.CharField( max_length = 255 )
    county = models.CharField(max_length=255, choices=COUNRY_LIST_CHOICES)

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)
    
    def __str__(self):
        return self.plot_number