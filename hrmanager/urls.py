from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout),
    path('page/main2/', views.main2),
    path('page/personInfo/', views.personInfo, name='personInfo'),
    path('page/changePass/', views.changePass, name='changePass'),
    path('page/attendCheck/', views.attendCheck),
    path('page/askForLeave/', views.askForLeave),
    path('page/abnormalOfAttend/', views.abnormalOfAttend),
    path('page/leaveForCheck/', views.leaveForCheck),
    path('page/newsList/', views.newsList),
    path('page/linksList/', views.linksList),
    path('error/', views.error),
    path('page/systemParameter/', views.systemParameter),
    path('page/payReport/', views.payReport),
    path('page/payRecord/', views.payRecord),
    path('page/attendReport/', views.attendReport),
    path('page/addressList/', views.addressList),

    path('login_handle/', views.login_handle),
    path('uploadpic/', views.uploadPic),

    path("attendRecordCount/", views.attendRecordCount),  #首页出勤数统计
    path("personSave/", views.personSave), #个人信息保存
    path('changePwd/', views.changePwd),  #更改密码
    path('attend_handle/', views.attend_handle),  #考勤记录查询
    path('leave_handle/', views.leave_handle),   #请假审批
    path('leaveCheck_handle/', views.leaveCheck_handle), #请假查询
    path('get_payment/', views.get_payment),  #获取工资信息
    path('get_paycount/', views.get_paycount),  #获取出勤总数
    path('paymentAll/', views.paymentAll)   #获取所有的工资信息
]
app_name = 'hrmanager'