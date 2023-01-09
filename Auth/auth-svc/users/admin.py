from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

class UserAdmin(BaseUserAdmin):    
    list_display = ('username', 'name','date_joined', 'is_staff','last_login','secret_key')
    list_filter = ('is_staff',)

    fieldsets=(
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'mobile_number', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), ('Important dates', {'fields': ('last_login', )})
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide','extrapretty'),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    search_fields = ('username',)
    ordering = ('-date_joined',)



admin.site.register(User, UserAdmin)
