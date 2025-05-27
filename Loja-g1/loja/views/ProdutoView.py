from django.http import HttpResponse
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone

def list_produto_view(request, id=None):
    #Carrega dados do navegador
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    f = request.GET.get("xfabricante")
    dias = request.GET.get("dias")
    #mostra dados do navegador
    if destaque is not None:
        print(destaque)
    if produto is not None:
        print(produto)
    if promocao is not None:
        print(promocao)
    if categoria is not None:
        print(categoria)
    if f is not None:
        print(f)
    #carrega dados do banco de dados
    produtos = Produto.objects.all()
    #produtos = Produto.objects.filter(criado_em__gt=datetime.now())
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if f is not None:
        produtos = produtos.filter(fabricante__Fabricante=f)
    if id is not None:
        produtos = produtos.filter(id=id)
    if dias is not None:
        print(dias)
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gt=now)
                
    #mostra dados do banco de dados
    print(produtos)

    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')

    return HttpResponse('<h1>Produto de id %s!</h1>' % id)