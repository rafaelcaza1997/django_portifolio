from django.contrib import admin

# Register your models here.
from projetos.models import Projeto

class ProjetoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Projeto, ProjetoAdmin)

admin.site.site_header = "APP Portfólio"
admin.site.site_title = "Admin"
admin.site.index_title = " Painel de controle "