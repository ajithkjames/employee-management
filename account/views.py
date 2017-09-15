# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from account.models import User, Skill ,Team, Project, Task
from account.serializers import UserSerializer, SkillSerializer, TeamSerializer, ProjectSerializer, TaskSerializer
from account.permissions import UserPermission, TeamPermission, ProjectPermission, TaskPermission

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):

	serializer_class = TaskSerializer
	queryset = Task.objects.all()
	permission_classes = (TaskPermission,)


class SkillViewSet(viewsets.ModelViewSet):

	serializer_class = SkillSerializer
	queryset = Skill.objects.all()


class UserViewSet(viewsets.ModelViewSet):

	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = (UserPermission,)

class TeamViewSet(viewsets.ModelViewSet):

	serializer_class = TeamSerializer
	queryset = Team.objects.all()
	permission_classes = (TeamPermission,)


class ProjectViewSet(viewsets.ModelViewSet):

	serializer_class = ProjectSerializer
	queryset = Project.objects.all()
	permission_classes = (ProjectPermission,)


class EmployeeTasks(generics.ListAPIView):
	
	serializer_class = TaskSerializer

	def get_queryset(self):
	    return Task.objects.filter(assignee=self.request.user)
