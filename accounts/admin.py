from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser, OrganizerProfile


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('email', 'password', 'is_active', 'is_staff')


class OrganizerProfileInline(admin.StackedInline):
    model = OrganizerProfile
    can_delete = False
    verbose_name_plural = 'Organizer Profile'


class CustomUserAdmin(DefaultUserAdmin):
    form = CustomUserChangeForm
    add_form = DefaultUserAdmin.add_form
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    inlines = (OrganizerProfileInline,)


admin.site.register(CustomUser, CustomUserAdmin)
