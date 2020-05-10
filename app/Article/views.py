from django.shortcuts import render, HttpResponse
from django.views.generic import View
# Create your views here.

class Article(View):
    def get(self, request):

        return render(request, 'Article.html')

