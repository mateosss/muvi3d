# Muestras MuVi3D 2021

Este repositorio está relacionado al proyecto de compromiso social
[MuVi3D](https://www.instagram.com/muvi3d.cse/). El proyecto se basa mayormente
en el escaneo 3D de muestras de museos para que sean de fácil acceso por la
sociedad. En esta tarea surgen varios puntos que podrían beneficiarse de la
automatización y el conocimiento en programación, web y 3D de los participantes.

Este repositorio es por ahora un simple script que permite listar y visualizar
muestras en la web, accesible en <https://mateosss.github.io/muvi3d>. Se listan
más abajo algunos proyectos relacionados a la parte técnica que estaría bueno
encarar para mejorar a MuVi3D en general.

# Proyectos

Acá se definen algunos objetivos autocontenidos con los que estaría bueno
mejorar el proyecto.

## Integrar Interfaz Web

Uno de los organizadores del proyecto hizo una diseño para interfaz web
preliminar que puede accederse desde [acá](http://muvi3d.000webhostapp.com/). La
página está hecha exclusivamente con HTML/CSS/JS y estaría bueno integrarla con
este repositorio para que pueda generarse automáticamente.

## Optimización de los Modelos (LOD)

Actualmente solo se tiene acceso a los modelos generados con resolución
completa. Estos son muy pesados (entre ~500K y ~1M de vértices) y se dificulta
verlos en computadoras/celulares con poca capacidad de cómputo. Estaría bueno,
dada una muestra, generar automáticamente modelos más sencillos con distintos
[níveles de detalle](https://es.wikipedia.org/wiki/Nivel_de_detalle_(LOD)). Esto
es, modelos con menor cantidad de polígonos y texturas de menor resolución.

## Optimización de los Modelos (Normal Map)

Otra optimización posterior a la del LOD, es la de bakear automáticamente un
mapa de normales para las muestras. El primer minuto de [este
video](https://www.youtube.com/watch?v=0r-cGjVKvGw) explica qué es esto y luego
procede a explicar como hacerlo en Blender. Esto hace que se puedan mantener una
buena calidad de detalles de la superficie de las muestras en los modelos
optimizados dados por el LOD, haciendo que incluso en celulares las muestras se
vean muy bien.

## Realidad Aumentada

El visor de modelos en uso es <https://modelviewer.dev/> y por defecto tiene
funcionalidades de [realidad aumentada][modelviewer-ar] que deshabilité por que
los modelos son demasiado grandes para que funcionen en celulares. Estaría bueno
reactivarla una vez que algunas de las optimizaciones de los modelos estén
funcionando. Más adelante se pensaba en realizar una muestra con esta
característica virtual en los museoss como un evento.

[modelviewer-ar]: https://youtu.be/Sy6FgYWJqcA?t=451

## Mejorar el Visor 3D

Model viewer ofrece un editor <https://modelviewer.dev/editor/> muy bueno que no
solo permite editar cosas como los HDRIs y la exposure sino que también permite
agregar "hotspots" que son puntos 3D del modelo con anotaciones, eso puede ser
muy útil. Estaría bueno que de alguna forma se le permita a los que suben las
muestras editar estas cosas, ya sea usando el mismo
[editor][https://modelviewer.dev/editor/] de modelviewer y copiando y pegando el
texto que genera o directamente en el visor.

## Chequeador de Datos Recolectados

Para poder automatizar muchos de estos procesos es necesario que las muestras de
entradas que los alumnos generan estén bien formateadas, con estructuras de
carpetas y nombres adecuados. Sería muy útil poder brindarle a los estudiantes
que participen de la toma de muestras un programa que les permita verificar si
dejaron en la carpeta las cosas con el formato adecuado.

## Mejoras de la Web

Sería genial poner más trabajo en mejorar la página web, tanto en diseño como en
características. Este no es un proyecto muy definido pero si surge cualquier
idea por favor planteala!

# Como Usar

Este repositorio usa git lfs para guardar los archivos binarios (glbs y jpgs
principalmente). Para poder actualizar las páginas hay que [instalar git
lfs][git-lfs]. Si clonaste el repo antes de instalar git lfs, hace `git lfs
install` en la carpeta del repo.

Para actualizar la lista simplemente agregar los archivos glbs al directorio
`glbs/` y correr `./make.py` que va a regenerar tanto `index.html` como las
`pages/` necesarias.

[git-lfs]: https://git-lfs.github.com/
