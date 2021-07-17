# Muestras MuVi3D 2021

Las muestras se encuentran en este link <https://mateosss.github.io/muvi3d>

# Como Usar

Este repositorio usa git lfs para guardar los archivos binarios (glbs y jpgs
principalmente). Para poder actualizar las páginas hay que [instalar git
lfs][git-lfs]. Si clonaste el repo antes de instalar git lfs, hace `git lfs
install` en la carpeta del repo.

Para actualizar la lista simplemente agregar los archivos glbs al directorio
`glbs/` y correr `./make.py` que va a regenerar tanto `index.html` como las
`pages/` necesarias.

[git-lfs]: https://git-lfs.github.com/
# A Mejorar

## Realidad Aumentada

El visor de modelos es https://modelviewer.dev/ y por defecto tiene
funcionalidades de [realidad aumentada][modelviewer-ar] que deshabilité por que
los modelos son demasiado grandes para que funcionen en celulares. No debería
ser *muy* difícil hacer un script que use Blender para hacer un modelo low poly
del escaneo (con menos de 10k de triangulos) y que genere un normal map de la
geometría. Estaría bueno que para visualizar se use la versión low poly ya que
total se ve muy similar al ojo y las versiones en full resolución ya estarían
almacenadas.

[modelviewer-ar]: https://youtu.be/Sy6FgYWJqcA?t=451

## Acceso a Todos los Samples

Sería genial que todos los datos recolectados durante el proyecto queden
disponibles en la web (videos, fotos, texturas, archivos de proyecto, etc).

## Mejorar el Visor

Model viewer ofrece un editor https://modelviewer.dev/editor/ muy bueno que no
solo permite editar cosas como los HDRIs y la exposure sino que también permite
agregar "hotspots" que son puntos 3D del modelo con anotaciones, eso puede ser
muy útil. Estaría bueno que de alguna forma se le permita a los que suben las
muestras editar estas cosas, ya sea usando el mismo
[editor][https://modelviewer.dev/editor/] de modelviewer y copiando y pegando el
texto que genera o directamente en el visor.
