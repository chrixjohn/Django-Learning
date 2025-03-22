from django.db import models

# Create your models here.

class director (models.Model):
    name=models.CharField(max_length=250)
class censorinfo(models.Model):
    rating=models.CharField(null=True)
    certified=models.CharField(null=True)

class movieinfo (models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()
    img=models.ImageField(upload_to='media/',null=True,blank=True)
    censor_details=models.OneToOneField(censorinfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    directed=models.ForeignKey(director,null=True,on_delete=models.CASCADE,related_name='direc')

    def __str__(self):
        return self.title




    