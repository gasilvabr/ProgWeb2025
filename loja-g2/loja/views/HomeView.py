#from django.http import HttpResponse
from django.shortcuts import render
from loja.models import Produto

def home_view(request):
    text_produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    if text_produto is not None:
        produtos = produtos.filter(Produto__contains=text_produto)
    print(text_produto) #Conteudo digitado pelo usuaro
    print(produtos) # Produtos do banco de dados com o texto digitado pelo usuario
    contexto = {
        'produtos': produtos
    }
    return render(request, template_name='home/home.html', context=contexto, status=200)