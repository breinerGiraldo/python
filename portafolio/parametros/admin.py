from django.contrib import admin

# Register your models here.
from. models import Etnia
from. models import TipoDocu
from. models import EstaCivil
from. models import TipoEstu
from. models import TipoLogr

admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)

# class EtniaModelAdmin(admin.ModelAdmin):
#     #indicamos que columnas queremos ver(en este caso solo mostramos el nombre ya que no tenemos otras)
#     list_display=["NombreEtni"]
#     #indicamos que columna hacemos clic para editar
#     #list_display_links=[NombreEtni]
#     #agregamos una barra de busqueda
#     search_fields=["NombreEtni"]
#     #podemos agrgar un filtro
#     list_filter=["NombreEtni"]
#     #indicamos desde donde se optinen los datos
#     class Meta:
#         model=Etnia
# admin.site.register(Etnia)

#estado civil

# class EstaCivilModelAdmin(admin.ModelAdmin):
#     #indicamos que columnas queremos ver(en este caso solo mostramos el nombre ya que no tenemos otras)
#     list_display=["NombreEsta"]
#     #indicamos que columna hacemos clic para editar
#     #list_display_links=[NombreEtni]
#     #agregamos una barra de busqueda
#     search_fields=["NombreEsta"]
#     #podemos agrgar un filtro
#     list_filter=["NombreEsta"]
#     #indicamos desde donde se optinen los datos
#     class Meta:
#         model=EstaCivil
# admin.site.register(EstaCivil)


# #tipo de documento
# class TipoDocuModelAdmin(admin.ModelAdmin):
#     #indicamos que columnas queremos ver(en este caso solo mostramos el nombre ya que no tenemos otras)
#     list_display=["NombreTiDo"]
#     #indicamos que columna hacemos clic para editar
#     #list_display_links=[NombreEtni]
#     #agregamos una barra de busqueda
#     search_fields=["NombreTiDo"]
#     #podemos agrgar un filtro
#     list_filter=["NombreTiDo"]
#     #indicamos desde donde se optinen los datos
#     class Meta:
#         model=TipoDocu
# admin.site.register(TipoDocu)

# #tipo de logro
# class TipoLogrModelAdmin(admin.ModelAdmin):
#     #indicamos que columnas queremos ver(en este caso solo mostramos el nombre ya que no tenemos otras)
#     list_display=["NombreTiLo"]
#     #indicamos que columna hacemos clic para editar
#     #list_display_links=[NombreEtni]
#     #agregamos una barra de busqueda
#     search_fields=["NombreTiLo"]
#     #podemos agrgar un filtro
#     list_filter=["NombreTiLo"]
#     #indicamos desde donde se optinen los datos
#     class Meta:
#         model=TipoLogr
# admin.site.register(TipoLogr)



    