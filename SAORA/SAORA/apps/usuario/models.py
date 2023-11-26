import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TipoUsuario(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    tipo_usuario = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=250)
    ultima_actualizacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s : %s"%(self.tipo_usuario,self.descripcion)

class TipoAfiliado(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    tipo_afiliado = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=250)
    ultima_actualizacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s : %s"%(self.tipo_afiliado,self.descripcion)

class Afiliado(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    direccion = models.CharField(max_length=500)
    telefono = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)
    tipo_afiliado = models.ForeignKey(TipoAfiliado, on_delete=models.DO_NOTHING, null=False, blank=False)
    ultima_actualizacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s %s"%(self.nombre,self.apellido_paterno,self.apellido_materno)

class Usuario(AbstractUser):
    tipo_afiliado = models.ForeignKey(TipoAfiliado, on_delete=models.DO_NOTHING, null=True, blank=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, null=True, blank=True)
    ultima_actualizacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return  "Usuario: %s"%(self.username)