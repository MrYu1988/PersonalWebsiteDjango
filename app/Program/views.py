from django.shortcuts import render, HttpResponse
from django.views.generic import View
from Program.models import BigProgram,SubProgram
# Create your views here.

class ProgramWeb(View):
    def get(self, request):
        # 查询大项目名称
        Programs = BigProgram.objects.all()
        # 依据大项目名称查找大项目下的子项目名称和类别
        for Program in Programs:
            SubPrograms = SubProgram.objects.filter(SubProgramId=Program).order_by('update_time')
            Program.SubPrograms = SubPrograms

        #  将查询到的项目放入网页中
        context = {'Programs':Programs}
        return render(request, 'Program.html', context)
