from django.contrib import admin
from .models import UserRegisterGroup


# Register your models here.
class UserRegisterAdmin (admin.ModelAdmin):

    list_display = [field.name for field in UserRegisterGroup._meta.fields]
    list_filter = ['name']
    search_fields = ['name', 'email']

    fields = ["email"]



    class Meta:
        model = UserRegisterGroup
admin.site.register(UserRegisterGroup, UserRegisterAdmin)


