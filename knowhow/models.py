from django.db import models

from plant.models import Plant
from selleaf.models import File, Like, Scrap, Tag
from selleaf.period import Period


class Knowhow(Period):
    knowhow_title = models.CharField(max_length=50, null=False)
    knowhow_content = models.CharField(max_length=500, null=False)
    knowhow_count = models.IntegerField(default=0, null=False)
    knowhow_category = models.CharField(null=False)
    member = models.ForeignKey('Member', on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_knowhow'

class KnowhowFile(File):
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_file'

class KnowhowLike(Like):
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_like'

class KnowhowPlant(Plant):
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_plant'
class KnowhowRecommend(models.Model):
    recommend_url = models.CharField(null=False)
    recommend_content = models.CharField(null=False, max_length=30)
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_recommend'



class KnowhowScrap(Scrap):
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_scrap'

class KnowhowTag(Tag):
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_knowhow_tag'

class KnowhowReply(Period):
    knowhow_reply_content = models.CharField(null=False, max_length=50)
    knowhow = models.ForeignKey('Knowhow', on_delete=models.PROTECT)
    member = models.ForeignKey('Member', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_reply'

class KnowhowReplyLike(Like):

    knowhow_reply = models.ForeignKey('KnowhowReply', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_knowhow_reply_like'
