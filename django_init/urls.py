from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from aplicaciones.principal.views import *
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'cultivos', CultivoViewSet)
router.register(r'enfermedades', EnfermedadViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'pasosTratamiento', PasosTratamientoViewSet)
router.register(r'imagenCultivo', ImagenCultivoViewSet)
router.register(r'imagenEnfermedad', ImagenEnfermedadViewSet)
router.register(r'imagenTratamiento', ImagenTratamientoViewSet)
router.register(r'usuarioForo', UsuarioForoViewSet)
router.register(r'preguntaForo', PreguntaForoViewSet)
router.register(r'respuestaForo', RespuestaForoViewSet)
router.register(r'sugerencia', SugerenciaForoViewSet)
router.register(r'imagenEnfermedadCultivo', ImagenEnfermedadCultivoViewSet)
router.register(r'cultivoPregunta', CultivoPreguntaViewSet)
router.register(r'enfermedadPregunta', EnfermedadPreguntaViewSet)
router.register(r'TratamientoPregunta', TratamientoPreguntaViewSet)
router.register(r'enfermedadCultivo', EnfermedadCultivoViewSet)
router.register(r'rango', RangoViewSet)
router.register(r'tipoTratamiento', TipoTratamientoViewSet)
router.register(r'danosEnfermedadCultivo', DanosEnfermedadCultivoViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

