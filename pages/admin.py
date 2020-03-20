from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreationForm,CustomUserChangeForm
from . models import Module,Professor,Rating,CustomUser
admin.site.register(Module)
admin.site.register(Professor)
admin.site.register(Rating)

class CustomUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = CustomUser

admin.site.register(CustomUser,CustomUserAdmin)