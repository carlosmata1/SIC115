from django.contrib import admin
from models import Cuenta,TipoCuenta,Rubro, Transaccion,TipoTransaccion,Empleado,Puesto,Movimiento

from models import Cuenta,TipoCuenta,Rubro, Transaccion,TipoTransaccion,Empleado,Puesto,Movimiento,prestacion

# Register your models here.
admin.site.register(Cuenta)
admin.site.register(TipoCuenta)
admin.site.register(Rubro)
admin.site.register(Transaccion)
admin.site.register(TipoTransaccion)
admin.site.register(Empleado)
admin.site.register(Puesto)
admin.site.register(Movimiento)
admin.site.register(prestacion)
