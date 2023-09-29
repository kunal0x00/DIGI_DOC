from django.contrib import admin

from home.models import Contact
from .models import User
# Register your models here.

admin.site.register(Contact)

admin.site.register(User)