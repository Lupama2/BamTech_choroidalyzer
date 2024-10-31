# Jugando con Choroidalyzer

## Introducción

El objetivo general es aprender sobre la herramienta Choroidalyzer. Contamos con dos objetivos particulares. En primer lugar, buscamos aprender a aplicar la herramienta sobre nuevos datos. En segundo lugar, identificar durante este aprendizaje el nicho en el cual se podría sumar valor a la herramienta.


## Setup

Se recomienda emplear un conda environment. Para crearlo y activarlo, ejecutar los siguientes comandos:

```
conda create -n choroidalyzer python=3.10

conda activate choroidalyzer
```

Luego, instalar las dependencias necesarias.

```
cd path/to/directory
conda env update --file environment.yml
```

Si se desea utilizar jupyter lab, instalarlo opcionalmente.
```
pip install jupyterlab
```

## Repo-structure

El repositorio cuenta de los siguientes archivos y carpetas:
. choroidalyze/ : contiene el código de la herramienta Choroidalyzer.
. data/ : contiene los datos sobre los que se aplica la herramienta. Nótese que estos datos no se guardan en el repositorio, gracias a que .gitignore incluye imágenes.
. examples/ : contiene ejemplos de uso de la herramienta.
. functions/ : contiene funciones que se utilizan para pre-procesar las imágenes y luego analizarlas
. main.ipynb : es el archivo principal del repositorio. Contiene el código que se ejecuta para aplicar la herramienta sobre los datos.


## Problemas conocidos

A continuación se desarrolla una lista de problemas conocidos:
. 