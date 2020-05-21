from django.shortcuts import render
from django.views.generic import View
from Life.models import LiftModels,LiftType
# Create your views here.
class LifeDisplay(View):
    def get(self, request):

        LiftTypeTmps = LiftType.objects.all()
        for Lift in LiftTypeTmps:
            Lives = LiftModels.objects.filter(LiftId = Lift).order_by('update_time')
            Lift.Lives = Lives
        context = {'Lives':LiftTypeTmps}

        return render(request, 'Life.html', context)

