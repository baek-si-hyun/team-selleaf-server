from django.db import models

from selleaf.Period import Period


class Knowhow(Period):
    knowhow_title = models.CharField(max_length=50, null=False)
    knowhow_content = models.CharField(max_length=500, null=False)
    knowhow_count = models.IntegerField(default=0, null=False)
    knowhow_category = models.ForeignKey('Category', on_delete=models.PROTECT)
    user = models.Foreignkey('User', on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_knowhow'

class KnowhowFile(models.Model):
    # knowhow_file_id (슈퍼키)
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_file'

class KnowhowLike(models.Model):
    # knowhow_like_id (슈퍼키)
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_like'

class KnowhowPlant(Period):
    plant = models.ForeignKey('PlantCategory', on_delete=models.PROTECT)
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_plant'
class KnowhowRecommend(models.Model):
    recommend_url = models.CharField(null=False)
    recommend_content = models.CharField(null=False, max_length=30)
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_recommend'



class KnowhowScrap(Period):
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_scrap'

class KnowhowTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT)
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_knowhow_tag'