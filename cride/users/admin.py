""""User models admi"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from cride.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """User model admin"""
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')

    list_filter = ('is_client', 'is_staff', 'created_at', 'updated_at')

admin.site.register(User,CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin"""

    list_display= ('user','reputation','rides_taken','rides_offered')
    search_fields=('user__username','user__email','user__rides_taken','user__rides_offered')
    list_filter=('reputation',)