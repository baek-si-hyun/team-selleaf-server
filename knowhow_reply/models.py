from django.db import models

from selleaf.models import Like, Period


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
