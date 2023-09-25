from django.contrib import admin
from django.urls import path
from home import views
#newly added 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("security",views.security,name='security'),
    path("resources",views.resources,name='resources'),
    path("contact",views.contact,name='contact'),
    path("signin",views.signin,name='signin'),
    path("signup",views.signup,name='signup')
]

#newly added
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)