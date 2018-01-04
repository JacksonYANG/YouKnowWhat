from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'UserInfo'
    id = models.AutoField(primary_key=True, max_length=500,db_column='UID')
    UserName = models.CharField(max_length=50,db_column='username',blank=False)
    Password = models.CharField(max_length=50,db_column='password',blank=False)
    Phone = models.CharField(max_length=15,db_column='phone',blank=False)