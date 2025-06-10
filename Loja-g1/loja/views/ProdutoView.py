#from django.http import HttpResponse
from django.shortcuts import render # Retire from django.http import HttpResponse

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

    # Adicione para definir o contexto e carregar o template
    context = {
        'produtos': produtos
    }
    return render(request, template_name='produto/produto.html', context=context, status=200)

def edit_produto_view(request, id=None):
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = { 'produto': produto }
    return render(request, template_name='produto/produto-edit.html', context=context, status=200)
