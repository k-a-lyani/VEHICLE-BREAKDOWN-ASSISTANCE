"""OnRoad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('commonuser', views.commonuser, name='commonuser'),
    path('commonlogin', views.commonlogin, name='commonlogin'),
    path('commonmechanic', views.commonmechanic, name='commonmechanic'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('adminapproveuser', views.adminapproveuser, name='adminapproveuser'),
    path('adminmechanic', views.adminmechanic, name='adminmechanic'),
    path('adminuser', views.adminuser, name='adminuser'),
    path('mechanichome', views.mechanichome, name='mechanichome'),
    path('userhome', views.userhome, name='userhome'),
    path('userworkrequest', views.userworkrequest, name='userworkrequest'),
    path('mechanicworkrequest', views.mechanicworkrequest, name='mechanicworkrequest'),
    path('userwork', views.userwork, name='userwork'),
    path('userchooseworker', views.userchooseworker, name='userchooseworker'),
    path('userbookworker', views.userbookworker, name='userbookworker'),
    path('mechanicapprovework', views.mechanicapprovework, name='mechanicapprovework'),
    path('mechanicwork', views.mechanicwork, name='mechanicwork'),
    path('mechanicallwork', views.mechanicallwork, name='mechanicallwork'),
    path('usercompletedwork', views.usercompletedwork, name='userwork'),
    path('userallfeedback', views.userallfeedback, name='userallfeedback'),
    path('userfeedback', views.userfeedback, name='userfeedback'),
    path('mechanicfeedback', views.mechanicfeedback, name='mechanicfeedback'),
    path('adminfeedback', views.adminfeedback, name='adminfeedback'),
]
