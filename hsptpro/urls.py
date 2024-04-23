"""
URL configuration for hsptpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from hsptlapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='page1'),
    path('ab',views.aboutpg,name='page2'),
    path('dp',views.dep,name='page3'),
    path('ds',views.doctor,name='page4'),
    path('ss',views.bookingfn,name='page5'),
    path('sd',views.newpg,name='page6')
]
