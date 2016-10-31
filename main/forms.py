from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               label='username',
                               widget=forms.TextInput(attrs={'class': 'validate white-text'}))
    password = forms.CharField(required=True,
                               label='password',
                               widget=forms.PasswordInput(attrs={'class': 'validate white-text'}))
