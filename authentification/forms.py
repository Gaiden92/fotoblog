from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, min_length=8, widget=forms.PasswordInput, label="Entrez un mot de passe")
    