from __future__ import unicode_literals
from django.contrib import admin


# Change Header Here
admin.site.site_header = 'Welcome to the Inkosi App Admin Area'


# Register your models here.
from targets.models import Target, Target_Assignment


class IncxosiiUserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_cell', 'user_email']


class IncxosiiTargetAdmin(admin.ModelAdmin):
    list_display = ['target_title', 'target_created_date', 'target_ownerID']


class IncxosiiAssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment_name', 'assignment_created_date', 'assignment_due_date', 'related_targetID']


# class InkosiTypeAdmin(admin.ModelAdmin):
#     list_display = ['student_activity_type', 'student_activity_typeID']


# class InkosiStuActAdmin(admin.ModelAdmin):
#     list_display = ['activity_type', 'activity_details', 'created_date']


# class InkosiStuCourseAsgnAdm(admin.ModelAdmin):
#     list_display = ['student_course_assignmentID', 'isStarted', 'start_date', 'complete_date', 'stu_course_asgn_created_date']


# admin.site.register(IncxosiiUserAdmin)
admin.site.register(Target, IncxosiiTargetAdmin)
admin.site.register(Target_Assignment, IncxosiiAssignmentAdmin)


