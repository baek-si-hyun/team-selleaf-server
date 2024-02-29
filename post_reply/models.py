from django.db import models

from selleaf.models import Like, Period


class PostReply(Period):
    post_reply_content = models.CharField(null=False, max_length=50)
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_post_reply'

class PostReplyLike(Like):

    post_reply = models.ForeignKey('PostReply', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_post_reply_like'
