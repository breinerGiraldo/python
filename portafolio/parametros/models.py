from django.db import models
#from ckeditor.fields import RichTextField

#importamos la liosta de tipos de mensaje
from .pqrsf import PQRSF_CHOICES


class Contact(models.Model):
    email=models.EmailField( max_length=50, verbose_name="correo electronico")
    tipom=models.CharField( max_length=50, choices=PQRSF_CHOICES,default="peticion",verbose_name="categoria")
    nombre=models.CharField( max_length=250,verbose_name="Nombre")
    #msj=RichTextField(default="quisiera",verbose_name="mensaje")

    #sub clase para organzar los nombres de acuerdo al diccionario que usemos
    class Meta:
        verbose_name="Mensaje PQRSF"
        verbose_name_plural="mensajes PQRSF"


     
    def __str__(self):
        return self.nombre
   
class Etnia(models.Model):
    NombreEtni=models.CharField(max_length=50)

    # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Grupo Etnico"
        verbose_name_plural = "Grupos Etnicos"

    def __str__(self):
        return self.NombreEtni

class EstaCivil(models.Model):
    NombreEsta=models.CharField(max_length=50)

     # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estado civil"

    def __str__(self):
        return self.NombreEsta
        
class TipoDocu(models.Model):
    NombreTiDo=models.CharField(max_length=50)

     # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Tipo De Documento"
        verbose_name_plural = "Tipo De Documentos"

    def __str__(self):
        return self.NombreTiDo

    
class TipoEstu(models.Model):
    NombreTiEs=models.CharField(max_length=50)

     # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Tipo De Estudiante"
        verbose_name_plural = "Tipo De Estudiantes"

    def __str__(self):
        return self.NombreTiEs

        
class TipoLogr(models.Model):
    NombreTiLo=models.CharField(max_length=50)

  # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Tipo De Logro"
        verbose_name_plural = "Tipo De Logros"

    def __str__(self):
        return self.NombreTiLo


