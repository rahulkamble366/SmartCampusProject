from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('TEACHER', 'Teacher'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')

    # Common fields for all user types
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
    campus_id = models.CharField(max_length=20, unique=True, blank=True, null=True)

    # Teacher-specific fields
    department = models.CharField(max_length=100, blank=True, null=True)
    employee_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)

    # Student-specific fields
    major = models.CharField(max_length=100, blank=True, null=True)
    enrollment_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    current_semester = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"