from django import forms
from models import Cuenta,Rubro

tiposCuentas=((1,'Activo',),(2,'Pasivo',),(3,'Capital',),(4,'Resultado',))


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
 		rubro=forms.ModelChoiceField(required=True,queryset=Rubro.objects.all())						
		tipo=forms.ChoiceField(required=True,choices=tiposCuentas)
		
		