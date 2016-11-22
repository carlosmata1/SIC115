# coding: utf-8

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from django.views.generic import ListView
from django.views.generic.edit import FormView

from main.forms import CuentaForm
from main.forms import EmpleadoForm
from main.forms import LoginForm
from main.forms import MovimientoForm

from django.forms import formset_factory
from main.forms import EmpleadoForm
from django.forms import formset_factory
from django.db.models import Max,Sum,Avg
import time
from decimal import Decimal
from main.forms import TransaccionForm
from main.forms import EquipoForm
from models import Cuenta, TipoCuenta, Transaccion, Empleado, Movimiento, ordenDeFabricacion, producto


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


def cuentas_list_view(request):
    cuentas=CuentaForm()
    return render(request,  'main/cuentas_list.html',

     {'cuenta': cuentas,'titulo':'Cuentas',
     'activos':Cuenta.objects.filter(tipo=1),
     'pasivos':Cuenta.objects.filter(tipo=2),
     'patrimonios':Cuenta.objects.filter(tipo=3),
     'ResultadosD':Cuenta.objects.filter(tipo=4),
     'ResultadosH':Cuenta.objects.filter(tipo=5),
     'contraActivos':Cuenta.objects.filter(tipo=6)})

                  

def cuenta_nueva(request):
    cuentas = CuentaForm()
    cuentaNueva = Cuenta()

    if request.method == 'POST':
        formulario = CuentaForm(request.POST)
        if formulario.is_valid():
            tipo=formulario.cleaned_data["tipo"]
            cuentaNueva.cuentaMayor=formulario.cleaned_data["cuenta_Mayor"]
            cuentaNueva.nombre = formulario.cleaned_data["nombre"]
            cuentaNueva.tipo = TipoCuenta.objects.get(id = int(tipo))

            cuentaNueva.rubro = formulario.cleaned_data["rubro"]
            rubro=cuentaNueva.rubro.numero
            cuentaNueva.codigo=str(cuentaNueva.cuentaMayor.codigo)+str(Cuenta.objects.filter(cuentaMayor=cuentaNueva.cuentaMayor).count()+1)
            cuentaNueva.saldoInicial=0
            cuentaNueva.debe=0
            cuentaNueva.haber=0
            cuentaNueva.saldoFinal=0

           

            cuentaNueva.save()
            return redirect('cuentas_list')
        else:
            return cuentas_list_view(request)

    return render(request,  'main/cuentas_list.html', {'cuenta': cuentas})


def ajustes_financieros_view(request):
    return render(request, 'main/ajustes_financieros.html', {
        'titulo': 'Ajustes',
    })


def balance_general_view(request):
    return render(request, 'main/balance_general.html', {
        'titulo': 'Balance',
        'activos':Cuenta.objects.filter(tipo=1).order_by('-rubro').exclude(saldoFinal=0.0),
        'pasivos':Cuenta.objects.filter(tipo=2).order_by('-rubro').exclude(saldoFinal=0.0),
        'patrimonios':Cuenta.objects.filter(tipo=3).order_by('-rubro').exclude(saldoFinal=0.0)
    })


def estado_capital_view(request):
    return render(request, 'main/estado_capital.html', {
        'titulo': 'Estado de Capital','patrimonioDebe':Cuenta.objects.filter(acreedor=False,tipo=3),'patrimonioHaber':Cuenta.objects.filter(acreedor=True,tipo=3)
    })


def estado_resultados(request):
    return render(request, 'main/estado_resultados.html', {
        'titulo': 'Estado de Resultados','resultadoDebe':Cuenta.objects.filter(tipo_id=4),'resultadoHaber':Cuenta.objects.filter(tipo_id=5)
    })


def balance_comprobacion(request):
    return render(request, 'main/balance_comprobacion.html', {


        'titulo': 'Balance de Comprobación','cuentas':Cuenta.objects.all(),'totalHaber':Cuenta.objects.filter(acreedor=True).aggregate(totalH=Sum('saldoFinal')),'totalDebe':Cuenta.objects.filter(acreedor=False).aggregate(totalD=Sum('saldoFinal'))
    })


