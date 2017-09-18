from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as restview
from account.views import SkillViewSet, UserViewSet ,TeamViewSet, ProjectViewSet, TaskViewSet, EmployeeTasks


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, 'user_detail')
router.register(r'skill', SkillViewSet, 'skills')
router.register(r'team', TeamViewSet, 'teams')
router.register(r'project', ProjectViewSet, 'projects')
router.register(r'task', TaskViewSet, 'tasks')

urlpatterns = [
	url(r'^employeetasks/$', EmployeeTasks.as_view(), name="emp_tasks-list"),
    url(r'^login/', restview.obtain_auth_token),
]

urlpatterns += router.urls