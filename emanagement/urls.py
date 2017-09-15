from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('account.urls', namespace='account')),
]
