from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Postulacion

@admin.register(Postulacion)
class PostulationAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'oferta', 'estado', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('estudiante__usuario__first_name',
                    'estudiante__usuario__last_name',
                    'estudiante__dni',
                    'oferta__titulo',
                    'oferta__empresa__nombre')
    actions = ["accept_postulation"]

    def accept_postulation(self, request, queryset):
        for postulation in queryset:
            try:
                postulation.accept(accepted_by_user=request.user)
            except ValidationError as e:
                self.message_user(request, str(e), level="error")
                return 
            
        self.message_user(request, "Postulación aceptada y oferta cerrada correctamente")
        