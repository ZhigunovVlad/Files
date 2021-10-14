from . import views
from django.urls import path

urlpatterns = [

    path('', views.index,name='home'),
    path('upload',views.upload,name='upload'),
    path('filter',views.filter,name='filter')

]
