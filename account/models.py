# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    empid = models.CharField(max_length=255, blank=True, null=True, unique=True)
    teamlead = models.BooleanField(default=False, verbose_name="Team Lead")


class Skill(models.Model):
    name = models.CharField(max_length=50)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return u'%s - %s' % (self.name, self.user)


class Team(models.Model):
	name = models.CharField(max_length=50)
	lead= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	members = models.ManyToManyField(User, related_name='team_members' )

	def __str__(self):
		return u'%s - %s' % (self.name, self.lead)


class Project(models.Model):
	name = models.CharField(max_length=50)
	team= models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
	members= models.ManyToManyField(User)

	def __str__(self):
		return u'%s - %s' % (self.team.name, self.name)


class Task(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	assigner = models.ForeignKey(User, null=True, blank=True,  related_name='assigner')
	assignee = models.ForeignKey(User, null=True, blank=True)
	project = models.ForeignKey(Project, null=True, blank=True)

	def __str__(self):
		return u'%s - %s' % (self.project, self.title)