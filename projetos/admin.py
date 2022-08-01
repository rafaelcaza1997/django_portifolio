from django.contrib import admin

# Register your models here.
from projetos.models import Projeto

class ProjetoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Projeto, ProjetoAdmin)
