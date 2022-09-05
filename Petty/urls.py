from django.urls import path, re_path
from Petty import views

urlpatterns = [

    re_path(r'^$', views.home, name='home')

]