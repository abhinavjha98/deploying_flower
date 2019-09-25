from django.conf.urls import url
from django.urls import path,re_path
from hello_world import views

urlpatterns = [
	re_path('$',views.index,name = 'index'),
]