from django.shortcuts import render, redirect
from django.http import HttpResponse
from hrmanager.models import *
from django.urls import reverse
from django.conf import settings
import os
# Create your views here.

def index(request):
    username = request.session.get('username', default = '未登录')
    return render(request, 'index.html', {"username":username})

def login(request):
    return render(request, 'page/userInfo/login.html')

def main2(request):
    return render(request, 'page/main2.html')

def personInfo(request):
    return render(request, 'page/personInfo/personInfo.html')

def changePass(request):
    return render(request, 'page/userInfo/changePass.html')

def attendCheck(request):
    return render(request, 'page/attendCheck/attendCheck.html')

def askForLeave(request):
    return render(request, 'page/askForLeave/askForLeave.html')

def abnormalOfAttend(request):
    return render(request, 'page/abnormalOfAttend/abnormalOfAttend.html')

def leaveForCheck(request):
    return render(request, 'page/leaveForCheck/leaveForCheck.html')

def linksList(request):
    return render(request, 'page/links/linksList.html')

def newsList(request):
    return render(request, 'page/news/newsList.html')

def error(request):
    return render(request, '404.html')

def systemParameter(request):
    return render(request, 'page/systemParameter/systemParameter.html')

#登录操作
def login_handle(request):
    dict = request.POST
    uid = dict.get('userid')
    pwd = dict.get("password")
    employeeinfo = employeeInfo.objects.get(employeeId = uid)
    if employeeinfo.password == pwd:
        request.session['username'] = employeeinfo.employeeName
        return redirect(reverse('main:index'))
    else:
        return render(request, 'page/userInfo/login.html')

def logout(request):
    request.session.flush()
    return render(request, 'page/userInfo/login.html')

def uploadPic(request):
    if request.method == 'POST':
        f1 = request.FILES['pic']
        fname = os.path.join(settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb') as f:
            for c in f1.chunks():
                f.write(c)
        return HttpResponse(fname)
    else:
        return HttpResponse('error')
