# coding: utf-8
import time

from django import forms

from main.models import Transaccion, Empleado, TipoTransaccion, Cuenta, Rubro

tiposCuentas=((1,'Activo',),(2,'Pasivo',),(3,'Capital',),(4,'Resultado',))


class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               label='username',
                               widget=forms.TextInput(attrs={'class': 'validate white-text'}))
    password = forms.CharField(required=True,
                               label='password',
                               widget=forms.PasswordInput(attrs={'class': 'validate white-text'}))


class CuentaForm(forms.Form):
    nombre = forms.CharField(required=True,label='Nombre de la cuenta')
    rubro = forms.ModelChoiceField(required=True,queryset=Rubro.objects.all())
    tipo = forms.ChoiceField(required=True,choices=tiposCuentas)

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ["fecha", "empleado", "tipo", "cuenta", "monto", "comentario"]

    fecha = forms.DateField(
        required=True,
        label='Fecha',
        widget=forms.DateInput(attrs={
            'class': 'datepicker',
        }),
        initial=time.strftime("%d/%m/%Y"),
    )

    empleado = forms.ModelChoiceField(
        required=True,
        label='Empleado',
        widget=forms.Select(),
        queryset=Empleado.objects.all()
    )

    tipo = forms.ModelChoiceField(
        required=True,
        label='Tipo de transacción',
        widget=forms.Select(),
        queryset=TipoTransaccion.objects.all()
    )

    cuenta = forms.ModelChoiceField(
        required=True,
        label='Cuenta',
        widget=forms.Select(),
        queryset=Cuenta.objects.all()
    )

    monto = forms.DecimalField(
        required=True,
        label='Monto',
        min_value=0,
        decimal_places=5
    )

    comentario = forms.CharField(
        required=True,
        label='Comentario (Opcional)',
        max_length=100
    )
