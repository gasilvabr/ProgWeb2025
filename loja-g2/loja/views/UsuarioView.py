from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm

def list_usuario_view(request, id=None):
    # carrega somente usuarios, não inclui os admin
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
        'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context, status=200)

def edit_usuario_view(request):
    print('edit_usuario_view')
    ##usuario = request.user
    usuario = get_object_or_404(Usuario, user=request.user)
    ##print(usuario)
    print('edit_usuario_view2')
    usuarioForm = UserUsuarioForm(instance=usuario)
    print('edit_usuario_view3')
    userForm = UserForm(instance=request.user)
    print('edit_usuario_view4')
    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm
    }
    print('edit_usuario_view5')
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)    
    