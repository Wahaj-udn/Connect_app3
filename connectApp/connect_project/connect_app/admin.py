# connect_app/admin.py
'''from django.contrib import admin
from .models import CustomUser, Post

admin.site.register(CustomUser)
admin.site.register(Post)'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_alumni', 'roll_number')
    list_filter = ('is_staff', 'is_alumni', 'is_superuser')
    search_fields = ('username', 'email', 'roll_number')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'roll_number', 'is_alumni')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'roll_number', 'is_alumni'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)

