from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# User includes username,password,email,first_name,last_name
# Additional includes additional information, i.e registration information-User information

class AddManager(models.Manager):
    def create_add(self, user, mobilenumber, location, city, country, zipcode, confirmpassword, dateofbirth, gender):
        add = self.create(user=user, mobilenumber=mobilenumber, location=location, city=city, country=country,\
                        zipcode=zipcode, confirmpassword=confirmpassword, dateofbirth=dateofbirth,\
                        gender=gender)
        return add


class AddSearch(models.Manager):
    def create_search(self, user, city, bar, coffee, restaurant, food, art, fashion, film, holiday, music, shopping, sport,\
                     outdoor, acti, trend):
        search = self.create(user=user, city=city, bar=bar, coffee=coffee, restaurant=restaurant, food=food, art=art,\
                          fashion=fashion, film=film, holiday=holiday, music=music, shopping=shopping, sport=sport,\
                          outdoor=outdoor, acti=acti, trend=trend)
        return search


class Registration(models.Model):
    user = models.OneToOneField(User)
    mobilenumber = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    dateofbirth = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    objects = AddManager()


class Search(models.Model):
    user = models.ForeignKey(User)
    city = models.CharField(max_length=100)
    bar = models.CharField(default=False, max_length=100)
    coffee = models.CharField(default=False, max_length=100)
    restaurant = models.CharField(default=False, max_length=100)
    food = models.CharField(max_length=100)

    art = models.CharField(default=False, max_length=100)
    fashion = models.CharField(default=False, max_length=100)
    film = models.CharField(default=False, max_length=100)
    holiday = models.CharField(default=False, max_length=100)
    music = models.CharField(default=False, max_length=100)
    shopping = models.CharField(default=False, max_length=100)
    sport = models.CharField(default=False, max_length=100)
    outdoor = models.CharField(default=False, max_length=100)
    acti = models.CharField(max_length=100)

    trend = models.CharField(default=False, max_length=100)

    objects = AddSearch()