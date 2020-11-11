from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cultivo)
admin.site.register(Enfermedad)
admin.site.register(Tratamiento)
admin.site.register(PasosTratamiento)
admin.site.register(TablaImagenCultivo)
admin.site.register(TablaImagenEnfermedad)
admin.site.register(TablaImagenTratamiento)
admin.site.register(UsuarioForo)
admin.site.register(PreguntaForo)
admin.site.register(RespuestaForo)
admin.site.register(Sugerencia)
admin.site.register(TablaImagenEnfermedadCultivo)
admin.site.register(CultivoPregunta)
admin.site.register(EnfermedadPregunta)
admin.site.register(TratamientoPregunta)
admin.site.register(EnfermedadCultivo)
admin.site.register(Rango)
admin.site.register(TipoTratamiento)
admin.site.register(DanosEnfermedadCultivo)


