from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
import django.contrib.auth

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'pk')
    pass

authlist_display = ('pk', )