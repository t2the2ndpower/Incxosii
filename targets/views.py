# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Api imports
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from targets.serializers import UserSerializer, GroupSerializer, TargetsSerializer, TargetAssignmentSerializer, rTarget_Assignments_RelationshipsSerializer, rTarget_Assigned_ToSerializer, rAssignment_Activity_RelationshipsSerializer

# model imports
from targets.models import Target, Target_Assignment, rTarget_Assigned_To, rTarget_Assignments_Relationships, rAssignment_Activity_Relationships
# # from django.http import HttpResponse

# Forms import
from .forms import Create_Target_Form, Create_Assignment_Form
from django.http import HttpResponseRedirect

# Email imports
from django.core.mail import send_mail

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


def target_detail_view(request, target_id):
    # print('target_id', request.GET.get('target_id'))
    obj = Target.objects.get(id=target_id)
    # objs = Target_Assignment.objects.get(ids=target_assignment_id)
    #queryset = Target_Assignment.objects.all()
    queryset = Target_Assignment.objects.filter(related_targetID = target_id)



    RequestContext = {
        'object': obj,
        #'objects': objs,
        'objects_list': queryset,
    }
    print(queryset)
    return render(request, "target_detail.html", RequestContext)


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


# Django Form Views

@login_required(login_url='/accounts/login/')
def Create_Target_View(request):
    form = Create_Target_Form(request.POST or None)
    if form.is_valid():
        form.save()
        #form = Create_Target_Form()
        return HttpResponseRedirect('/target_assignment/create')
        
    context = {
        'form': form
    }
    return render(request, 'create_target.html', context)

@login_required(login_url='/accounts/login/')
def Create_Assignments_View(request):
    form = Create_Assignment_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Create_Assignment_Form()
        
    context = {
        'form': form
    }
    return render(request, 'create_assignments.html', context)



# SEND EMAIL VIEWS

# @login_required(login_url='/accounts/login/')
def Send_Assign_Target_View(request):

    send_mail(
        'You have just been assigned a Target to shoot for!',
        'Technoladie just assigned a Target to you, please login to the Incxosii Mastery App to manage your Target based assignments!',
        'idsg3.test@gmail.com',
        ['technoladie@gmail.com'],
        fail_silently=False
         )
    return render(request, 'send/assign_target_comm.html')



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