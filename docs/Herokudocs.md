# Despliegue en Heroku
Los pasos que he seguido para realizar el [despliegue](https://workwaitqueue.herokuapp.com) de mi proyecto en Heroku se puede leer en: [Despligue en Heroku](https://github.com/adriordi/proyectoIV/blob/master/docs/DespliegueHeroku.md).

Toda la documentación sobre la api, que proporciona el propio hug, la puedes encontrar [aquí](https://workwaitqueue.herokuapp.com/documentation).

Se puede comprobar el funcionamiento realizando las siguientes operaciones:

* Obtener el número de trabajos de la cola: [/works](https://workwaitqueue.herokuapp.com/works)
> Nos devuelve un entero en el cual nos dice el número de trabajos que hay actualmente en la cola.

* Añadir un trabajo a la cola: [/add_work](https://workwaitqueue.herokuapp.com/add_work)
> Para ver la funcionalidad de este método de la api se debe de hacer con un curl desde terminal ya que desde navegador no se nos permite hacer un PUT.
~~~~
curl -X PUT https://workwaitqueue.herokuapp.com/add_work
~~~~

* Eliminar un trabajo de la cola: [/del_work](https://workwaitqueue.herokuapp.com/del_work)
> Como pasa con el método anterior, para ver la funcionalidad tiene que ser desde consola ya que el navegador no nos lo permite.
~~~~
curl -X PUT https://workwaitqueue.herokuapp.com/del_work
~~~~

* Métodos para trabajos con prioridad:
** Obtener el número de trabajos con prioridad de la cola: [/priority_works](https://workwaitqueue.herokuapp.com/priority_works)

** Añadir un trabajo con prioridad a la cola: [/add_priority_work](https://workwaitqueue.herokuapp.com/add_priority_work)
~~~~
curl -X PUT https://workwaitqueue.herokuapp.com/add_priority_work
~~~~

** Eliminar un trabajo con prioridad de la cola: [/del_priority_work](https://workwaitqueue.herokuapp.com/del_priority_work)
~~~~
curl -X PUT https://workwaitqueue.herokuapp.com/del_priority_work
~~~~


* Saber si la cola está vacía o no: [/empty](https://workwaitqueue.herokuapp.com/empty)
> En el apartado data nos dice a través de un booleano si la cola está vacía (TRUE) o no (FALSE). 

Al final de [este documento](https://github.com/adriordi/proyectoIV/blob/master/docs/DespliegueHeroku.md) se puede ver un par de ejemplos de uso de la api.
