from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from hrmanager.models import *
from django.urls import reverse
from django.conf import settings
import os
from django.core import serializers
import json
from django.db.models import Q
# Create your views here.

def index(request):
    username = request.session.get('username', default = '未登录')
    return render(request, 'index.html', {"username":username})

def login(request):
    return render(request, 'page/userInfo/login.html')

def main2(request):
    return render(request, 'page/main2.html')

def personInfo(request):
    employeeid = request.session.get('employeeId')
    employee_info = employeeInfo.objects.get(employeeId=employeeid)
    empid = employee_info.employeeId
    empName = employee_info.employeeName
    empAge = int(employee_info.age)
    empPhone = lambda : '111111' if employee_info.phoneNumber is None else employee_info.phoneNumber
    empEmail = lambda :'111111@qq.com' if employee_info.email is None else employee_info.email
    empJobName = lambda : '无' if employee_info.jobNameId is None else employee_info.jobNameId
    context = {"id":empid, "age":empAge, "name":empName, "phone":empPhone, "email":empEmail, "jobName":empJobName}
    return render(request, 'page/personInfo/personInfo.html', context)

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

def payReport(request):
    return render(request, 'page/payment/payReport.html')

def payRecord(request):
    return render(request, 'page/payment/payRecord.html')

def attendReport(request):
    return render(request, 'page/attendCheck/attendReport.html')

def addressList(request):
    employeeContact = employeeInfo.objects.all()
    contactList = []
    imageBase = 80
    for item in employeeContact:
        itemDict = {}
        itemDict['employeeName'] = item.employeeName
        itemDict['phoneNumber'] = item.phoneNumber
        itemDict['email'] = item.email
        itemDict['imageName'] = imageBase
        imageBase = imageBase + 1
        contactList.append(itemDict)
    contaxt = {"code": 200, "data": contactList}
    return render(request, 'page/userInfo/addressList.html', contaxt)

#登录操作
def login_handle(request):
    dict = request.POST
    uid = dict.get('userid')
    pwd = dict.get("password")
    employeeinfo = employeeInfo.objects.get(employeeId = uid)
    if employeeinfo.password == pwd:
        request.session['username'] = employeeinfo.employeeName
        request.session['employeeId'] = employeeinfo.employeeId
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

#出勤记录统计
def attendRecordCount(request):
    abnormalData = []
    currentUserId = request.session.get('employeeId')
    attendNormal = attendRecord.objects.filter(attendanceStatusId=1, employeeId=currentUserId)
    attendAbnormal = attendRecord.objects.filter(~Q(attendanceStatusId=1), employeeId=currentUserId)
    for item in attendAbnormal:
        itemDict = {}
        itemDict['abnormalTime'] = item.attendEndTime.strftime("%Y-%m-%d")
        itemDict['abnormalReason'] = item.attendanceStatusId.attendStatus
        abnormalData.append(itemDict)
    context = {"attendNormal": attendNormal.count(), "attendAbnormal": attendAbnormal.count(), "abnormalData":abnormalData }
    return JsonResponse(context)

#个人信息保存
def personSave(request):
    dict = request.POST
    email = dict.get('email')
    #age = lambda: 0 if dict.get('age') is None else int(dict.get('age'))
    age = int(dict.get('age'))
    phone = dict.get("phone")
    employeeId = int(request.session.get('employeeId'))
    employeeInfo.objects.filter(employeeId=employeeId).update(email=email, age=age, phoneNumber=phone)
    return redirect(reverse('main:personInfo'))

def changePwd(request):
    newPwd = request.POST.get('newPwd')
    employeeId = int(request.session.get('employeeId'))
    employeeInfo.objects.filter(employeeId=employeeId).update(password=newPwd)
    return redirect('/hrmanager/page/changePass/')

#考勤记录查询
def attend_handle(request):
    attendStatusid = request.GET.get('attendStatus')
    attendData = []
    employeeId = int(request.session.get('employeeId'))
    if attendStatusid:
        attendInfo = attendRecord.objects.filter(employeeId=employeeId).filter(attendanceStatusId=attendStatusid)
    else:
        attendInfo = attendRecord.objects.filter(employeeId=employeeId)
    for item in attendInfo:
        itemData = {}
        itemData['attendanceId'] = item.attendanceId
        itemData['employeeName'] = item.employeeId.employeeName
        itemData['attendStartTime'] = item.attendStartTime.strftime("%Y-%m-%d %H:%M:%S") if item.attendStartTime is not None else None
        itemData['attendEndTime'] = item.attendEndTime.strftime("%Y-%m-%d %H:%M:%S") if item.attendEndTime is not None else None
        itemData['attendStatus'] = item.attendanceStatusId.attendStatus
        attendData.append(itemData)

    context = {"code":0,"msg":"", "count":attendInfo.count(),"data":attendData}

    return JsonResponse(context)

#请假审批

