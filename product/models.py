from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import User


objects=models.Manager()
choice = (('Fruits' ,'Fruits'),
          ('vegetable' , 'Vegetable'),
          ('LandEquipment' , 'Land Equipment'),
          ('RentLand' , 'Rent Land'),
          ('other', 'other',))

class Auction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=64)
    describe = models.CharField(max_length=300)
    bid = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/images/')
    category = models.CharField(max_length=60,choices=choice,default='Fruits')

    def __str__(self):
        return str(self.user)

class Bid(models.Model):
    user=models.CharField(max_length=64)
    title=models.CharField(max_length=64)
    bid=models.IntegerField()

class comment(models.Model):
    user = models.CharField(max_length=64)
    comments = models.CharField(max_length=140,blank=True,null=True)
    listid = models.IntegerField(default=0)


class watchs(models.Model):
    user = models.CharField(max_length=64)
    auctionh = models.IntegerField()

class Closebid(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listid = models.IntegerField()
    bidprice = models.IntegerField()
    image1 = models.ImageField(blank=True, null=True)