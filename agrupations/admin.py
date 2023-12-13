from django.contrib import admin
from .models import Client, House, Agrupation, Proyect, Block


class AgrupationAdmin(admin.ModelAdmin):
    search_fields = ["ci", "nomenclature"]
    # list_display = ["client_ci"]

# def client_ci(self, obj):
#     return obj.client.ci  # Asume que client_id es el campo que quieres mostrar
# # client_ci.short_description = 'Client CI'  # Establece el nombre de la columna en la interfaz de administración

admin.site.register(Client)
admin.site.register(House)
admin.site.register(Proyect)
admin.site.register(Block)
admin.site.register(Agrupation, AgrupationAdmin)