from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    ##############################################
    ####### URLS PARA EDUCACION FINANCIERA #######
    ##############################################
    path('educacion/', include('Aplicaciones.Educacion.urls')),  
    path('auth/', include('social_django.urls', namespace='social')),
    ####################################################################
    ####### URLS PARA ADMINISTRAR MODULO DE EDUCACION FINANCIERA #######
    ####################################################################
    path('administrarEducacion/', include('Aplicaciones.AdministrarEducacion.urls')),  
    ###########################################################
    ############## URLS PARA ADMINITRAR CONTENIDOS#############
    ###########################################################
    path('AdministrarContenido/', include('Aplicaciones.AdministrarContenido.urls')),
    #########################################################
    ############## URLS RUMBO A LA AUTENTICACION#############
    #########################################################
    path('autenticacion/', include('Aplicaciones.Autenticacion.urls')),  
    ############################################################
    ############## URLS RUMBO A LA PAGINA PRINCIPAL#############
    ############################################################
    path('', include('Aplicaciones.Contenido.urls')),  


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)