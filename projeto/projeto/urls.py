"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from agenda.views import UserViewSet, GroupViweSet, LocalViweSet, ConvidadoViweSet, CompromissoViweSet, Anotacao_CompromissoViweSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViweSet)
router.register('local', LocalViweSet)
router.register('convidado', ConvidadoViweSet)
router.register('compromisso', CompromissoViweSet)
router.register('Anotacao_Compromisso', Anotacao_CompromissoViweSet)

urlpatterns = [
    path('', include('agenda.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
