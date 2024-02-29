from django.db import models
from member.models import Member
from selleaf.Period import Period


class Address(Period):
    address_zipcode = models.CharField(max_length=60,null=False,blank=False)
    address_city = models.CharField(max_length=255,null=False,blank=False)
    address_district = models.CharField(max_length=255,null=False,blank=False)
    address_detail = models.CharField(max_length=255,null=False,blank=False)

    class Meta:
        abstract = True


class City(Period):
    city_name = models.CharField(max_length=255,null=False,blank=False)

    class Meta:
        abstract = True


class District(City):
    district_name = models.CharField(max_length=255,null=False,blank=False)

    class Meta:
        abstract = True


class File(Period):
    file_url = models.ImageField(upload_to='file/%Y/%m/%d')

    class Meta:
        abstract = True


class Like(Period):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class Mileage(Period):
    mileage_status = models.BooleanField(default=True)
    mileage = models.BigIntegerField(null=False, blank=False)

    class Meta:
        abstract = True


class Scrap(Period):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class Tag(Period):
    tag_name = models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        abstract = True


class Alarm(Period):
    sender = models.ForeignKey(Member, on_delete=models.PROTECT, null=True, related_name='sender')
    receiver = models.ForeignKey(Member, on_delete=models.PROTECT, null=True, related_name='reciever', blank=True)
    # 확인 True 미확인 False
    alarm_status = models.BooleanField(null=True, default=False)

    class Meta:
        abstract = True
