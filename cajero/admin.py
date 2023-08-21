from django.contrib import admin
from . import models
# Register your models here.
class UsuarioBancoAdmin(admin.ModelAdmin):
    list_display=["id","id_usuario","nombre"]
    list_editable=["id_usuario","nombre"]
    search_fields=["id_usuario","nombre"]
    list_per_page=20
    
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ["id","id_usuario", "id_nro_cta", "balance"]  
    list_editable = ["id_usuario", "id_nro_cta", "balance"]  
    list_display_links = None  
    search_fields = ["id_usuario__name", "id_numero_cta"]  
    list_per_page = 20


class GiroCuentaAdmin(admin.ModelAdmin):
    list_display = ["monto_giro", "id_nro_cta", "id_transaccion"]
    list_editable = ["id_nro_cta", "id_transaccion"]  
    search_fields = ["id_nro_cta__id_nro_cta", "id_transaccion"]
    list_per_page = 20
    list_display_links = ["monto_giro"]


class DepositoCuentaAdmin(admin.ModelAdmin):
    list_display = ["monto_deposito", "id_nro_cta", "id_transaccion"]
    list_editable = ["id_nro_cta", "id_transaccion"]  
    search_fields = ["id_nro_cta", "id_transaccion"]
    list_per_page = 20
    list_display_links = ["monto_deposito"]


# Register your models here.
admin.site.register(models.UsuarioBanco,UsuarioBancoAdmin)
admin.site.register(models.CuentaBancaria,CuentaBancariaAdmin)
admin.site.register(models.GiroCuenta,GiroCuentaAdmin)
admin.site.register(models.DepositoCuenta,DepositoCuentaAdmin)