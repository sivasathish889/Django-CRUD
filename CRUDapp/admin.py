from django.contrib import admin
from CRUDapp.models import Student
# Register your models here.
class Student_admin(admin.ModelAdmin):
    stu=["Sno","SrollNo", "Sclass", "Snative"]

admin.site.register(Student,Student_admin)