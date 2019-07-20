from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Target, Target_Assignment, rTarget_Assignments_Relationships, rTarget_Assigned_To, rAssignment_Activity_Relationships

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class TargetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Target
        fields = (
            'targetID',
            'url',
            'target_title',
            'target_description',
            'target_ownerID',
            'target_created_date',
            'target_image'
            )


class TargetAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Target_Assignment
        fields = (
            'target_assignmentID',
            'url',
            'related_targetID',
            'assignment_name',
            'assignment_number',
            'assignment_description',
            'assignment_due_date',
            'assignment_created_date',
            'assignment_created_by'
        )


class rTarget_Assigned_ToSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rTarget_Assigned_To
        fields = (
            'related_targetID',
            'url',
            'assigned_to_user',
            'target_signup_date',
            'target_completion_date'
            )


class rTarget_Assignments_RelationshipsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rTarget_Assignments_Relationships
        fields = (
            'related_target_assignmentID',
            'url',
            'assignment_assigned_to_user',
            'assignment_start_date',
            'assignment_due_date'
            )


class rAssignment_Activity_RelationshipsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rAssignment_Activity_Relationships
        fields = (
            'rTarget_Assignment_RelationshipID',
            'activity_create_date',
            'activity_created_by',
            'activity_type',
            'activity_description'
        )
