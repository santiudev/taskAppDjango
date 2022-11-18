
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ('id', "first_name", "last_name", "email", "date_joined")

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)