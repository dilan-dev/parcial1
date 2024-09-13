"""
URL configuration for MiGestorEventos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from eventos.views import ver_eventos, crear_evento, index, OrganizadorListView, OrganizadorCreateView, loginPanel, logoutUser, editar_evento

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("vereventos/", ver_eventos, name="ver_eventos"),
    path("crearevento/", crear_evento, name='crear_evento'),
    path("organizadores/", OrganizadorListView.as_view(), name='organizador-list'),
    path("organizadores/nuevo/", OrganizadorCreateView.as_view(), name='organizador-create'),
    path("loginpage/", loginPanel, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('editar-evento/<int:id>/', editar_evento, name='editar_evento'),
]
