from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.

class User(AbstractUser):
    mobilenumber = models.CharField(max_length=10, null=True)
    uimg = models.ImageField(upload_to='ProfilePic/',default='profilepic.png')
    t = [(1,'Guest'),(2,'Manager'),(3,'User')]
    role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
    f = [(2,'Manager'),(3,'User')]
    rltype = models.IntegerField(choices = f)
    pfe = models.ImageField(upload_to='ID_Prf/',default='profilepic.png')
    is_checked = models.BooleanField(default=False)
    uname = models.CharField(max_length=50)
    ud = models.OneToOneField(User, on_delete=models.CASCADE)

class Rooms(models.Model):
    rno = models.IntegerField()
    rdes = models.CharField(max_length=200)
    rcost = models.DecimalField(max_digits=10, decimal_places=2)
    rimg = models.ImageField(upload_to = 'Roomsimg/',default = 'profilepic.png')
    uid = models.ForeignKey(User,on_delete=models.CASCADE)

class Bookings(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    rid = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    rno = models.IntegerField()
    sdate = models.DateField()
    edate= models.DateField()
    is_checkin = models.BooleanField(default=False)
    ci_date = models.DateField(null=True)
    co_date = models.DateField(null=True)