# SQL-patrones

Se crea una base de datos y se llena de datos con firstname, lastname, username, email y password.
Descargamos el repositorio y luego se descomprime, abrimos la terminal y nos ubicamos en la ruta donde se encuentra el codigo, antes tenemos que tener el programa Docker. cuando ya estemos en la ruta
donde se encuentra el codigo ejecutamos el comando de docker: 
```
docker build --tag=Nombre
```
_Corremos la aplicacion con el comando_

```
docker run -r 4000:80 nombre
```
despues abrimos nuestro navegador y en la direccion colocamos http://localhost:4000

_Se presentaran 2 botones, el primero que mostrara la lista de la base de datos y el 2 el cual retorna un Json_
