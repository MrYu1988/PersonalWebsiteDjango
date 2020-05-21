from django.db import models
from db.base_model import BaseModel

# Create your models here.
'''相片名称、相片、相片类型、存储时间等'''

class LiftModels(BaseModel):

    LiftName = models.CharField(max_length=128, verbose_name='图片名称')

    LiftIcon = models.ImageField(upload_to='img')
    LiftId = models.ForeignKey('LiftType', verbose_name='图片编号', on_delete=models.CASCADE)

    class Meta:
        db_table = 'df_Life'
        verbose_name = '生活'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.LiftName

class LiftType(models.Model):
    '''

    '''

    LiftType = models.CharField(max_length=128, verbose_name='图片类型')
    class Meta:
        db_table = 'df_LifeType'
        verbose_name = '生活类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.LiftType