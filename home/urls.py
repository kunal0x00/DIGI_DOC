from django.contrib import admin
from django.urls import path
from home import views
#newly added 
from django.conf import settings
from django.conf.urls.static import static
from .views import UploadFileView
from . import views
from .views import upload_file, download_encrypted_file,  delete_file, file_list
from .views import dashboard
from django.contrib.auth import views as auth_views
from .views import custom_logout
from .views import file_list

urlpatterns = [
    path("",views.index,name='home'),
    path("about/",views.about,name='about'),
    path("security",views.security,name='security'),
    path("resources",views.resources,name='resources'),
    path("contact",views.contact,name='contact'),
    path("signup/", views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('upload/', upload_file, name='upload_file'),
    path('dashboard/', dashboard, name='dashboard'),
    path('download_encrypted_file/<int:file_id>/', download_encrypted_file, name='download_encrypted_file'),
    #path('download_uploaded_file/<int:file_id>/', views.download_uploaded_file, name='download_uploaded_file'),
    path('file_list/', file_list, name='file_list'),
    path('delete_file/<int:file_id>/', delete_file, name='delete_file'),  
    
    path('download_uploaded_file/<int:file_id>/', views.download_file_taneesha, name='download_uploaded_file'),


]


#newly added
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)