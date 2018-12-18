# Despliegue con Docker

## Creación de workwaitqueue-docker
Lo primero que hay que hacer es [crear una nueva applicación](https://github.com/adriordi/proyectoIV/blob/master/docs/DespliegueHeroku.md) en Heroku como hicimos en el hito anterior, en este caso, la he creado desde el propio navegador llamándola **workwaitqueue-docker**.

## Creación de heroku.yml
Una vez creada la applicación, debemos crear un archivo **heroku.yml** en la raíz de nuestro proyecto. Para ello vamos hacer uso del plugin "heroku-manifest", siguiendo estos pasos:

* Actualizamos nuestro cli de heroku a la beta e instalamos el plugin.
~~~~
$ heroku update beta
$ heroku plugins:install @heroku-cli/plugin-manifest
~~~~

* Creamos el manifiesto de nuestra applicación.
~~~~
$ heroku manifest:create
~~~~

* Subimos los cambios a GitHub.
~~~~
$ git add heroku.yml
$ git commit -m "Add heroku.yml"
~~~~

* Cambiamos la pila de heroku.
~~~~
$ heroku stack:set container
~~~~

* Pusheamos nuestra applicación a Heroku.
~~~~
$ git push heroku master
~~~~

[Enlace a mi heroku.yml](https://github.com/adriordi/proyectoIV/blob/master/heroku.yml).

Toda la documentación que he seguido para realizar este apartado se en cuentra [aquí](https://devcenter.heroku.com/articles/buildpack-builds-heroku-yml#getting-started-existing-app)

## Despliegue del contenedor

Para el despliegue del contenedor nos hace falta un archivo Dockerfile, [enlace al mio](https://github.com/adriordi/proyectoIV/blob/master/Dockerfile), el cual cree basándome en el que encontre en la [documentación ofical de docker](https://docs.docker.com/get-started/part2/#dockerfile).

Una vez creado, seguí paso a paso la [documentación oficial de Heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime#dockerfile-commands-and-runtime):

* Logeo en Container Registry:
~~~~
$ heroku login
$ heroku container:login
~~~~

* Buildeo de la imagen y push al Container Registry:
~~~~
$ heroku container:push web
~~~~

* Release de la imagen:
~~~~
$ heroku container:release web
~~~~

* Por último para el despliegue:
~~~~
$ heroku git:remote -a workwaitqueue-docker
$ git push heroku master
~~~~

Toda la documentacion del despliegue con docker se puede encontrar [aqui](https://workwaitqueue-docker.herokuapp.com/doc) 