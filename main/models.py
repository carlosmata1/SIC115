from __future__ import unicode_literals

from django.db import models


class Puesto(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    salarioNominalDiario = models.DecimalField(max_digits=10, decimal_places=5, null=False)
    def __str__(self):
        return self.nombre

# Create your models here.
class Empleado(models.Model):
    sexo_opt = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
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
    def __str__(self):
        return self.nombres+" "+self.apellidos


class Usuario(models.Model):
    id = models.TextField(max_length=25, primary_key=True, auto_created=False, editable=True)
    password = models.CharField(max_length=64, null=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)


class Proveedor(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    marca = models.CharField(max_length=50, null=False)
    direccion = models.TextField(max_length=200, null=False)
    telefono = models.CharField(max_length=9, null=False)
    nit = models.CharField(max_length=17, null=False)


class TipoTransaccion(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=49, null=False)
    def __str__(self):
        return self.nombre


class Rubro(models.Model):
    id = models.IntegerField(editable=False,auto_created=True, primary_key=True)
    numero=models.IntegerField()
    nombre=models.CharField(max_length=21, null=False)    
    def __unicode__(self):
        return self.nombre
        

class TipoCuenta(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    codigo=models.CharField(max_length=5,null=False)
    nombre = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    saldoInicial = models.DecimalField(max_digits=20, decimal_places=2)
    nombre=models.CharField(max_length=50,  null=False)
    tipo=models.ForeignKey(TipoCuenta, null=False)
    debe = models.DecimalField(max_digits=20, decimal_places=2)
    haber = models.DecimalField(max_digits=20, decimal_places=2)
    saldoFinal = models.DecimalField(max_digits=20, decimal_places=2)
    codigo= models.CharField(max_length=5, null=False)
    acreedor=models.BooleanField(default=True)
    rubro=models.ForeignKey(Rubro,null=False)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=9, null=False)


class Inventario(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    descripcion = models.TextField(max_length=100, null=False)
    valor = models.DecimalField(max_digits=5, decimal_places=5)


class Transaccion(models.Model):
    id = models.IntegerField(editable=False, auto_created=True, primary_key=True)
    fecha = models.DateField()
    empleado = models.ForeignKey(Empleado, null=False)
    tipo = models.ForeignKey(TipoTransaccion, null=False)
    descripcion=models.TextField(max_length=10,null=True)
    monto = models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return str(self.id)
class Movimiento(models.Model):
    id=models.IntegerField(editable=False,auto_created=True,primary_key=True)
    transaccion=models.ForeignKey(Transaccion, null=False)
    cuenta=models.ForeignKey(Cuenta,null=False)
    debe=models.BooleanField()
    cantidad=models.DecimalField(max_digits=10,decimal_places=5,null=True)
    def __str__(self):
        return str(self.cantidad)


class prestacion(models.Model):
    id=models.IntegerField(editable=False, auto_created=True, primary_key=True)
    nombre=models.CharField(max_length=100, null=False)
    porcentage= models.DecimalField(max_digits=6,decimal_places=3)
    def __str__(self):
        return self.nombre