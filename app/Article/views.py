from django.shortcuts import render, HttpResponse
from django.views.generic import View
from Article.models import ArticleModels, ArticleType
# Create your views here.

class Article(View):
    def get(self, request):

        # Programs = BigProgram.objects.all()
        # # 依据大项目名称查找大项目下的子项目名称和类别
        # for Program in Programs:
        #     SubPrograms = SubProgram.objects.filter(SubProgramId=Program).order_by('update_time')
        #     Program.SubPrograms = SubPrograms
        #
        # #  将查询到的项目放入网页中
        # context = {'Programs':Programs}

        ArticleTypeTmps = ArticleType.objects.all()
        for Article in ArticleTypeTmps:
            Articles = ArticleModels.objects.filter(ArticleId = Article).order_by('update_time')
            Article.Articles = Articles
        context = {'Articles':ArticleTypeTmps}

        return render(request, 'Article.html', context)


class ArticleDetail(View):
    def get(self, request, ArticleID):

        Articles = ArticleModels.objects.filter(id=ArticleID)
        if Articles == None:
            return render(request, 'ArticleDetail.html')
        # 打开html文件内容
        myfile = Articles[0].ArticleHtml.open()
        # 读取文件内容
        bb = myfile.read()
        # 关闭文件
        myfile.close()
        # 对文件进行解码
        tempstr = bb.decode('utf-8')
        # 删除字符串‘body前的内容’
        tempstr = tempstr[(tempstr.find('<body>') + 6):]
        # 删除body后的内容
        tempstr = tempstr[:(tempstr.find('body>') - 2)]

        context = {'body': tempstr,
                   'Article':Articles[0]}

        return render(request, 'ArticleDetail.html', context)


