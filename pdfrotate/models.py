from django.db import models

# Create your models here.

class PDF(models.Model):
    file=models.FileField(null=False)
    page_num=models.IntegerField(null=False)
    an_of_rot=models.IntegerField(null=False)
    edited_file=models.FileField(null=True)
