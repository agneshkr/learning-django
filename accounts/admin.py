from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    add_form= CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser

    list_display = ["username","name","email","is_staff"]
    filter_display = ["is_staff"]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),) 
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)

admin.site.register(CustomUser,CustomUserAdmin)