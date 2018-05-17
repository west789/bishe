from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

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
    return render(request, 'page/404.html')

def systemParameter(request):
    return render(request, 'page/systemParameter/systemParameter.html')