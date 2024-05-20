from django.db import models

from member.models import Member
from post.models import Post
from selleaf.models import Tag


class AiPost(models.Model):
    post_title = models.CharField(max_length=80, null=False)
    post_content = models.CharField(max_length=8000, null=False)
    post_tags = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'tbl_ai_post'


class AiKnowhow(models.Model):
    knowhow_title = models.CharField(max_length=80, null=False)
    knowhow_content = models.CharField(max_length=8000, null=False)
    knowhow_category = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'tbl_ai_knowhow'


class AiPostReply(models.Model):
    POSTREPLY_STATUS = [
        (0, '비활성화'),
        (1, '활성화'),
    ]
    post_reply_content = models.CharField(null=False, max_length=50)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)
    post_reply_status = models.IntegerField(choices=POSTREPLY_STATUS, default=1)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_ai_post_reply'
        ordering = ['-id']
