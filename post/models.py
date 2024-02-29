# from django.db import models
#
# class Post(models.Model):
#     post_title = models.CharField(max_length=50, null=False)
#     post_content = models.CharField(max_length=500, null=False)
#     post_count = models.IntegerField(default=0, null=False)
#     post_category = models.ForeignKey('Category', on_delete=models.PROTECT)
#     user = models.Foreignkey('User', on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'tbl_post'
#
#
# class PostFile(models.Model):
#     # post_file_id (슈퍼키)
#     post = models.ForeignKey('Post', on_delete=models.PROTECT)
#     class Meta:
#         db_table = 'tbl_post_file'
#
# class PostLike(models.Model):
#     # post_like_id (슈퍼키)
#     post = models.ForeignKey('Post', on_delete=models.PROTECT)
#     class Meta:
#         db_table = 'tbl_post_like'
#
# class PostPlant(models.Model):
#     plant = models.ForeignKey('PlantCategory', on_delete=models.PROTECT)
#     post = models.ForeignKey('Post', on_delete=models.PROTECT)
#     class Meta:
#         db_table = 'tbl_post_plant'
#
# class PostScrap(models.Model):
#     post = models.ForeignKey('Post', on_delete=models.PROTECT)
#     class Meta:
#         db_table = 'tbl_post_scrap'
#
# class PostTag(models.Model):
#     tag = models.ForeignKey('Tag', on_delete=models.PROTECT)
#     post = models.ForeignKey('Post', on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'tbl_post_tag'
#
# class PostCategory(models.Model):
#     category_name = models.CharField(max_length=50, null=False)