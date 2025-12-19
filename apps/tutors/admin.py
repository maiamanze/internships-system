from django.contrib import admin
from .models import Tutor

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ("usuario", "tipo", "institucion")
    list_filter = ("tipo",)
    search_fields = ("usuario__first_name", "usuario__last_name")