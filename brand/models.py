from django.db import models

# Create your models here.

class distributor(models.Model):
    distri_name = models.CharField(max_length=  20, unique=True)
    distri_addr = models.CharField(max_length=  300)
    
    
    def __str__(self):
        return self.distri_name

class brands(models.Model):
    brand_name = models.CharField(max_length=  20, unique=True)
    brand_desc = models.CharField(max_length=  300)
    brand_cat = models.CharField(max_length= 20)
    brnad_distri = models.ForeignKey(distributor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.brand_name