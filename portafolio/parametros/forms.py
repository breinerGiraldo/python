#importamos la libreria form
from django import forms

# creamos una lista con las posibles peticiones
from .pqrsf import PQRSF_CHOICES   

#CREAMOS LA ESTRUCTURA DEL FORMULARIO
class contacform(forms.Form):
    #cramos los campos
    email=forms.EmailField(label="correo electronico", widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
    tipom = forms.ChoiceFiel(choices = PQRSF_CHOICES, label="Tipo de Atencion Requerida", initial='', widget=forms.select(attrs={'class':'form-control'}),required=True)
    nombre= forms.CharField(label="nombre", required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    msj=forms.CharField(label='mensaje', widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}), required=True)