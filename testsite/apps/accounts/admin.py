from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import UserInterest, UserPersona, UserProfile

admin.site.register(UserProfile)
admin.site.register(UserPersona)
admin.site.register(UserInterest)