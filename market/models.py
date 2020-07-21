from django.db import models

# Create your models here.
class Market(models.Model):
    title       = models.CharField(max_length=50,blank=False,default="New market")
    description = models.TextField(blank=False,default="Yaha sab milta hai bhai")
    city        = models.CharField(max_length=50,blank=False,default="Bhopal")
    image       = models.ImageField(upload_to='markets',default="default.png")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('market-list')
