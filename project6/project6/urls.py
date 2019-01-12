"""project6 URL Configuration

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
from django.urls import path
from django.conf.urls import url
from django. contrib import admin
from app6.views import GetInput,PostInput,Welcome,Add
urlpatterns=[url(r'^admin/',admin.site.urls),url(r'^$',Welcome.as_view()),url(r'^getinput$',GetInput.as_view(),name='getinput'),url(r'^postinput$',PostInput.as_view(),name='postinput'),url(r'^add$',Add.as_view(),name='add'),]
