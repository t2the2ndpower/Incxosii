from __future__ import unicode_literals
from django.contrib import admin


# Change Header Here
admin.site.site_header = 'Welcome to the Inkosi App Admin Area'


# Register your models here.
from targets.models import Target, Target_Assignment, rTarget_Assigned_To, rTarget_Assignments_Relationships, rAssignment_Activity_Relationships


class IncxosiiUserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_cell', 'user_email']


class IncxosiiTargetAdmin(admin.ModelAdmin):
    list_display = ['target_title', 'target_created_date', 'target_ownerID']


class IncxosiiAssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment_name', 'assignment_created_date', 'assignment_due_date', 'related_targetID']


class IncxosiirTarget_Assignments_RelationshipsAdmin(admin.ModelAdmin):
    list_display = ['recordID','related_target_assignmentID', 'assignment_assigned_to_user', 'assignment_start_date', 'assignment_due_date']


class IncxosiirTarget_Assigned_ToAdmin(admin.ModelAdmin):
    list_display = ['recordID','related_targetID', 'assigned_to_user', 'target_signup_date', 'target_completion_date']


class IncxosiirAssignment_Activity_RelationshipsAdmin(admin.ModelAdmin):
    list_display = ['recordID', 'rTarget_Assignment_RelationshipID', 'activity_create_date', 'activity_created_by', 'activity_type', 'activity_description']


admin.site.register(Target, IncxosiiTargetAdmin)
admin.site.register(Target_Assignment, IncxosiiAssignmentAdmin)
admin.site.register(rTarget_Assigned_To, IncxosiirTarget_Assigned_ToAdmin)
admin.site.register(rTarget_Assignments_Relationships, IncxosiirTarget_Assignments_RelationshipsAdmin)
admin.site.register(rAssignment_Activity_Relationships, IncxosiirAssignment_Activity_RelationshipsAdmin)


