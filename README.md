
![Sin título-1](https://user-images.githubusercontent.com/84250823/139501999-35b1a740-1975-45af-813c-72653f564bcf.jpg)

 
 <p align="center" style="background-color:white">
 <a href="![logo](https://user-images.githubusercontent.com/84250823/136850833-c994078c-cea3-40b7-b725-9f794ea3e130.jpg)" rel="noopener">
 <img src="https://user-images.githubusercontent.com/84250823/136850833-c994078c-cea3-40b7-b725-9f794ea3e130.jpg" alt="RAVN logo"></a>
</p>

<p align="center" style="background-color:white; font-size:"40px"> PROYECTO BACKEND RKG </p>
 
## E-commerce de mascotas - Tienda de mascotas y apartado de adopciones
 
AUTORES 💻 :

>  _Kevin More_ 😎
                                                                 
![2giphy](https://user-images.githubusercontent.com/84250823/139501774-37575b6b-0578-46cd-9cdd-c2fbfe4f240d.gif)

>  _Renzo Estrada_ 😎

![1giphy](https://user-images.githubusercontent.com/84250823/139501690-52b857e9-6c00-4fac-b215-54c64cce4c83.gif)
 
>  _Guillermo Mujica_ 😎
                                                                 
![3giphy](https://user-images.githubusercontent.com/84250823/139501883-e5778b5c-e810-43f4-9709-5e4bec168582.gif)

### Idea del proyecto 😼:
La idea principal es tener un ecommerce enfocado a las
mascotas, respecto a las ideas secundarias estarían enfocadas a un apartado de adopciones y donaciones a centro de rescate de mascotas

#### Soluciones:
> Agilizar el proceso de compras
> Difundir la concientización de adopción de animales
> Incentivar a las personas a apoyar en los refugios de animales

#### Tecnologías:
>Base de datos: postgres
<img src="https://img.icons8.com/color/48/000000/postgreesql.png"/>
                                                                 
>Frameworks : Django
<img src="https://img.icons8.com/color/48/000000/django.png"/>
                                                            
>Editor de código: VisualCode
<img src="https://img.icons8.com/color/48/000000/visual-studio-code-2019.png"/>
                                                                             
>Lector de base de datos : DataGrip
<img src="https://img.icons8.com/color/48/000000/pixel-cat.png"/>
                                                                                                                                                       
>Repositorio : GitHub
<img src="https://img.icons8.com/color-glass/48/000000/github.png"/>
                                                                  
>Tester: Postman
<img src="https://img.icons8.com/dusk/64/000000/postman-api.png"/>
                                                                
>Diagramador del MER: MySQL WorkBench
<img src="https://img.icons8.com/color/48/000000/mysql-logo.png"/>
                                                                
>Canal de comunicación: Discord, Whatsapp, llamadas telefónicas
>
# Instrucciones

1. Para navegar en el proyecto descargarte el repositorio mediante el siguiente comando:

```
git clone https://github.com/kevinmore26/RKG-BACK
```

2. Una vez que haya descargado, ahora, tendrás que ingresar a la carpeta `RKG-BACK\` y  entrar a la rama `main` (estará por defecto)

3. Instalamos los requirements.txt para el correcto funcionamiento
```
pip install -r requirements.txt
```

4. Procede con el siguiente comando para crear las migraciones(en el caso de haber migraciones, eliminarlas, ya que usted no las tiene en una base de datos, lanzandole error)
```
python manage.py makemigrations gestion --name <nombre_migracion>
```

>  No es necesario entrar a una carpeta para encontrar el manage.py ya que se encuentra afuera para una mejor organización por tema de tener varias apps (facturacion,gestion...)

5. Creamos una DATABASE con el siguiente nombre: `django_rkg_revenge\`

6. Seguido del siguiente comando para ejecutar las migraciones
```
python manage.py migrate gestion
```
7.Ejecutamos el servidor 
```
python manage.py runserver
```
8. Listo

![44giphy](https://user-images.githubusercontent.com/84250823/139502617-6d5c9d7c-0243-4641-9e72-c56318cf561d.gif)



