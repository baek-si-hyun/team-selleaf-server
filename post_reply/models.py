# from django.db import models
#
# class PostReply(models.Model):
#     post_reply_content = models.CharField(null=False, max_length=50)
#     post = models.ForeignKey('Post', on_delete=models.PROTECT)
#     user = models.Foreignkey('User', on_delete=models.PROTECT)
#     class Meta:
#         db_table = 'tbl_post_reply'
#
# class PostReplyLike(models.Model):
#
#     post_reply = models.ForeignKey('PostReply', on_delete=models.PROTECT)
#     class Meta:
#         db_table = 'tbl_post_reply_like'