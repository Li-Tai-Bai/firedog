from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
def index(request):

    context = {'name': 'the double eleven, go click will be surprised!'}
    return render(request, 'book/index.html', context=context)
