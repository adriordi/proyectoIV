# WorkWaitQueue
Ver [página del proyecto](https://adriordi.github.io/proyectoIV/)

Contenedor: https://workwaitqueue-docker.herokuapp.com

Despliegue final: [35.204.69.190](http://35.204.69.190/)



<img src="https://cloud.google.com/_static/be157a52c2/images/cloud/cloud-logo.svg" width="180">
[![](https://www.herokucdn.com/deploy/button.svg)](https://workwaitqueue.herokuapp.com/)
[![](https://cdn.rawgit.com/play-with-docker/stacks/cff22438/assets/images/button.png)](https://workwaitqueue-docker.herokuapp.com/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/adriordi/proyectoIV.svg?branch=master)](https://travis-ci.org/adriordi/proyectoIV)


# Enlaces
[Instalación](https://github.com/adriordi/proyectoIV/blob/master/docs/Instalacion.md)

[Despliegue en Heroku](https://github.com/adriordi/proyectoIV/blob/master/docs/Herokudocs.md)

[Despliegue con Docker](https://github.com/adriordi/proyectoIV/blob/master/docs/DespliegueDocker.md)

[Enlace al contenedor de DockerHub](https://hub.docker.com/r/radidiaz/proyectoiv/)

[Despliegue en IaaS](https://github.com/adriordi/proyectoIV/blob/master/docs/DespliegueIaaS.md)


# Descripción
Proyecto para la asignatura "Infraestructura Virtual" de la Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación.
El proyecto se basa en una cola de trabajos para mantener el orden y prioridad sobre trabajos que se manden a una plataforma. Los trabajos son comandos de shell que se podrán ejecutar remotamente en el servidor con orden de llegada manteniendo la prioridad de estos.

# Herramientas
* [Python](https://www.python.org/); como principal lenguaje de programación.
* [hug](http://www.hug.rest/); como framework para desarrollar la API.
* [unittest](https://docs.python.org/3/library/unittest.html); como framework para los test unitarios.
* [Docker](https://www.docker.com/), [Heroku](https://www.heroku.com/) y [Travis-CI](https://travis-ci.org); para la integración, despliege y contenerización.
 

# Descripción de la clase
Ahora mismo cuento con una clase sencilla llamada [Workwaitqueue](https://github.com/adriordi/proyectoIV/blob/master/src/mainWWQ.py). La clase contiene métodos para saber el estado de la cola, la cantidad de trabajos que contiene y poder añadir o eliminar trabajos con una prioridad determinada.

# Integración Continua
Para la integración continua se usará [Travis-CI](https://travis-ci.org) que una vez conectado a este repositorio, modificamos el archivo de configuración para que pase los test y realice la construcción y el despliege del proyecto.

