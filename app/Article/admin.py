from django.contrib import admin
from Article.models import ArticleModels,ArticleType
from PersonalWebsiteDjango.settings import MEDIA_ROOT
from pydocx import PyDocX

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''新增或更新表中的数据时调用'''
        super().save_model(request, obj, form, change)
        print("2222")
        ArticleNames = ArticleModels.objects.filter(ArticleName=obj)
        for Article in ArticleNames:
            if Article.ArticleDoc.name:
                if Article.ArticleDoc.name.endswith('.docx'):
                    path = MEDIA_ROOT + '/' + Article.ArticleDoc.name
                    pathHtml = MEDIA_ROOT  + '/Html/' + Article.ArticleName +'.html'
                    html = PyDocX.to_html(path)  # 转为html，如：D:\\test\\文件2.docx
                    f = open(pathHtml, 'w', encoding="utf-8")  # 变为如：D:\\test\\文件2.html
                    f.write(html)
                    f.close()
                    ArticleModels.objects.filter(ArticleName = Article.ArticleName).update(ArticleHtml = pathHtml)
                    print(pathHtml)
                    print('good')

admin.site.register(ArticleModels, ArticleAdmin)
admin.site.register(ArticleType)