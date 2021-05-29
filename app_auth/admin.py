from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app_auth.models import (
    User,
)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'npm',
        'generation',
        'faculty',
        'study_program',
        'educational_program',
    )


admin.site.register(User, UserAdmin)
