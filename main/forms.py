import datetime
from django import forms
from models import Cuenta,Rubro,Transaccion,Empleado,TipoTransaccion

tiposCuentas=((1,'Activo',),(2,'Pasivo',),(3,'Capital',),(4,'Resultado',))
DATE_INPUT_FORMATS = ('%d-%m-%Y')
debes=((True,'False',),(False,'True',))

class LoginForm(forms.Form):
    	username = forms.CharField(required=True,
                               label='username',
                               widget=forms.TextInput(attrs={'class': 'validate white-text'}))
    	password = forms.CharField(required=True,
                               label='password',
                               widget=forms.PasswordInput(attrs={'class': 'validate white-text'}))
class CuentaForm(forms.Form):
 		nombre=forms.CharField(required=True,
 								label='Nombre de la cuenta')
 		rubro=forms.ModelChoiceField(required=True,
 			queryset=Rubro.objects.all())						
		tipo=forms.ChoiceField(required=True,
			choices=tiposCuentas)


class MovimientoForm(forms.Form):
	cuenta=forms.ModelChoiceField(label='Eliga la cuenta a realizar el movimiento',
		queryset=Cuenta.objects.all())
	

	tipo=forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'id':'test6p','checked':'checked'}),
        choices=debes,
    )
	cantidad=forms.DecimalField(label='Cantidad a transferir a Cuenta:',max_digits=10,decimal_places=2,min_value=0)
	
	
		
class TransaccionForm(forms.Form):
	monto=forms.DecimalField(label='monto de transaccion',max_digits=10, decimal_places=2,min_value=0.0)
	empleado=forms.ModelChoiceField(required=True,
			queryset=Empleado.objects.all())
	tipo=forms.ModelChoiceField(required=True,
			queryset=TipoTransaccion.objects.all())
	descripcion=forms.CharField(widget=forms.Textarea)
	fecha=forms.DateField()