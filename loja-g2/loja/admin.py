from django.contrib import admin

class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'preco', 'categoria',)
    exclude =('msgPromocao',)
    search_fields = ('Produto',)

# Register your models here.
from .models import * #imporata nossos models
admin.site.register(Fabricante,FabricanteAdmin) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
# incluir a tabela de usuário no final
admin.site.register(Usuario)