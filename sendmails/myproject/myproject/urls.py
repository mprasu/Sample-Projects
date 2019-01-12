"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from myapp.views import welcome,viewArticle,viewArticles,sendSimpleEmail,sendMassEmail,sendAdminsEmail,sendManagersEmail,sendEmailWithAttach,login
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),url(r'^hello/$',welcome),url(r'^article/(\d{2})/$',viewArticle,name='abc'),url(r'^articles/(\d{2})/(\d{4})/',viewArticles,name='articles'),url(r'^smail/$',sendSimpleEmail),url(r'^massEmail/$',sendMassEmail),url(r'^admn/$',sendAdminsEmail),url(r'^mangr/$',sendManagersEmail),url(r'^compose/',sendEmailWithAttach),url(r'^connection/$',login)]




#url(r'^massEmail/(?P<emailto1>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<emailto2>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',sendMassEmail)
#(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$
