from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'legacy', 'career', 'year', 'academic_state')
    search_fields = ('legacy', 'user__first_name', 'user__last_name')

