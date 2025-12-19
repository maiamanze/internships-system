from django.contrib import admin
from .models import Reporte

@admin.register(Reporte)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("practica", "tipo", "fecha", "aprobado")
    list_filter = ("tipo", "aprobado")
    search_fields = ("practica__estudiante__usuario__first_name", "practica__estudiante__usuario__last_name", "practica__estudiante__dni")
