from django.db import models
from datetime import datetime
# Create your models here.

#员工信息表
class employeeInfo(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=200)
    age = models.CharField(max_length=2, null=True, blank=True)
    password = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    departmentId = models.ForeignKey("departmentInfo", on_delete=models.CASCADE)
    roleId = models.ForeignKey("roleInfo", on_delete=models.CASCADE)
    jobStatus = models.CharField(max_length=20)
    jobNameId = models.ForeignKey("jobNameInfo", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.employeeId) + self.employeeName
    class Meta():
        db_table = 'employeeinfo'
#角色信息表
class roleInfo(models.Model):
    roleId = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=200)
    def __str__(self):
        return str(self.roleId) + " " + self.roleName
    class Meta():
        db_table = 'roleinfo'

#部门信息表
class departmentInfo(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=200)
    departmentManager = models.CharField(max_length=200)
    def __str__(self):
        return str(self.departmentId) + " " + self.departmentName+ " " + self.departmentManager
    class Meta():
        db_table = 'departmentinfo'

#职位信息表
class jobNameInfo(models.Model):
    jobNameId = models.AutoField(primary_key=True)
    jobName = models.CharField(max_length=200)
    def __str__(self):
        return str(self.jobNameId) + self.jobName
    class Meta():
        db_table = 'jobnameinfo'

#工作状态信息表
class attendStatusInfo(models.Model):
    attendStatusId = models.AutoField(primary_key=True)
    attendStatus = models.CharField(max_length=200)
    def __str__(self):
        return str(self.attendStatusId) + " " + self.attendStatus
    class Meta():
        db_table = 'attendstatusinfo'

#考勤记录表
class attendRecord(models.Model):
    attendanceId = models.AutoField(primary_key=True)
    employeeId = models.ForeignKey("employeeInfo", on_delete=models.CASCADE)
    attendStartTime = models.DateTimeField(null=True, blank=True)
    attendEndTime = models.DateTimeField(null=True, blank=True)
    attendanceStatusId = models.ForeignKey("attendStatusInfo", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.attendanceId)
    class Meta():
        db_table = 'attendrecord'

#请假记录表
class leaveInfo(models.Model):
    leaveInfoId = models.AutoField(primary_key=True)
    employeeId = models.ForeignKey("employeeInfo", on_delete=models.CASCADE)
    departmentId = models.ForeignKey('departmentInfo', on_delete=models.CASCADE)
    leaveReason = models.TextField()
    leaveTime = models.DateTimeField()
    createTime = models.DateTimeField()
    def __str__(self):
        return str(self.leaveInfoId)
    class Meta():
        db_table = 'leaveinfo'

#工资信息表
class paymentInfo(models.Model):
    paymentInfoId = models.AutoField(primary_key=True)
    employeeId = models.ForeignKey("employeeInfo", on_delete=models.CASCADE)
    attendRecordInfo = models.CharField(max_length=200)
    payment = models.CharField(max_length=200)
    createTime = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.paymentInfoId)
    class Meta():
        db_table = 'paymentinfo'