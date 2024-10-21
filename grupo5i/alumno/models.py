from django.db import models

# Create your models here.

class Alumno (models.Model):
    apaterno=models.CharField(max_length=50, verbose_name="Apellido paterno jaja")
    amaterno=models.CharField(max_length=50, verbose_name="Apellido materno")
    nombre=models.CharField(max_length=100, verbose_name="Nombre(s)")
    fecha_nacimiento=models.DateField( verbose_name="Fecha de nacimiento", null=False, blank=False)
    fecha_ingreso=models.DateField( verbose_name="Fecha de ingreso", null=False, blank=False)

    class meta:
        db_table="alumnos"
        verbose_name="alumnoo"
        verbose_name_plural="alumnosjaj"

    def __str__(self) -> str:
        return self.nombre

class frase(models.Model):
    comentario=models.TextField(verbose_name="Comentarios",max_length=400)
    alumno_fk=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    
    class meta:
        verbose_name="frase"
        verbose_name_plural="Frases"