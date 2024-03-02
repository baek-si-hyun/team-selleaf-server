from django.db import models
from member.models import Member
from selleaf.period import Period


class City(Period):
    city_name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        abstract = True


class District(City):
    district_name = models.CharField(max_length=255, null=False, blank=False)

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
    tag_name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        abstract = True



