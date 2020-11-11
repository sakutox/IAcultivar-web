from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class CultivoViewSet(viewsets.ModelViewSet):
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()

class EnfermedadViewSet(viewsets.ModelViewSet):
    serializer_class = EnfermedadSerializer
    queryset = Enfermedad.objects.all()

class TratamientoViewSet(viewsets.ModelViewSet):
    serializer_class = TratamientoSerializer
    queryset = Tratamiento.objects.all()

class PasosTratamientoViewSet(viewsets.ModelViewSet):
    serializer_class = PasosTratamientoSerializer
    queryset = PasosTratamiento.objects.all()

class ImagenCultivoViewSet(viewsets.ModelViewSet):
    serializer_class = ImagenCultivoSerializer
    queryset = TablaImagenCultivo.objects.all()

class ImagenEnfermedadViewSet(viewsets.ModelViewSet):
    serializer_class = ImagenEnfermedadSerializer
    queryset = TablaImagenEnfermedad.objects.all()

class ImagenTratamientoViewSet(viewsets.ModelViewSet):
    serializer_class = ImagenTratamientoSerializer
    queryset = TablaImagenTratamiento.objects.all()

class UsuarioForoViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioForoSerializer
    queryset = UsuarioForo.objects.all()

class PreguntaForoViewSet(viewsets.ModelViewSet):
    serializer_class = PreguntaForoSerializer
    queryset = PreguntaForo.objects.all()

class RespuestaForoViewSet(viewsets.ModelViewSet):
    serializer_class = RespuestaForoSerializer
    queryset = RespuestaForo.objects.all()

class SugerenciaForoViewSet(viewsets.ModelViewSet):
    serializer_class = SugerenciaSerializer
    queryset = Sugerencia.objects.all()

class ImagenEnfermedadCultivoViewSet(viewsets.ModelViewSet):
    serializer_class = ImagenEnfermedadCultivoSerializer
    queryset = TablaImagenEnfermedadCultivo.objects.all()

class CultivoPreguntaViewSet(viewsets.ModelViewSet):
    serializer_class = CultivoPreguntaSerializer
    queryset = CultivoPregunta.objects.all()

class EnfermedadPreguntaViewSet(viewsets.ModelViewSet):
    serializer_class = EnfermedadPreguntaSerializer
    queryset = EnfermedadPregunta.objects.all()

class TratamientoPreguntaViewSet(viewsets.ModelViewSet):
    serializer_class = TratamientoPreguntaSerializer
    queryset = TratamientoPregunta.objects.all()

class EnfermedadCultivoViewSet(viewsets.ModelViewSet):
    queryset = EnfermedadCultivo.objects.all()
    serializer_class = EnfermedadCultivoSerializer
    

class RangoViewSet(viewsets.ModelViewSet):
    serializer_class = RangoSerializer
    queryset = Rango.objects.all()

class TipoTratamientoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoTratamientoSerializer
    queryset = TipoTratamiento.objects.all()

class DanosEnfermedadCultivoViewSet(viewsets.ModelViewSet):
    serializer_class = DanosEnfermedadCultivoSerializer
    queryset = DanosEnfermedadCultivo.objects.all()