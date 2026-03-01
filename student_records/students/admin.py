from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'first_name', 'last_name', 'email', 'grade')
    search_fields = ('first_name', 'last_name', 'email', 'roll_number')
    list_filter = ('grade',)