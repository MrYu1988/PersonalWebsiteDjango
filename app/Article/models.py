from django.db import models
from db.base_model import BaseModel

# Create your models here.
class Article(BaseModel):
    '''
    文章表：包含文章编号、文档类别、文档名称、文章简介、文章内容
    '''
    ArticleType = models.CharField(max_length=128, verbose_name='文章类型')
    ArticleName = models.CharField(max_length=128, verbose_name='文章名称')
    ArticleBrief = models.CharField(max_length=256, verbose_name='文章简介')
    ArticleContext = models.CharField(max_length=128, verbose_name='文章内容')

    class Meta:
        db_table = 'df_Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name