def agregar_movimiento(request):

    formulario=TransaccionForm()

    if request.method == 'POST':
        futura = int(request.POST.get('mov'))
        movimientos = formset_factory(MovimientoForm, extra=futura)

        return render(request, 'main/libro_diario.html', {'titulo': 'Libro Diario', 'movimientos': movimientos, 'transaccion': formulario, 'agregar': True})
    elif request.method == 'GET':
        return render(request, 'main/libro_diario.html')

def agregar_Transaccion(request):
    transaccion=Transaccion()
    formulario=TransaccionForm(request.POST)
    movimientoF = formset_factory(MovimientoForm)
    if request.method=='POST':
        formulario=TransaccionForm(request.POST)
        movimientos=movimientoF(request.POST)
        if formulario.is_valid() & movimientos.is_valid():
            empleado1=formulario.cleaned_data["empleado"]
            transaccion=Transaccion.objects.create(empleado=empleado1,monto=formulario.cleaned_data["monto"],tipo=formulario.cleaned_data["tipo"],descripcion=formulario.cleaned_data["descripcion"],fecha=formulario.cleaned_data["fecha"])
            

            transaccion2=transaccion
            return guardarMovimientos(request,formulario,movimientos,transaccion2)
        return redirect('libro_diario')

def libro_diario(request):
    transaccionF = TransaccionForm()

    return render(request, 'main/libro_diario.html', {
        'titulo': 'Libro Diario', 'transaccion': transaccionF, 'agregar': False,
          'transacciones': Movimiento.objects.all()

    })



def guardarMovimientos(request,formulario,movimientos,transaccion):
    for movimiento in movimientos :
        movimientoM=Movimiento()
        movimientoM.cuenta=movimiento.cleaned_data.get('cuenta')
        movimientoM.debe=movimiento.cleaned_data.get('tipo')
        movimientoM.cantidad=movimiento.cleaned_data.get('cantidad')
        
        Movimiento.objects.create(cuenta=movimiento.cleaned_data.get('cuenta') ,debe=movimiento.cleaned_data.get('tipo') ,cantidad=movimiento.cleaned_data.get('cantidad') ,transaccion=Transaccion.objects.get(id=Transaccion.objects.count()))
        cuentaModificar=Cuenta.objects.get(id=movimientoM.cuenta.id)
        
        cuentaModificar.save()
        if movimientoM.debe :
            cuentaModificar.debe=float(movimientoM.cantidad)+cuentaModificar.debe
            t=guardarCambioCuenta(cuentaModificar)
        else:
            cuentaModificar.haber=float(movimientoM.cantidad)+cuentaModificar.haber
            t=guardarCambioCuenta(cuentaModificar)

    return redirect('libro_diario')

def guardarCambioCuenta(cuenta_modificar):
    if cuenta_modificar.haber >= cuenta_modificar.debe:
        cuenta_modificar.saldoFinal = cuenta_modificar.haber - cuenta_modificar.debe
        cuenta_modificar.acreedor = True
    else:
        cuenta_modificar.saldoFinal = cuenta_modificar.debe - cuenta_modificar.haber
        cuenta_modificar.acreedor = False
    cuenta_modificar.save()
    return 1


def empleado_view(reques):
    if reques.method == 'POST':
        form = EmpleadoForm(reques.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados_list')
    else:
        form = EmpleadoForm()

    return render(reques, 'main/agregarEmpleado.html', {'form': form, 'titulo': 'Agregar Empleado'})


class empleado_list(TemplateView):
    model = Empleado
    template_name = 'main/empleados_list.html'
    template_name = 'main/list_empleados.html'


class planilla(ListView):
    model = Empleado
    template_name = 'main/Planilla.html'



class listaOrdenes(ListView):
    model = ordenDeFabricacion
    template_name = 'main/ordenFabricacion.html'


class listaProductos(ListView):
    model = producto
    template_name = 'main/produccion_ventas.html'

def equipo_view(request):
    equipoForm=EquipoForm()

    return render(request ,'main/equipo_list.html',{'titulo':'Compra','comprarF':equipoForm})
