from django.db import models
from db.base_model import BaseModel

# Create your models here.

class BigProgram(BaseModel):
    '''项目表：项目编号id
    项目图标
    项目简介'''
    ProgramIcon = models.ImageField(upload_to='img')
    ProgramBrief = models.CharField(max_length=256, verbose_name='项目简介')
    ProgramName = models.CharField(max_length=64, verbose_name='项目名称')

    class Meta:
        db_table = 'df_Program'
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ProgramName

class SubProgram(BaseModel):
    '''项目表：项目编号id
    项目图标
    项目简介'''
    SubProgramName = models.CharField(max_length=64, verbose_name='子项目名称')
    SubProgramBrief = models.CharField(max_length=256, verbose_name='子项目简介')
    SubProgramId = models.ForeignKey('BigProgram', verbose_name='子项目编号', on_delete=models.CASCADE)
    SubProgramDoc = models.FileField(upload_to='doc', null=True)
    SubProgramHtml = models.FileField(upload_to='Html', blank=True, null=True)

    class Meta:
        db_table = 'df_SubProgram'
        verbose_name = '子项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.SubProgramName

