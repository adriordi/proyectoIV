from fabric import Connection
from fabric import task

@task
def install_app(ctx):
    "Clona el repositorio e instala las dependencias"
    run('rm -rf proyectoIV')
    run('git clone https://github.com/adriordi/proyectoIV.git')
    run('cd proyectoIV && make install')

def start_app():
    "Inicia la aplicación"
    run('cd proyectoIV && sudo gunicorn app:__hug_wsgi__ -b 0.0.0.0:80')
