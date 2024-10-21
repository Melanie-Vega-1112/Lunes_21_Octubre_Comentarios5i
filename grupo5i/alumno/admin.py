from django.contrib import admin
from .models import Alumno, frase

# Register your models here.

class comentariointline(admin.TabularInline):
    model=frase
    extra=1


class alumnoadmin(admin.ModelAdmin):
    fields=["apaterno", "amaterno", "nombre", "fecha_nacimiento", "fecha_ingreso"]
    list_display=["apaterno", "amaterno", "nombre"]
    inlines=[comentariointline]

admin.site.register(Alumno, alumnoadmin)

@admin.register(frase)
class fraseadmin(admin.ModelAdmin):
    fields=["comentario", "alumnofk"]
    list_display=["comentario"]