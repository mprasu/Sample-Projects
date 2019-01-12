from django.conf.urls import url, include
from django.contrib import admin
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  url(r'^admin/', admin.site.urls),
  
  url(r'^signup1',signup1),
  url(r'^location',location),
  url(r'^login',login),
  url(r'^forgetpassword',forgetpassword),
  url(r'^mySettings',mySettings),
  url(r'^changepassword',changepassword),
  url(r'^editprofile',editprofile),
  url(r'^deleteAccount',deleteAccount),
  url(r'^viewdetails',viewdetails),
  url(r'^contact',contact),
  url(r'^filter_data',filter_data),
  url(r'^myevents',myevents),
  url(r'^sendingSMS',sendingSMS),
  url(r'^twiliosms',twiliosms),
  url(r'^media',media),
  #url(r'^gallery',gallery),
  url(r'massmail',massmail),
  url(r'',home),
  
  ]
  # +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

