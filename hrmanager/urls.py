from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login),
    path('logout/', views.logout),
    path('page/main2/', views.main2),
    path('page/personInfo/', views.personInfo),
    path('page/changePass/', views.changePass),
    path('page/attendCheck/', views.attendCheck),
    path('page/askForLeave/', views.askForLeave),
    path('page/abnormalOfAttend/', views.abnormalOfAttend),
    path('page/leaveForCheck/', views.leaveForCheck),
    path('page/newsList/', views.newsList),
    path('page/linksList/', views.linksList),
    path('page/error/', views.error),
    path('page/systemParameter/', views.systemParameter),

    path('login_handle/', views.login_handle),
    path('uploadpic/', views.uploadPic)
]
app_name = 'hrmanager'