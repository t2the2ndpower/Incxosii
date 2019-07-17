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

    def get_absolute_url(self):
        return f"/target/detail/{self.id}/"


@deconstructible
class Target_Assignment(models.Model):
    related_targetID = models.ForeignKey(Target, on_delete=models.CASCADE)   
    target_assignmentID = models.IntegerField(auto_created=True, unique=True)    
    assignment_name = models.CharField(max_length=80, blank=False)
    assignment_number = models.IntegerField(auto_created=True)
    assignment_description = models.CharField(max_length=10000, blank=False)
    assignment_due_date = models.DateField()
    assignment_created_date = models.DateField(auto_now_add=True)
    assignment_created_by = models.ForeignKey('auth.User', related_name='target_Assignment', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/target_assignment/details{self.id}/"


    