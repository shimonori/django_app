from django import forms

class LoginForm(forms.Form):
    mail = forms.EmailField(label='mail')
    passwd = forms.CharField(label='passwd')
    
class notLoginForm(forms.Form):
    mail = forms.EmailField(label='mail')