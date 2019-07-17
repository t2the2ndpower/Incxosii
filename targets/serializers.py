from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Target, Target_Assignment

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
            'target_created_date'
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
