# Despliegue en Heroku

Para poder desplegar mi applicación en Heroku seguí los pasos que se pueden leer en [su documentación](https://devcenter.heroku.com/articles/heroku-cli) además de crear el archivo Procfile.

Mi despliegue fue siguiendo los siguientes pasos:

* Instalación

~~~~
curl https://cli-assets.heroku.com/install.sh | sh
yay -S heroku-cli
heroku --version
~~~~

* Login 

~~~~
heroku login
~~~~

* Generación del token

~~~~
heroku auth:token
travis encrypt $(heroku auth:token) --add deploy.api_key
~~~~

* Creación de la applicación y enlace con github

~~~~
heroku create
heroku git:remote -a workwaitqueue
~~~~

* Push de mi applicación a Heroku

~~~~
git push heroku master
~~~~

