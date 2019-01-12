from django.conf.urls import url
from django.urls import path 
from genericviews import views
#app_name = 'genericviews' 
urlpatterns = [
 
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
        url(r'^makeentry$', views.MakeEntry.as_view(), name='makeentry'),
	url(r'^/(?P<pk>[0-9]+)/delete/$',views.DeleteView.as_view(),name='item-delete'),
]