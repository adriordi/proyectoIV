# Despliegue con Docker

Al principio, para desplegar mi applicación con un contenedor, seguí los pasos de la [documentación de Docker](https://docs.docker.com/get-started/part2/#run-the-app), además de la [documentación de Heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime).

Una vez estaba desplegado, con la ayuda de [Rafa Leyva](https://github.com/rafaelleru/), nos dimos cuenta de que sería mejor tener un despliegue automático para minimizar las tareas cada vez que se genera una nueva versión. Estuvimos leyendo la [documentación que ofrece Travis para desplegar con dockers](https://docs.travis-ci.com/user/docker/), hasta que encontramos [este artículo](https://medium.com/@javierfernandes/continuous-deployment-con-docker-travis-heroku-c24042fb830b) que describía perfectamente lo que queríamos hacer.

# Pasos que seguí:

Necesitaremos tener una cuenta en dockerhub para poder ejecutar docker en travis y una cuenta en Heroku para crear una app y taggear la imagen buildeada, para a continuación pushear la imagen y ejecutar el Heroku release.

Debemos evitar escribir usuarios y passwords en .travis.yml, por lo que lo vamos añadir varias variables de ambiente, como usuario/password de dockerhub y heroku además de la api_key y app_name de nuestra aplicación a desplegar en heroku, definiéndolas en el apartado de "Environment Variables" de los ajustes de travis.

* Añadir en .travis.yml

~~~~
sudo: required

services:
  - docker
~~~~

Para poder ejecutar el comando "docker"


* Loggeo en dockerhub

~~~~
before_install:
  # login to docker registries (dockerhub + heroku)
  - echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
~~~~

* Buildear y pusheo de la imagen 

~~~~
- docker build -t "user_dockerhub"/"repo_dockerhub" .

deploy:
  provider: script
  script:
    # push to dockerhub
    docker push "user_dockerhub"/"repo_dockerhub";
  branch: master
~~~~

* Instalar heroku CLI y loggin al registry de Heroku

~~~~
# install heroku CLI
  - wget -qO- https://toolbelt.heroku.com/install.sh | sh
  - echo "$HEROKU_PASSWORD" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com
~~~~

* Generación de token para usar como HEROKU_PASSWORD

~~~~
heroku authorizations:create
~~~~

* Tag y push den deploy de la imagen

~~~~
- docker tag "user_dockerhub"/"repo_dockerhub" registry.heroku.com/$HEROKU_APP_NAME/web

....

docker push registry.heroku.com/$HEROKU_APP_NAME/web;
~~~~

* Release

~~~~
heroku container:release web --app $HEROKU_APP_NAME
~~~~


Al final nuestro archivo .travis.yml quedaría [así](https://github.com/adriordi/proyectoIV/.travis.yml)