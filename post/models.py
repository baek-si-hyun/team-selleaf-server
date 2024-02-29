from django.db import models

from selleaf.models import Period, File, Like, Plant, Scrap, Tag


class Post(Period):
    post_title = models.CharField(max_length=50, null=False)
    post_content = models.CharField(max_length=500, null=False)
    post_count = models.IntegerField(default=0, null=False)
    post_category = models.CharField(null=False)
    member = models.ForeignKey('Member', on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_post'


class PostFile(File):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_post_file'

class PostLike(Like):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_post_like'

class PostPlant(Plant):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_post_plant'

class PostScrap(Scrap):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    class Meta:
        db_table = 'tbl_post_scrap'

class PostTag(Tag):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_post_tag'

class PostCategory(models.Model):
    category_name = models.CharField(max_length=50, null=False)

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