from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Cultivo(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    nombreCientifico = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=10000)
    ambienteCrecimiento = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Enfermedad(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    nombreCientifico = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=10000)

    def __str__(self):
        return self.nombre

class EnfermedadCultivo(TimeStampedModel):
    cultivo = models.ForeignKey(Cultivo, related_name='cultivo', on_delete=models.CASCADE)
    enfermedad = models.ForeignKey(Enfermedad, related_name='enfermedad', on_delete=models.CASCADE)

    def __str__(self):
        return self.cultivo.nombre + " (" + self.enfermedad.nombre + ")"

class DanosEnfermedadCultivo(TimeStampedModel):
    enfermedadCultivo = models.ForeignKey(EnfermedadCultivo, on_delete=models.CASCADE)
    partePlanta = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=10000)

    def __str__(self):
        return self.enfermedadCultivo.cultivo.nombre + " (" + self.enfermedadCultivo.enfermedad.nombre + ")"

class TablaImagenEnfermedadCultivo(TimeStampedModel):
    danosEnfermedadCultivo = models.ForeignKey(DanosEnfermedadCultivo, on_delete=models.CASCADE)
    urlImagen = models.CharField(max_length=500)

    def __str__(self):
        return self.enfermedadCultivo

class TipoTratamiento(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre

class Rango(TimeStampedModel):
    rangoMinimo = models.IntegerField()
    rangoMaximo = models.IntegerField()
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tratamiento(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    tipoDeTratamiento = models.ForeignKey(TipoTratamiento, on_delete=models.CASCADE)
    enfermedadCultivo = models.ForeignKey(EnfermedadCultivo, on_delete=models.CASCADE)
    rango = models.ForeignKey(Rango, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class PasosTratamiento(TimeStampedModel):

    def cargar_imagen_cultivo(instance, filename):        
        if instance.pk:            
            old_instance = TablaImagenTratamiento.objects.get(pk=instance.pk)            
            old_instance.imagen.delete()        
        return 'pasosTratamiento/'+filename

    Tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    noPaso = models.CharField(max_length=10)
    titulo = models.CharField(max_length=200)
    descripción = models.CharField(max_length=1000)
    urlImagen = models.ImageField(        
        upload_to=cargar_imagen_cultivo, blank=True)

    def __str__(self):
        return self.titulo

class TablaImagenCultivo(TimeStampedModel):

    def cargar_imagen_cultivo(instance, filename):        
        if instance.pk:            
            old_instance = TablaImagenTratamiento.objects.get(pk=instance.pk)            
            old_instance.imagen.delete()        
        return 'cultivos/'+filename


    cultivo = models.ForeignKey(Cultivo,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    imagen = models.ImageField(        
        upload_to=cargar_imagen_cultivo, blank=True)
    
    
class TablaImagenEnfermedad(TimeStampedModel):

    def cargar_imagen_enfermedad(instance, filename):        
        if instance.pk:            
            old_instance = TablaImagenTratamiento.objects.get(pk=instance.pk)            
            old_instance.imagen.delete()        
        return 'enfermedades/'+filename

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    imagen = models.ImageField(        
        upload_to=cargar_imagen_enfermedad, blank=True)
    enfermedad = models.ForeignKey(Enfermedad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TablaImagenTratamiento(TimeStampedModel):

    def cargar_imagen_tratamiento(instance, filename):        
        if instance.pk:            
            old_instance = TablaImagenTratamiento.objects.get(pk=instance.pk)            
            old_instance.imagen.delete()        
        return 'tratamientos/'+filename
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    tratamiento = models.ForeignKey(Tratamiento,on_delete=models.CASCADE)
    imagen = models.ImageField(        
        upload_to=cargar_imagen_tratamiento, blank=True)

    def __str__(self):
        return self.nombre

class UsuarioForo(TimeStampedModel):
    nombre = models.CharField(max_length=300)
    contrasena = models.CharField(max_length=16)
    dedicacion = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class PreguntaForo(TimeStampedModel):
    titulo = models.CharField(max_length=200)
    cuerpo = models.CharField(max_length=500)
    apropiada = models.BooleanField(True)
    usuarioForo = models.ForeignKey(UsuarioForo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class RespuestaForo(TimeStampedModel):
    textoRespuesta = models.CharField(max_length=1000)
    apropiada = models.BooleanField(True)
    usuarioForo = models.ForeignKey(UsuarioForo, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(PreguntaForo, on_delete=models.CASCADE)

    def __str__(self):
        return self.textoRespuesta

class Sugerencia(TimeStampedModel):
    titulo = models.CharField(max_length=200)
    cuerpo = models.CharField(max_length=500)
    puntuacion = models.IntegerField()
    usuarioForo = models.ForeignKey(UsuarioForo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class CultivoPregunta(TimeStampedModel):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(PreguntaForo, on_delete=models.CASCADE)

    def __str__(self):
        return self.cultivo.nombre + " - " +self.pregunta.titulo

class EnfermedadPregunta(TimeStampedModel):
    pregunta = models.ForeignKey(PreguntaForo, on_delete=models.CASCADE)
    enfermedadCultivo = models.ForeignKey(EnfermedadCultivo, on_delete=models.CASCADE)

    def __str__(self):
        return self.enfermedadCultivo.cultivo.nombre + " (" + self.enfermedadCultivo.enfermedad.nombre + ")" + " - " + self.pregunta.titulo

class TratamientoPregunta(TimeStampedModel):
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(PreguntaForo, on_delete=models.CASCADE)

    def __str__(self):
        return self.tratamiento

