from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuit', 'rubro', 'contacto')
    search_fields = ('nombre', 'cuit')

