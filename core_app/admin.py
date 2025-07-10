from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # The fields to be displayed in the list view of the admin panel
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_type', 'campus_id')

    # Fields to be used as filters in the list view
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active', 'groups')

    # Fields to be searched in the list view
    search_fields = ('username', 'email', 'first_name', 'last_name', 'campus_id', 'employee_id', 'enrollment_id')

    # Order of fields in the list view
    ordering = ('username',)

    # Customize the form for changing an existing user
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': (
            'user_type',
            'phone_number',
            'address',
            'date_of_birth',
            'profile_picture', # Corrected typo here
            'campus_id',
            'department',
            'employee_id',
            'designation',
            'major',
            'enrollment_id',
            'current_semester',
        )}),
    )

    # Customize the form for adding a new user
    # Note: add_fieldsets is separate because when adding a user, password
    # fields are typically shown, but not when editing an existing user.
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': (
            'user_type',
            'phone_number',
            'address',
            'date_of_birth',
            'profile_picture', # Corrected typo here
            'campus_id',
            'department',
            'employee_id',
            'designation',
            'major',
            'enrollment_id',
            'current_semester',
        )}),
    )

# Register your custom User model with your CustomUserAdmin class
admin.site.register(User, CustomUserAdmin)
