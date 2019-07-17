# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Api imports
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from targets.serializers import UserSerializer, GroupSerializer, TargetsSerializer, TargetAssignmentSerializer
# model imports
from .models import Target, Target_Assignment
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

