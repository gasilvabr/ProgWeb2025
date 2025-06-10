#from django.http import HttpResponse
from django.shortcuts import render
from loja.models import Produto

def home_view(request):
    textodigitado_produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    if textodigitado_produto is not None:
        produtos = produtos.filter(Produto__contains=textodigitado_produto)    
    print(textodigitado_produto)        
    print(produtos)

    contexto = {
        'produtos': produtos
    }

    return render(request, template_name='home/home.html', context=contexto, status=200)