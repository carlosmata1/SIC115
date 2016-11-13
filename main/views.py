# coding: utf-8

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView

from main.forms import LoginForm, TransaccionForm
from main.models import Transaccion


@login_required(login_url='login')
def index_view(request):
    return render(request, 'main/index.html')


class ViewLoginForm(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('index')


def acerca_de_view(request):
    return render(request, 'main/acerca_de.html', {
        'titulo': 'Acerca de',
    })


def ayuda_view(request):
    return render(request, 'main/ayuda.html', {
        'titulo': 'Ayuda',
    })


def proveedores_list_view(request):
    return render(request, 'main/list_proveedores.html', {
        'titulo': 'Proveedores',
    })


def usuarios_list_view(request):
    return render(request, 'main/list_usuarios.html', {
        'titulo': 'Usuarios',
    })


def empleados_list_view(request):
    return render(request, 'main/list_empleados.html', {
        'titulo': 'Empleados',
    })


def ajustes_financieros_view(request):
    return render(request, 'main/ajustes_financieros.html', {
        'titulo': 'Ajustes',
    })


def balance_general_view(request):
    return render(request, 'main/balance_general.html', {
        'titulo': 'Balance',
    })


def estado_capital_view(request):
    return render(request, 'main/estado_capital.html', {
        'titulo': 'Estado de Capital',
    })


def estado_resultados(request):
    return render(request, 'main/estado_resultados.html', {
        'titulo': 'Estado de Resultados',
    })


def balance_comprobacion(request):
    return render(request, 'main/balance_comprobacion.html', {
        'titulo': 'Balance de Comprobación',
    })


# def libro_diario(request):
#     return render(request, 'main/libro_diario.html', {
#         'titulo': 'Libro Diario',
#     })


class TransaccionCreateView(CreateView):
    model = Transaccion
    template_name = 'main/libro_diario.html'
    form_class = TransaccionForm
    success_url = reverse_lazy('libro_diario')
