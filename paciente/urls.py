from django.conf.urls import url
from paciente import views


urlpatterns = [
    url(r'^$', views.inicio_paci, name='paciente'),    
]
