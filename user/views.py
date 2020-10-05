from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.


def signup(request):
    return render(request, 'user/signup.html')


def login(request):
    return render(request, 'user/login.html')


def loginresult(request):
    if(request.POST.get("name")=='' or request.POST.get('password')==''):
        return render(request,'user/login.html')
    name = request.POST.get('name')
    pwd = request.POST.get('password')
    user = User.objects.get(user_name=name)

    if (user!=None and user.user_password==pwd):
        allUsers = User.objects.all()
        print(allUsers[0])
        request.session['user_name'] = name
        params = {'users': allUsers, 'user_name': request.session['user_name']}

        return render(request, 'user/index.html', params)
    request.session['user_name']=''
    return render(request, 'user/login.html')


def signup1(request):
    name = request.POST.get('name')
    pwd = request.POST.get('password')
    usr=User.objects.filter(user_name=name,user_password=pwd)
    if(usr==None):
        return render(request,'user/signup.html')
    user = User(user_name=name, user_password=pwd)
    user.save()
    print(user.user_id)
    return render(request, 'user/index.html')


def index(request):
    if(request.session['user_name']==None):
        return render(request,'user/login.html')
    allUsers = User.objects.all()
    print(allUsers[0])
    print(request.session['user_name'])
    params = {'users': allUsers, 'user_name': request.session['user_name']}
    return render(request,'user/index.html',params)


def logout(request):
    del request.session['user_name']
    print(request.session['user_name'])
    return render(request,'user/index.html')