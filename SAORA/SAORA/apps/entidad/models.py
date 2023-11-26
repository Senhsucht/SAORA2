import uuid,random
from django.db import models
from django.utils import timezone

# Create some functions
def random_string():
    return random.randint(10000, 99999)

# Create your models here.

class TipoEntidad(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    tipo_entidad = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=250)
    ultima_actualizacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s : %s"%(self.tipo_entidad,self.descripcion)

class Entidad(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    codigo_ent = models.PositiveIntegerField(default = random_string,null=False)
    nombre = models.CharField(max_length=200,unique=True,null=False)
    dir_calle = models.CharField(max_length=50,null=False)
    dir_numero = models.CharField(max_length=10,null=False)
    dir_int = models.CharField(max_length=6)
    dir_colonia = models.CharField(max_length=50,null=False)
    dir_ciudad = models.CharField(max_length=50,null=False)
    dir_estado = models.CharField(max_length=50,null=False)
    dir_pais = models.CharField(max_length=25,null=False)
    dir_cp = models.CharField(max_length=10,null=False)
    tipo_entidad = models.ForeignKey(TipoEntidad, on_delete=models.DO_NOTHING, null=False, blank=False)
    representante = models.CharField(max_length=50,null=False)
    mision = models.CharField(max_length=500)
    
    def __str__(self):
        return "%s : %s"%(self.nombre,self.codigo_ent)

class TipoContacto(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    tipo_contacto = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=250)
    ultima_actualizacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s : %s"%(self.tipo_contacto,self.descripcion)
    
class Contacto(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    nombre_contacto = models.CharField(max_length=50,null=False)
    contacto = models.CharField(max_length=50,null=False)
    tipo_contacto = models.ForeignKey(TipoContacto, on_delete=models.DO_NOTHING, null=False, blank=False)
    entidad = models.ForeignKey(Entidad, on_delete=models.DO_NOTHING, null=False, blank=False)

    def __str__(self):
        return "%s : %s - %s"%(self.entidad,self.nombre_contacto,self.tipo_contacto)

