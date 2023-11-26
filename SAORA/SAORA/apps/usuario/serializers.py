from rest_framework import serializers
from .models import Usuario, Afiliado

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' 

class AfiliadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afiliado
        fields = '__all__' 
