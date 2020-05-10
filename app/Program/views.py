from django.shortcuts import render, HttpResponse
from django.views.generic import View
# Create your views here.

class Program(View):
    def get(self, request):

        return render(request, 'Program.html')
