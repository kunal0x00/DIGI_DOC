from django.contrib import admin
from django.urls import path
from home import views
#newly added 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name='home'),
]