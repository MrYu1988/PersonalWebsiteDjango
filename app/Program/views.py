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


class SubProgramDetail(View):
    def get(self, request, ProgramID, SubProgramID):
        print(ProgramID)
        print(SubProgramID)

        SubPrograms = SubProgram.objects.filter(id=SubProgramID)
        if SubPrograms is None:
            return render(request, 'ProgramContext.html')
        # 打开html文件内容
        myfile = SubPrograms[0].SubProgramHtml.open()
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
                   'SubProgram':SubPrograms[0]}
        return render(request, 'ProgramContext.html', context)


class SubProgramUnqul(View):
    def get(self, request, ProgramID):
        # 查询大项目名称
        Programs = BigProgram.objects.filter(id=ProgramID).order_by('update_time')
        # 依据大项目名称查找大项目下的子项目名称和类别
        for Program in Programs:
            SubPrograms = SubProgram.objects.filter(SubProgramId=Program).order_by('update_time')
            Program.SubPrograms = SubPrograms

        #  将查询到的项目放入网页中
        context = {'Programs':Programs}
        return render(request, 'Program.html', context)

