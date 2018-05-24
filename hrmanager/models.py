from django.db import models
from datetime import datetime
# Create your models here.

#员工信息表
class employeeInfo(models.Model):
    employeeId = models.AutoField(primary_key=True, verbose_name="员工编号")
    employeeName = models.CharField(max_length=200, verbose_name="员工姓名")
    age = models.CharField(max_length=5, null=True, blank=True, verbose_name="年龄")
    password = models.CharField(max_length=20, verbose_name="密码")
    phoneNumber = models.CharField(max_length=11, null=True, blank=True, verbose_name="联系方式")
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name="邮箱")
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    departmentId = models.ForeignKey("departmentInfo", on_delete=models.CASCADE, verbose_name="部门编号")
    roleId = models.ForeignKey("roleInfo", on_delete=models.CASCADE, verbose_name="角色编号")
    jobStatus = models.CharField(max_length=20, null=True, verbose_name="目前状态")
    jobNameId = models.ForeignKey("jobNameInfo", on_delete=models.CASCADE, verbose_name="职位编号")
    def __str__(self):
        return self.employeeName
    class Meta():
        db_table = 'employeeinfo'
        verbose_name = "员工信息表"
        verbose_name_plural = verbose_name
#角色信息表
class roleInfo(models.Model):
    roleId = models.AutoField(primary_key=True, verbose_name="角色编号")
    roleName = models.CharField(max_length=200, verbose_name="角色名称")
    def __str__(self):
        return self.roleName
    class Meta():
        db_table = 'roleinfo'
        verbose_name = '角色信息表'
        verbose_name_plural = verbose_name

#部门信息表
class departmentInfo(models.Model):
    departmentId = models.AutoField(primary_key=True, verbose_name="部门编号")
    departmentName = models.CharField(max_length=200, verbose_name="部门名称")
    departmentManager = models.CharField(max_length=200, verbose_name="部门经理")
    def __str__(self):
        return self.departmentName
    class Meta():
        db_table = 'departmentinfo'
        verbose_name = '部门信息表'
        verbose_name_plural = verbose_name

#职位信息表
class jobNameInfo(models.Model):
    jobNameId = models.AutoField(primary_key=True, verbose_name='职位编号')
    jobName = models.CharField(max_length=200, verbose_name='职位名称')
    def __str__(self):
        return self.jobName
    class Meta():
        db_table = 'jobnameinfo'
        verbose_name = '职位信息表'
        verbose_name_plural = verbose_name


#出勤状态信息表
class attendStatusInfo(models.Model):
    attendStatusId = models.AutoField(primary_key=True, verbose_name="出勤状态编号")
    attendStatus = models.CharField(max_length=200, verbose_name="出勤状态")
    def __str__(self):
        return self.attendStatus
    class Meta():
        db_table = 'attendstatusinfo'
        verbose_name = '出勤状态表'
        verbose_name_plural = verbose_name

#考勤记录表
class attendRecord(models.Model):
    attendanceId = models.AutoField(primary_key=True, verbose_name="考勤记录编号")
    employeeId = models.ForeignKey("employeeInfo", on_delete=models.CASCADE, verbose_name="员工编号")
    attendStartTime = models.DateTimeField(null=True, blank=True, verbose_name="签到时间")
    attendEndTime = models.DateTimeField(null=True, blank=True, verbose_name="签出时间")
    attendanceStatusId = models.ForeignKey("attendStatusInfo", on_delete=models.CASCADE, verbose_name="出勤状态")
    def __str__(self):
        return str(self.attendanceId)
    class Meta():
        db_table = 'attendrecord'
        verbose_name = '考勤记录表'
        verbose_name_plural = verbose_name

#请假记录表
class leaveInfo(models.Model):
    leaveInfoId = models.AutoField(primary_key=True, verbose_name="请假编号")
    employeeId = models.ForeignKey("employeeInfo", on_delete=models.CASCADE, verbose_name="员工编号")
    #departmentId = models.ForeignKey('departmentInfo', on_delete=models.CASCADE, verbose_name="部门编号")
    leaveStatus = models.IntegerField(default=0, verbose_name="审批状态")
    leaveReason = models.TextField(verbose_name="请假原因")
    leaveTotalDays = models.IntegerField(default=1, verbose_name="请假天数")
    leaveTime = models.CharField(max_length=200, verbose_name="请假时间")
    createTime = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    def __str__(self):
        return str(self.leaveInfoId)
    class Meta():
        db_table = 'leaveinfo'
        verbose_name = '请假记录表'
        verbose_name_plural = verbose_name

#工资信息表
class paymentInfo(models.Model):
    paymentInfoId = models.AutoField(primary_key=True,verbose_name="工资记录编号")
    employeeId = models.ForeignKey("employeeInfo", on_delete=models.CASCADE, verbose_name="员工编号")
    attendRecordInfo = models.CharField(max_length=200, verbose_name="出勤记录信息")
    payment = models.CharField(max_length=200, verbose_name="发放工资")
    createTime = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    def __str__(self):
        return str(self.paymentInfoId)
    class Meta():
        db_table = 'paymentinfo'
        verbose_name = '工资记录表'
        verbose_name_plural = verbose_name