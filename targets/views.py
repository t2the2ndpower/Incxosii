# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Api imports
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from targets.serializers import UserSerializer, GroupSerializer, TargetsSerializer, TargetAssignmentSerializer, rTarget_Assignments_RelationshipsSerializer, rTarget_Assigned_ToSerializer, rAssignment_Activity_RelationshipsSerializer
# model imports
from targets.models import Target, Target_Assignment, rTarget_Assigned_To, rTarget_Assignments_Relationships, rAssignment_Activity_Relationships
# # from django.http import HttpResponse
# from .forms import target_form, assignment_form

# Create your views here.

def index_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "index.html", {})


def target_view(request, *args, **kwargs):
    queryset = Target.objects.all()

    context = {
        'object_list': queryset,
    }

    return render(request, "targets.html", context)


def target_detail_view(request, *args, **kwargs):
    obj = Target.objects.get(id=1)

    context = {
        'object': obj,
    }

    return render(request, "target_detail.html", context)


def target_assignment_view(request, *args, **kwargs):
    # obj = Course.objects.get(id=id)
    queryset = Target_Assignment.objects.all()

    context = {
        # 'object': obj,
        'object_list': queryset,
    }

    return render(request, "target_assignments_list.html", context)


def target_assignment_detail_view(request, *args, **kwargs):
    # obj = Course.objects.get(id=id)
    queryset = Target_Assignment.objects.get(id=1)

    context = {
        # 'object': obj,
        'object_list': queryset,
    }

    return render(request, "target_assignment_detail.html", context)


def rTarget_Assigned_To_view(request, *args, **kwargs):
    # obj = Course.objects.get(id=id)
    queryset = rTarget_Assigned_To.objects.get(id=1)

    context = {
        # 'object': obj,
        'object_list': queryset,
    }

    return render(request, "target_assigned_to.html", context)


def rTarget_Assignments_Relationships_view(request, *args, **kwargs):
    # obj = Course.objects.get(id=id)
    queryset = rTarget_Assignments_Relationships.objects.get(id=1)

    context = {
        # 'object': obj,
        'object_list': queryset,
    }

    return render(request, "target_assignments_relationships.html", context)


def rAssignment_Activity_Relationships_view(request, *args, **kwargs):
    # obj = Course.objects.get(id=id)
    queryset = rAssignment_Activity_Relationships.objects.get(id=1)

    context = {
        # 'object': obj,
        'object_list': queryset,
    }

    return render(request, "rAssignment_Activity_Relationships.html", context)





# API VIEWSETS

class UserViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows users to be viewed or edited.
    # """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows groups to be viewed or edited.
    # """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetsSerializer


class TargetAssignmentViewSet(viewsets.ModelViewSet):
    queryset = Target_Assignment.objects.all()
    serializer_class = TargetAssignmentSerializer


class rTarget_Assigned_To_ViewSet(viewsets.ModelViewSet):
    queryset = rTarget_Assigned_To.objects.all()
    serializer_class = rTarget_Assigned_ToSerializer


class rTarget_Assignments_Relationships_ViewSet(viewsets.ModelViewSet):
    queryset = rTarget_Assignments_Relationships.objects.all()
    serializer_class = rTarget_Assignments_RelationshipsSerializer


class rAssignment_Activity_Relationships_ViewSet(viewsets.ModelViewSet):
     queryset = rAssignment_Activity_Relationships.objects.all()
     serializer_class = rAssignment_Activity_RelationshipsSerializer   