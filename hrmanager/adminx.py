import xadmin
from .models import *
from xadmin import views



class employeeInfoAdmin(object):
    list_display = ["employeeId", "employeeName", "age" , "phoneNumber",
                    "email", "address", "departmentId", "roleId","jobNameId",  "jobStatus",  ]
    list_per_page = 5  # 每页显示的个数
    show_detail_fields = ["employeeName", "jobStatus"]  # 设置详情标识
    refresh_times = (3, 5)  # 刷新时间
    # list_filter = ("employeeId", "employeeName", "age", "password", "phoneNumber",
    #                 "email", "address", "departmentId__departmentName", "roleId", "jobStatus", )
    ordering = ("employeeId",)
    search_fields = ("address", "departmentId__departmentName",)


    def get_readonly_fields(self):
        """  重新定义此函数，限制普通用户所能修改的字段  """
        if self.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    readonly_fields = ('employeeName',)

# class attendStatusInfoInline():
#     model = attendStatusInfo
#     extra = 2
class attendRecordAdmin(object):
    list_display = ["attendanceId", "employeeId", "attendStartTime", "attendEndTime", "attendanceStatusId" ]
    list_per_page = 5  # 每页显示的个数
    show_detail_fields = ["employeeId", "attendanceStatusId"]  # 设置详情标识
    refresh_times = (3, 5)  # 刷新时间
    ordering = ("attendanceId",)
    list_filter = ("attendanceId", "employeeId__employeeName", "attendStartTime", "attendEndTime", "attendanceStatusId" )
    search_fields = ("employeeId__employeeName",)


class leaveInfoAdmin(object):
    list_display = ["leaveInfoId", "employeeId",  "leaveReason", "leaveTime","leaveTotalDays","leaveStatus1", "createTime" ]
    ordering = ("leaveStatus1",)
    search_fields = ("leaveStatus1__confirmStatus",)
    show_detail_fields = ["leaveStatus1"]  # 设置详情标识
    list_bookmarks = [{
        "title": "未审批",
        "query": {"leaveStatus1__confirmStatus__contains": "未审批"},
        # "query": {"jobNameId__gt": '105'},
        "order": ("leaveInfoId",),
        "cols": ["leaveInfoId", "leaveStatus1"],
    }]


class departmentInfoAdmin(object):
    list_display = ["departmentId", "departmentName", "departmentManager", ]
    ordering = ("departmentId",)
    list_filter = ('departmentName',)


class paymentInfoAdmin(object):
    list_display = ["paymentInfoId", "employeeId", "attendRecordInfo", "payment", "createTime" ]
    ordering = ("paymentInfoId",)
    data_charts = {
        "user_count": {'title': "工资统计", "x-field": "employeeId_id", "y-field": ("payment",),
                       "order": ('employeeId',)},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }

class jobNameInfoAdmin(object):
    list_display = ['jobNameId','jobName']    #显示的字段
    #model_icon = 'fa fa-university'
    list_per_page = 5  #每页显示的个数
    show_detail_fields = ['jobName']    #设置详情标识
    refresh_times = (3, 5)          #刷新时间
    search_fields = ('jobName',)
    ordering = ("jobNameId",)
    list_filter = ('jobName',)
    list_bookmarks = [{
        "title": "工程师",
        "query": {"jobName__contains": '工程师'},
        #"query": {"jobNameId__gt": '105'},
        "order": ("jobNameId",),
        "cols": ["jobNameId", "jobName"],
    }]


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '人事考勤管理系统'     #首页头
    site_footer = '庞绍良'             #首页尾
    menu_style = 'default'           # "accordion"折叠菜单
    # global_search_models = ['V_UserInfo', 'UserDistrict']
    # global_models_icon = {
    #     'V_UserInfo': "glyphicon glyphicon-user", 'UserDistrict': "fa fa-cloud"
    # }  # 设置models的全局图标
xadmin.site.register(employeeInfo, employeeInfoAdmin)
xadmin.site.register(attendRecord, attendRecordAdmin)
xadmin.site.register(leaveInfo, leaveInfoAdmin)
xadmin.site.register(paymentInfo, paymentInfoAdmin)
xadmin.site.register(departmentInfo, departmentInfoAdmin)
xadmin.site.register(jobNameInfo, jobNameInfoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
