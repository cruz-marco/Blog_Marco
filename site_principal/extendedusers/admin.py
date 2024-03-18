from django.contrib import admin
from .models import SocialMedia, PersonalData
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class SocialMediaInline(admin.StackedInline):
    model = SocialMedia
    can_delete = False
    verbose_name_plural = 'Redes Sociais'


class PersonalDataInline(admin.StackedInline):
    model = PersonalData
    can_delete = False
    verbose_name_plural = 'Dados pessoais'


class CustomUserAdmin(UserAdmin):
    inlines = (PersonalDataInline, SocialMediaInline)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
