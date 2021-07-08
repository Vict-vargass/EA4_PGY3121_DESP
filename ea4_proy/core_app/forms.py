from django import forms
from django.db.models import fields
from django.db.models.fields import CharField, EmailField
from django.forms import ModelForm, widgets
from .models import Obra

class publicarObra(forms.ModelForm):

    class Meta:
        model = Obra
        fields = ['nombreObra','historia','descripcion','precio','tecnicaUsada','categoria','imagen']
        widgets={
            'nombreObra': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre de la obra'}),
            'historia' : forms.Textarea(attrs={'class':'form-control resize','cols':'10','rows':'6','placeholder':'Ingrese la historia de la obra'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control resize','cols':'10','rows':'6','placeholder':'Ingrese una descripción'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'tecnicaUsada' : forms.Textarea(attrs={'class':'form-control resize','cols':'10','rows':'6','placeholder':'Ingrese la tecnica empleada'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
 
class EditarObra(forms.ModelForm):

    class Meta:
        model = Obra
        fields = ['idObra','nombreObra','historia','descripcion','precio','tecnicaUsada','categoria']
        widgets={
            'idSolicitudObra': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreObra': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre de la obra'}),
            'historia' : forms.Textarea(attrs={'class':'form-control resize','cols':'10','rows':'6','placeholder':'Ingrese la historia de la obra'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control resize','cols':'10','rows':'6','placeholder':'Ingrese una descripción'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'tecnicaUsada' : forms.Textarea(attrs={'class':'form-control resize','cols':'10','rows':'6','placeholder':'Ingrese la tecnica empleada'}),
            'categoria': forms.Select(attrs={'class': 'form-control'})
        }