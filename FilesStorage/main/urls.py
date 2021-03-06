from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index,name='home'),
    path('upload',views.upload,name='upload'),
    path('filter',views.filter,name='filter'),
    path('notime',views.notime,name='notime')
]

if settings.DEBUG :
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
