from django.shortcuts import render,HTTpResponse,redirect
from django.urls import reverse
from.forms import contacform

# Create your views here.

def indexcore(request):
    FormContac = contacform()
    if request.method == "POST":
        FormContac = contacform(data=request.POST)
        if FormContac.is_valid():
            email = request.POST.get('email', ' ')
            tipom = request.POST.get('tipom', '')
            nombre = request.POST.get('nombre', '')
            msj = request.POST.get('msj','')
            
            FormContac.save()
            return redirect(reverse('inicio')+"?Ok")
            #
            #
    #
     return render(request,'core/index.html',{'formulario':FormContac})



