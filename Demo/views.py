

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def show(request):
    name = request.POST.get("name", 'default')
    pass1 = request.POST.get("pass", 'def')
    remove = request.POST.get("remove", "off")
    params = {
        'name': name,
        'pass': pass1,
        'remove': remove
    }
    print(name)
    return render(request, 'show.html', params)
