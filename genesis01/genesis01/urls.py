
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('videos', views.videos, name = 'videos'),
    path('lab', views.lab, name = 'lab')
]
