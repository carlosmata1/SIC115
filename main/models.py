# coding: utf-8
from __future__ import unicode_literals

from django.db import models


class Puesto(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre = models.TextField(max_length=30, null=False)
    salario = models.DecimalField(max_digits=5, decimal_places=5, null=False)


# Create your models here.
class Empleado(models.Model):
    sexo_opt = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombres = models.TextField(max_length=50, null=False)
    apellidos = models.TextField(max_length=50, null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=1, choices=sexo_opt, null=False)
    direccion = models.TextField(max_length=200, null=False)
    telefono = models.CharField(max_length=9, null=False)
    contacto = models.CharField(max_length=9, null=False)
    dui = models.CharField(max_length=10, null=False)
    nit = models.CharField(max_length=17, null=False)
    afp = models.CharField(max_length=12, null=False)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    activo = models.BooleanField()

    def __unicode__(self):
        return self.nombres + " " + self.apellidos

    def getSexo(self):
        sexo_opt = {
            'M': 'Masculino',
            'F': 'Femenino'
        }

        return sexo_opt.get(self.sexo)


class Usuario(models.Model):
    id = models.TextField(max_length=25, primary_key=True, auto_created=False, editable=True)
    password = models.CharField(max_length=64, null=False, blank=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.empleado


class Proveedor(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    marca = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.TextField(max_length=200, null=False, blank=False)
    telefono = models.CharField(max_length=9, null=False, blank=False)
    nit = models.CharField(max_length=17, null=False, blank=False)

    def __unicode__(self):
        return self.marca


class TipoTransaccion(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)


class Rubro(models.Model):
    id = models.IntegerField(editable=False,auto_created=True, primary_key=True)
    numero=models.IntegerField()
    nombre=models.CharField(max_length=21, null=False)

    def __unicode__(self):
        return self.nombre


class TipoCuenta(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __unicode__(self):
        return self.nombre


class Cuenta(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tipo = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, default=1)
    saldoInicial = models.DecimalField(max_digits=5, decimal_places=5)
    debe = models.DecimalField(max_digits=5, decimal_places=5)
    haber = models.DecimalField(max_digits=5, decimal_places=5)
    saldoFinal = models.DecimalField(max_digits=5, decimal_places=5)
    # proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    rubro=models.ForeignKey(Rubro)

    def __unicode__(self):
        return self.nombre


class Cliente(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.CharField(max_length=9, null=False)

    def __unicode__(self):
        return self.nombre


class Inventario(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    descripcion = models.TextField(max_length=100, null=False, blank=False)
    valor = models.DecimalField(max_digits=5, decimal_places=5)

    def __unicode__(self):
        return self.descripcion


class Transaccion(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    fecha = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=5, decimal_places=5)
    comentario = models.TextField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.empleado + " al " + self.fecha
