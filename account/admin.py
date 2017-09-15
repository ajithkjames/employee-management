# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User, Skill, Team, Project, Task

class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('age',)}),
    )

admin.site.register(User, MyUserAdmin)
admin.site.register(Skill)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Task)
