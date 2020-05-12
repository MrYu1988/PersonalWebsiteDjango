from django.contrib import admin
from Program.models import BigProgram, SubProgram
from PersonalWebsiteDjango.settings import MEDIA_ROOT
from pydocx import PyDocX
import re

# Register your models here.
class BigProgramAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''新增或更新表中的数据时调用'''
        super().save_model(request, obj, form, change)
        print('test')


class SubProgramAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''新增或更新表中的数据时调用'''
        super().save_model(request, obj, form, change)
        subProgram = SubProgram.objects.filter(SubProgramName=obj)
        for programTmp in subProgram:
            if programTmp.SubProgramDoc.name:
                if programTmp.SubProgramDoc.name.endswith('.docx'):
                    path = MEDIA_ROOT + '/' + programTmp.SubProgramDoc.name
                    pathHtml = MEDIA_ROOT  + '/Html/' + programTmp.SubProgramName +'.html'
                    html = PyDocX.to_html(path)  # 转为html，如：D:\\test\\文件2.docx
                    f = open(pathHtml, 'w', encoding="utf-8")  # 变为如：D:\\test\\文件2.html
                    f.write(html)
                    f.close()
                    SubProgram.objects.filter(SubProgramName = programTmp.SubProgramName).update(SubProgramHtml = pathHtml)
                    print(pathHtml)


admin.site.register(BigProgram, BigProgramAdmin)
admin.site.register(SubProgram, SubProgramAdmin)