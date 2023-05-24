from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    worth = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    photo = models.ImageField(upload_to='home/images')

    def __str__(self):
        return self.product_name
    

    #location
    #count
    #seller validity
    #seller id
    