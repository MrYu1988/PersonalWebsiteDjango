from django.db import models
from db.base_model import BaseModel

# Create your models here.
class ArticleModels(BaseModel):
    '''
    文章表：包含文章编号、文档类别、文档名称、文章简介、文章内容
    '''

    ArticleName = models.CharField(max_length=128, verbose_name='文章名称')
    ArticleBrief = models.CharField(max_length=256, verbose_name='文章简介')
    ArticleId = models.ForeignKey('ArticleType', verbose_name='文章编号', on_delete=models.CASCADE)
    ArticleDoc = models.FileField(upload_to='doc', null=True)
    ArticleHtml = models.FileField(upload_to='Html', blank=True, null=True)

    class Meta:
        db_table = 'df_Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ArticleName


class ArticleType(BaseModel):
    ArticleID = models.CharField(max_length=128, verbose_name='文章类型', default=0)

    class Meta:
        db_table = 'df_ArticleType'
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ArticleID