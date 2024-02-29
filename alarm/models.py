from django.db import models

from knowhow.models import KnowhowReplyLike, KnowhowReply, KnowhowLike
from selleaf.models import Alarm
from apply.models import Apply
from lecture.models import LectureReview
from post.models import PostLike, PostReply, PostReplyLike

class ApplyAlarm(Alarm):
    Apply = models.ForeignKey(Apply,on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = 'tbl_apply_alarm'
        ordering = ['-id']

class ReviewAlarm(Alarm):
    lecture_review = models.ForeignKey(LectureReview,on_delete=models.PROTECT,blank=False, null=False)

    class Meta:
        db_table = 'tbl_lecture_review_alarm'
        ordering = ['-id']

class PostLikeAlarm(Alarm):
    post_like = models.ForeignKey(PostLike,on_delete=models.PROTECT,blank=False, null=False)

    class Meta:
        db_table = 'tbl_post_like_alarm'
        ordering = ['-id']

class PostReplyLikeAlarm(Alarm):
    post_reply_like = models.ForeignKey(PostReplyLike ,on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = 'tbl_post_reply_like_alarm'
        ordering = ['-id']


class PostReplyAlarm(Alarm):
    post_reply_like = models.ForeignKey(PostReplyLike, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = 'tbl_post_reply_alarm'
        ordering = ['-id']

class KnowhowLikeAlarm(Alarm):
    knowhow_like = models.ForeignKey(KnowhowLike, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = 'tbl_knowhow_like_alarm'
        ordering = ['-id']

class KnowhowReplyLikeAlarm(Alarm):
    knowhow_reply_like = models.ForeignKey(KnowhowReplyLike ,on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = 'tbl_knowhow_reply_like_alarm'
        ordering = ['-id']


class KnowhowReplyAlarm(Alarm):
    knowhow_reply = models.ForeignKey(KnowhowReply, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        db_table = 'tbl_knowhow_reply_alarm'
        ordering = ['-id']
