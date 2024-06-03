from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email_login']
            senha = form.cleaned_data['senha']

            usuario = auth.authenticate(request, username=email, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                aviso = 'Login efetuado com sucesso.'
                messages.success(request, aviso)
                return redirect('home')
            else:
                aviso = 'Login inválido! Dados incorretos.'
                messages.error(request, aviso)
                return redirect('login')

    return render(request, "usuarios/login.html", {"form": form})



def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                aviso = 'Senha diferente, repita o processo e coloque senhas iguais'
                messages.warning(request, aviso)
                return redirect('cadastro')
            
            nome = form["nome_cadastro"].value()
            email = form["email_login"].value()
            senha = form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe. Por favor, escolha outro.')
                return redirect('cadastro')

            if User.objects.filter(email=email).exists():
                aviso = 'Login já existe, escolha outro email!'
                messages.error(request, aviso)
                return redirect('cadastro')
        
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            aviso = 'Cadastro Efetuado com sucesso!'
            messages.success(request, aviso)
            return redirect('login')
        

    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'deslogado com sucesso')
    return redirect('login')