"""incxosii_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Api imports
# from rest_framework import routers
from targets import views

# Template imports
from django.views.generic.base import TemplateView

# Views import
from targets.views import target_view, target_detail_view, target_assignment_view, index_view, target_assignment_detail_view, Create_Target_View, Send_Assign_Target_View, Create_Assignments_View


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', index_view),
    path('incxosii_api/', include('targets.urls')),
    path('targets/', target_view),
    path('target/detail/<int:target_id>/', target_detail_view),
    #path('target/detail/', target_detail_view),
    path('target/detail/assignments', target_assignment_view),
    path('target_assignment/detail/<int:id>/', target_assignment_detail_view),
    path('target/create/', Create_Target_View),
    path('target_assignment/create/', Create_Assignments_View),
    path('target_assigned_to/send', Send_Assign_Target_View),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
