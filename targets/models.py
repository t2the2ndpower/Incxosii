from __future__ import unicode_literals
from django.db import models
from django.utils.deconstruct import deconstructible

# Create your models here.

@deconstructible
class Target(models.Model):
    targetID = models.IntegerField(auto_created=True, unique=True)
    target_title = models.CharField(max_length=80, blank=False)
    target_description = models.CharField(max_length=10000, blank=False)
    target_ownerID = models.ForeignKey('auth.User', related_name='Target', on_delete=models.CASCADE)
    target_created_date = models.DateField(auto_now_add=True)
    target_image = models.ImageField(upload_to='uploads')

    def get_absolute_url(self):
        return f"/target/detail/{self.id}/"


@deconstructible
class Target_Assignment(models.Model):
    related_targetID = models.ForeignKey(Target, related_name='assignments', on_delete=models.CASCADE)   
    target_assignmentID = models.IntegerField(auto_created=True, unique=True)    
    assignment_name = models.CharField(max_length=80, blank=False)
    assignment_number = models.IntegerField(auto_created=True)
    assignment_description = models.CharField(max_length=10000, blank=False)
    #assignment_duration = models.DurationField(default=24)
    assignment_due_date = models.DateField()
    assignment_created_date = models.DateField(auto_now_add=True)
    assignment_created_by = models.ForeignKey('auth.User', related_name='Target_Assignment', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/target_assignment/details{self.id}/"


@deconstructible
class rTarget_Assigned_To(models.Model):
    related_targetID = models.ForeignKey(Target, on_delete=models.CASCADE)   
    target_completion_date = models.DateField(blank=True)
    target_signup_date = models.DateField(auto_now_add=True)
    assigned_to_user = models.ForeignKey('auth.User', related_name='rTarget_Assignmed_To', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/r_target_assigned_to/details{self.id}/"    


@deconstructible
class rTarget_Assignments_Relationships(models.Model):
    related_target_assignmentID = models.ForeignKey(Target_Assignment, on_delete=models.CASCADE)   
    assignment_due_date = models.DateField(blank=True)
    assignment_start_date = models.DateField(auto_now_add=True)
    assignment_assigned_to_user = models.ForeignKey('auth.User', related_name='rTarget_Assignments_Relationships', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/r_target_assignments_relationships/details{self.id}/"


@deconstructible
class rAssignment_Activity_Relationships(models.Model):
    rTarget_Assignment_RelationshipID = models.ForeignKey(rTarget_Assignments_Relationships, on_delete=models.CASCADE)
    activity_create_date = models.DateField(auto_now_add=True)
    activity_created_by = models.ForeignKey('auth.User', related_name='rAssignment_Activity_Relationships', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, blank=False)
    activity_description = models.CharField(max_length=10000, blank=False)

    def get_absolute_url(self):
        return f"/r_assignment_activity_relationships/details{self.id}/"