def leave_handle(request):
    employeeId = int(request.session.get('employeeId'))
    paramDict = request.POST
    leaveRange = str(paramDict['leaveRange'])
    leaveDays = int(paramDict['leaveDays'] if paramDict.get('leaveDays') is not None else 1)
    leaveReason = str(paramDict['leaveReason'])
    leaveInfoSave = leaveInfo(employeeId_id=employeeId, leaveReason=leaveReason, leaveTime=leaveRange, leaveTotalDays=leaveDays)
    leaveInfoSave.save()
    return redirect('/hrmanager/page/askForLeave/')

#请假记录查询
def leaveCheck_handle(request):
    leavestatus = request.GET.get('leavestatus')
    employeeId = int(request.session.get('employeeId'))
    leaveList = []
    if leavestatus:
        leaveInfoData = leaveInfo.objects.filter(employeeId=employeeId).filter(leaveStatus1_id=leavestatus)
    else:
        leaveInfoData = leaveInfo.objects.filter(employeeId=employeeId)
    for item in leaveInfoData:
        itemDict = {}
        curStatus = get_curStatus(item.leaveStatus1.confirmInfoId)
        itemDict['employeeName'] = item.employeeId.employeeName
        itemDict['leaveInfoId'] = item.leaveInfoId
        itemDict['leaveTime'] = item.leaveTime
        itemDict['createTime'] = item.createTime.strftime("%Y-%m-%d %H:%M:%S") if item.createTime is not None else None
        itemDict['leaveStatus'] = curStatus
        itemDict['leaveDays'] = item.leaveTotalDays
        itemDict['leaveReason'] = item.leaveReason
        leaveList.append(itemDict)

    context = {"code": 0, "msg": "", "count": leaveInfoData.count(), "data": leaveList}
    return JsonResponse(context)
# 获取当前审批状态
def get_curStatus(item):
    if item == 1:
        return "未审批"
    elif item == 2:
        return "直接主管审批完成"
    elif item == 3:
        return "部门经理审批完成"

def get_payment(request):
    paymentList = []
    employeeid = request.session.get('employeeId')
    payment_info = paymentInfo.objects.filter(employeeId=employeeid)
    for item in payment_info:
        itemDict = {}
        itemDict['paymentId'] = item.paymentInfoId
        itemDict['employeeName'] = item.employeeId.employeeName
        itemDict['attendResult'] = item.attendRecordInfo
        itemDict['payment'] = item.payment
        itemDict['createTime'] = item.createTime.strftime("%Y-%m-%d %H:%M:%S") if item.createTime is not None else None
        paymentList.append(itemDict)
    context={"code": 0, "msg": "", "count": payment_info.count(), "data": paymentList}
    return JsonResponse(context)

#获取工资天数
def get_paycount(request):
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute('''
    select employeeId_id as id, count(1) as totalDays,employeeinfo.employeeName,
(select count(*) from attendrecord where employeeId_id=id and attendanceStatusId_id=1)as normalDays,
(select count(*) from attendrecord where employeeId_id=id and attendanceStatusId_id=2)as lessDays,
(select count(*) from attendrecord where employeeId_id=id and attendanceStatusId_id=2)as abnormalDays,
(select count(*) from attendrecord where employeeId_id=id and attendanceStatusId_id=2)as leaveDays,
(select count(*) from attendrecord where employeeId_id=id and attendanceStatusId_id=2)as absentDays,
(select count(*) from attendrecord where employeeId_id=id and attendanceStatusId_id=2)as workmoreDays
from attendrecord INNER JOIN employeeinfo on attendrecord.employeeId_id=employeeinfo.employeeId GROUP BY employeeId_id 
    ''')
    payCount = cursor.fetchall()
    zippayCount = list(zip(payCount[0], payCount[1], payCount[2]))
    countList = [str(sum(zippayCount[3])),str(sum(zippayCount[4])),str(sum(zippayCount[5]))
                 ,str(sum(zippayCount[6])),str(sum(zippayCount[7])),str(sum(zippayCount[8]))]
    countList = '|'.join(countList)
    cursor.close()
    payList = []
    for item in payCount:
        itemDict = {}
        itemDict["employeeName"] = item[2]
        itemDict["paytotalDays"] = item[1]
        itemDict["normalDays"] = item[3]
        itemDict["lessDays"] = item[4]
        itemDict["abnormalDays"] = item[5]
        itemDict["leaveDays"] = item[6]
        itemDict["absentDays"] = item[7]
        itemDict["workmoreDays"] = item[8]
        itemDict["normalRate"] = str(item[3]/item[1]*100)+'%'
        payList.append(itemDict)
        context = {"code": 0, "msg": "", "count": len(payList), "data": payList,"countList":countList  }
    return JsonResponse(context)

#获取所有工资信息
def paymentAll(request):
    paymentData = serializers.serialize('json', paymentInfo.objects.all())
    context = {"code":0, "paymentData":paymentData}
    return JsonResponse(context)



