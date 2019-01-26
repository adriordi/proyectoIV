from fabric import *
from fabric.api import *
from fabric.network import ssh


def Instalar():
    "Clona el repositorio e instala las dependencias"
    run('sudo rm -rf proyectoIV')
    run('git clone https://github.com/adriordi/proyectoIV.git')
    run('cd proyectoIV && make install')

def Iniciar():
    "Inicia la aplicacion"
    run('cd proyectoIV/ && sudo gunicorn api_queue:__hug_wsgi__ -b 0.0.0.0:80')

def Parar(): 
    "Parar la ejecución matando el proceso"
    run('sudo kill -9 $(ps -A -o pid,cmd | grep gunicorn | head -n 1 | cut -d " " -f 1)')

def Actualizar():
    "Reinicia la aplicacion y vuelve a ejecutarla"
    Parar()
    Instalar()
    Iniciar()
