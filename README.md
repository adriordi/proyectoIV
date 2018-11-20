# WorkWaitQueue
Ver [página del proyecto](https://adriordi.github.io/proyectoIV/)

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/adriordi/proyectoIV.svg?branch=master)](https://travis-ci.org/adriordi/proyectoIV)

# Descripción
Proyecto para la asignatura "Infraestructura Virtual" de la Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación.
El proyecto se basa en una cola de trabajos para mantener el orden y prioridad sobre trabajos que se manden a una plataforma. Los trabajos son comandos de shell que se podrán ejecutar remotamente en el servidor con orden de llegada manteniendo la prioridad de estos.

# Herramientas
Las herramientas y servicios para desarrollar y desplegar el proyecto serán:

* [Python](https://www.python.org/); como principal lenguaje de programación.
* [hug](http://www.hug.rest/); como framework para desarrollar la API.
* [unittest](https://docs.python.org/3/library/unittest.html); como framework para los test unitarios.
* [Docker](https://www.docker.com/), [Heroku](https://www.heroku.com/) y [Travis-CI](https://travis-ci.org); para la integración, despliege y contenerización.
* [Elasticsearch](https://www.elastic.co/); para la base de datos. 

# Descripción de la clase
Ahora mismo cuento con una clase sencilla llamada ("Workwaitqueue")[TODO: añadir enlace al src/mainWWQ.py]. La clase contiene métodos para saber el estado de la cola, la cantidad de trabajos que contiene y poder añadir o eliminar trabajos con una prioridad determinada.

# Integración Continua
Para la integración continua he elegido el servicio que ofrece [Travis-CI](https://travis-ci.org) que una vez conectado a este repositorio, modificamos el archivo de configuración para que pase los test y realice la construcción y el despliege del proyecto.


# Instalación
Hacer fork al repositorio y una vez situado en la raíz del  directorio realizar el siguiente comando:

~~~~
make install
~~~~

# Lanzar tests
Para comprobar los resultados de los test ejecutar la siguiente orden sobre la raíz del directorio:

~~~~
make test
~~~~

# Lanzar programa
El programa se ejecuta con el siguiente comando:

~~~~
python3 src/mainWWQ.py
~~~~

# Despliegue en Heroku
Los pasos que he seguido para realizar el [despliegue](https://workwaitqueue.herokuapp.com) de mi proyecto en Heroku se puede leer en: [Despligue en Heroku](./docs/DespliegueHeroku.md).

Toda la documentación sobre la api, que proporciona el propio hug, la puedes encontrar [aquí](https://workwaitqueue.herokuapp.com/documentation).

