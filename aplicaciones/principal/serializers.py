from rest_framework import serializers
from .models import *

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = '__all__'


class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = '__all__'

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = '__all__'
        depth = 2

class PasosTratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasosTratamiento
        fields = '__all__'
        depth = 3


class ImagenCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaImagenCultivo
        fields = '__all__'
        depth = 3

class ImagenEnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaImagenEnfermedad
        fields = '__all__'
        depth = 3

class ImagenTratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaImagenTratamiento
        fields = '__all__'
        depth = 3

class UsuarioForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioForo
        fields = '__all__'
        depth = 3

class PreguntaForoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreguntaForo
        fields = '__all__'
        depth = 3
    
class RespuestaForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaForo
        fields = '__all__'
        depth = 3

class SugerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sugerencia
        fields = '__all__'
        depth = 3

class ImagenEnfermedadCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaImagenEnfermedadCultivo
        fields = '__all__'
        depth = 3

class CultivoPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultivoPregunta
        fields = '__all__'
        depth = 3

class EnfermedadPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnfermedadPregunta
        fields = '__all__'
        depth = 3

class TratamientoPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoPregunta
        fields = '__all__'
        depth = 3

class EnfermedadCultivoSerializer(serializers.ModelSerializer):
    cultivo = CultivoSerializer(read_only = True, many = True)
    enfermedad = EnfermedadSerializer(read_only = True, many = True)

    class Meta:
        model = EnfermedadCultivo
        fields = '__all__'
        depth = 1

class RangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rango
        fields = '__all__'
        depth = 3

class TipoTratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTratamiento
        fields = '__all__'
        depth = 3

class DanosEnfermedadCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanosEnfermedadCultivo
        fields = '__all__'
        depth = 3
