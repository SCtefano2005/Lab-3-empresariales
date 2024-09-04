from django.shortcuts import render, redirect, get_object_or_404 #get_object_or_404 sirve para devolver un error si no encuentra nada con los parametros en la bd y manda un error 404
from .forms import *
from .models import *

def index(request): # renderiza el index
    return render(request, 'index.html') 

def registrar_usuario(request): # funcion para registrar usuarios
    if request.method == 'POST':# si es metodo POST carga el form de forms.py
        form = UsuarioForm(request.POST) # instancia el formulario con los datos ingresados por el usuario
        if form.is_valid():# si forms es valido guarda las rptas de form con form.save() y lo guarda en la variable usuario
            usuario = form.save()
            return redirect('usuario_detail', id=usuario.id)# redirije a usuario_detail dandole el parametro id.usuario
    else:
        form = UsuarioForm()# si el metodo es get carga el formulario 
    return render(request,'registrar_usuario.html', {'form': form})

def registrar_carro(request):# funcion para registrar carros
    if request.method == 'POST': #si es metodo POST carga el form de forms.py
        form = CarroForm(request.POST) #instancia el formulario con los datos ingresados por el usuario
        if form.is_valid():# si forms es valido va a procesar los datos
            dni = form.cleaned_data['dni'] # obitiene el dni y lo guarda en la variable dni
            usuario = get_object_or_404(Usuario, dni=dni)# verifica si el dni del usuario existe lo guarda en variable usuario, si no existe le manda error 404
            carro = form.save(commit=False)#aca crea una instancia el modelo carro pero sin guardar, seria como un staggin area de git.
            carro.usuario = usuario# aca le asigna el usuario encontrado por dni al carro
            carro.save()#commitea o guarda la instancia ahora si y lo manda a la bd
            return redirect('carro_detail', id=carro.id)# redirije al carro_detail pasandole el id del carro
    else:
        form = CarroForm()# si el metodo es get carga el formulario 
    
    return render(request, 'registrar_carro.html', {'form': form})

def usuario_detail(request, id): #Funcion para mostrar los datos de un usuario mediante su id
    usuario = get_object_or_404(Usuario, id=id)# busca al usuario por su id, si la id del usuario no existe, le manda el error 404
    return render(request, 'usuarios_detail.html', {'usuario': usuario})# renderiza al template 

def carro_detail(request, id):#Funcion para mostrar los datos de un usuario mediante su id
    carro = get_object_or_404(Carro, id=id)# busca al carro por su id, si la id del carro no existe, le manda el error 404
    return render(request, 'carros_detail.html', {'carro': carro})# renderiza al template 

def editar_usuario(request, id): # este sirve pa editar
    usuario = get_object_or_404(Usuario, id=id) #aca verifica si existe el usuario por su id, si no existe manda un error 404
    if request.method == 'POST': # aca verifica si POST
        form = UsuarioForm(request.POST, instance=usuario) # aca carga el formulario e instancia al objeto usuario que esta en la primera parte
        if form.is_valid():# verifica si es valido el form
            form.save()# Guarda el form y sobreescribe la informacion del usuario en la bd
            return redirect('usuario_detail', id=usuario.id)# redirije a detail
    else:
        form = UsuarioForm(instance=usuario)# si el metodo es get carga el formulario instanciando al objeto usuario
    return render(request, 'editar_usuario.html', {'form': form})

def editar_carro(request, id):
    carro = get_object_or_404(Carro, id=id)
    if request.method == 'POST':
        form = CarroForm_editar(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_detail', id=carro.id)
    else:
        form = CarroForm_editar(instance=carro)
    return render(request, 'editar_carro.html', {'form': form})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})


def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'listar_carros.html', {'carros': carros})


def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'confirmar_eliminar_usuario.html', {'usuario': usuario})


def eliminar_carro(request, id):
    carro = get_object_or_404(Carro, id=id)
    if request.method == 'POST':
        carro.delete()
        return redirect('listar_carros')
    return render(request, 'confirmar_eliminar_carro.html', {'carro': carro})
