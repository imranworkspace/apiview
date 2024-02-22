from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(unique=True,blank=True)
    city=models.CharField(max_length=15,default='latur')
    profile_pic = models.ImageField(upload_to='images/', default='', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table="students"