from django.db import models
from django.utils import timezone

class Period(models.Model):
    created_date = models.DateTimeField(null=False, auto_now_add=True)
    updated_date = models.DateTimeField(null=False, default=timezone.now)

    class Meta:
        abstract = True

class Address(Period):
    address_zipcode = models.CharField(max_length=60,null=False,blank=False)
    address_city = models.CharField(max_length=255,null=False,blank=False)
    address_district = models.CharField(max_length=255,null=False,blank=False)
    address_detail = models.CharField(max_length=255,null=False,blank=False)

    class Meta:
        abstract = True

class City(Period):
    area_name = models.CharField(max_length=255,null=False,blank=False)

    class Meta:
        abstract = True

class File(Period):
    file_url = models.FileField(upload_to='file/%Y/%m/%d')

    class Meta:
        abstract = True

class Like(Period):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True

class District(Period):
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    class Meta:
        abstract = True

class Mileage(Period):
    mileage_status = models.BooleanField(default=True)
    mileage = models.BigIntegerField(null=False, blank=False)

    class Meta:
        abstract = True


class Plant(Period):
    plant_name = models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        abstract = True


class Scrap(Period):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True

class Tag(Period):
    tag_name = models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        abstract = True