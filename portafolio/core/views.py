from django.shortcuts import render,HTTpResponse

# Create your views here.

def indexcore(request):
    return render(request,'index.html')

def nosotros(request):
    return render(request,'nosotros.html')    

def indexcore(request):
    #iniciamos el formulario de contacto
    FormarContac= ContactForm()
    #validamos  que se haya echo la peticion post del formulario de contacto
    if request.method == "POST":
       #re asiganmos el valor del formcntacto estavez con todo los datos del formulario
       FormarContac =  ContactForm(data=request.POST)
       #validaremos que todos los campos sean de dato correcto
       if FormarContac.is_valid():
           #retornamos validaciones  de los campos
           email = request.POST.get('email', '')
           tipom = request.POST.get('tipom,' , '')
           nombre = request.POST.get('nombre', '')
           msj = request.POST.get('msj', '')
           # si todo sale bien que no creo XD guardamos y rendericimos al nombre de la url con un mensaje 
           FormarContac.save()
           return redirect(reverse('inicio')+"?Ok")
           #otra forma de redirecionar
           # return direct(/index/?ok!)
    return render(request,'index.html',{'formulario': FormarContac}) 
    
