# WorkWaitQueue
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/adriordi/proyectoIV.svg?branch=master)](https://travis-ci.org/adriordi/proyectoIV)

# Descripción
Proyecto para la asignatura "Infraestructura Virtual" de la Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación.
El proyecto se basa en una cola de trabajos para mantener el orden y prioridad sobre trabajos que se manden a una plataforma. Los trabajos son comandos de shell que se podrán ejecutar remotamente en el servidor con orden de llegada manteniendo la prioridad de estos.

# Herramientas
* [Python](https://www.python.org/); como principal lenguaje de programación.
* [hug](http://www.hug.rest/); como framework para desarrollar la API.
* [unittest](https://docs.python.org/3/library/unittest.html); como framework para los test unitarios.
* [Docker](https://www.docker.com/), [Heroku](https://www.heroku.com/) y [Travis-CI](https://travis-ci.org); para la integración, despliege y contenerización.
* [Elasticsearch](https://www.elastic.co/); para la base de datos. 

# Descripción de la clase
Ahora mismo cuento con una clase sencilla llamada [Workwaitqueue](https://github.com/adriordi/proyectoIV/blob/master/src/mainWWQ.py). La clase contiene métodos para saber el estado de la cola, la cantidad de trabajos que contiene y poder añadir o eliminar trabajos con una prioridad determinada.

# Integración Continua
Para la integración continua se usará [Travis-CI](https://travis-ci.org) que una vez conectado a este repositorio, modificamos el archivo de configuración para que pase los test y realice la construcción y el despliege del proyecto.


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

Se puede comprobar el funcionamiento realizando las siguientes operaciones:

* Obtener el número de trabajos de la cola: [/works](https://workwaitqueue.herokuapp.com/works)

* Añadir un trabajo a la cola: [/add_work](https://workwaitqueue.herokuapp.com/add_work)
> Para ver la funcionalidad de este método de la api se debe de hacer con un curl desde terminal ya que desde navegador no se nos permite hacer un PUT.
~~~~
curl -X PUT https://workwaitqueue.herokuapp.com/add_work
~~~~

* Saber si la cola está vacía o no: [/empty](https://workwaitqueue.herokuapp.com/empty)
> En el apartado data nos dice a través de un booleano si la cola está vacía (TRUE) o no (FALSE). 

# Despliege con docker
Enlace al [contenedor en DockerHub](https://hub.docker.com/r/radidiaz/work_wait_queue/)