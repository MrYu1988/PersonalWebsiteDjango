from django.shortcuts import render, HttpResponse
from django.views.generic import View
from Program.models import BigProgram
from Article.models import ArticleModels
from Life.models import LiftModels
# Create your views here.

class index(View):
    def get(self, request):
        '''获取整个项目的内容'''
        BigPrograms = BigProgram.objects.all().order_by('update_time')[:4]
        ArticleModelsTmp = ArticleModels.objects.all().order_by('update_time')[:4]
        LiftModelsTmp = LiftModels.objects.all().order_by('update_time')[:8]

        context = {'BigProgramtemp' : BigPrograms,
                   'ArticleModelsTmp' : ArticleModelsTmp,
                   "LiftModelsTmp" : LiftModelsTmp}

        return render(request, 'index.html', context)

