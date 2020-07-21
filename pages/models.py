from django.db import models

# Create your models here.

class Slide(models.Model):
    image=models.ImageField(upload_to='Slides')

    def __str__(self):
        return self.image.name

    def get_absolute_url(self):
        return reverse('market-list')

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img=Image.open(self.image.path)
    #     if img.height>300 or img.width >300 :
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class Category(models.Model):
    short   = models.CharField(max_length=4,unique=True)
    long    = models.CharField(max_length=30,unique=True)
    is_service = models.BooleanField(default = False,blank = False)
    def __str__(self):
        return self.long+" -> " +self.short

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    short   = models.CharField(max_length=6,unique=True)
    long    = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.category.long + " -> " + self.long + "(" + self.short + ")"

class Tag(models.Model):
    title  = models.CharField(max_length=50)
    def __str__(self):
        return self.title
