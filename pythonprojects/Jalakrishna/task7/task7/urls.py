from django.conf.urls import url
from django.contrib import admin
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
  url(r'^admin/', admin.site.urls),
  url(r'^signup1',signup1),
  url(r'^resetpassword',resetpassword),
  url(r'^login',login),
  url(r'^password1', password1),
  url(r'^searching',searching),
  url(r'^details',details),
  url(r'^contacts',contacts),
  url(r'^filter',filter_data),
  url(r'^massmail',massmail),

  url(r'^updateprofile',updateprofile),

  url(r'^',home),
  # url(r'^loginform',loginform),

  # url(r'^register',register),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
