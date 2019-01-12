from django.conf.urls import url
from . import views 
app_name ='ProductsApp'
urlpatterns =[url(r'^$',views.ProductInputView.as_view(),name ='input'),url(r'^link$',views.ProductTemplate.as_view(),name='link'),url(r'^display$',views.ProductListView.as_view(),name='display')]
