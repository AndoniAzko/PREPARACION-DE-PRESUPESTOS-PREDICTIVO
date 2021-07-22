# PREPARACION-DE-PRESUPESTOS-PREDICTIVO
Este trabajo esta orientado al TFM de KSchool, con una finalidad de conseguir aplicarlo realmente en una empresa industrial. El objetivo ha sido crear un modelo predictivo para el cálculo de cilindros neumáticos a medida.

COMENZANDO

Hay que descargar en un zip todo el contenido del repositorio, el cual incluye los siguientes ficheros los cuales se deberían ejecutar en este orden:
- CALCULO PREDICTIVO DE CILINDROS ESPECIALES.docx: una memoria explicativa del proyecto, aquí se explica de forma sencilla lo que se ha hecho en el proyecto sin incluir ningún código. Leyendo este documento primero se entrenderá mejor lo que se hace en los siguientes.
- DATOS: incluye las tablas que se han utilizado para el proyecto.
- TFM KSCHOOL.ipynb: es el cuaderno de Jupyter que incluye todo el trabajo, incluye el código completo comentado para que se entienda lo que se ha hecho.
- FRONTEND.py: incluye el codigo del frontend de Streamlit
- finalized_model.sav : es el modelo que hemos generado.

PRE REQUISITOS

Para preparar el entorno solo hay que crear un entorno virtual de la siguiente manera:

- Instalar "pip" si no lo tenemos ya instalado: https://pip.pypa.io/en/latest/installation/
- Instalar la librería de entornos virtuales con el comando "pip install virtualenv".
- Crear un entorno virtual en la ruta que queramos con el comando "virtualenv .../nombrevenv"

Mas información de como crear un entorno virtual en el siguiente enlace: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/

Una vez que tengamos creado el entorno virtual vamos a instalar las librerías necesarias para ejecutar el proyecto. Para esto en el repositorio puedes encontar el fichero de texto "requeriments.txt". Una vez activado el entorno virtual hay que ejecutar el siguiente comando:

    (<env_name>)$ pip install -r path/to/requirements.txt
    
Con esto ya estaremos preparados para trabajar.

DESCARGA DEL REPOSITORIO Y DE LOS DATOS

Hay que descargar el contenido del repositorio y guardar el contenido en una misma carpeta. 

Para descargar los datos se han subido a drive, se requiere un permiso para acceder a ellos ya que son datos de una empresa privada. Los datos hay que guardarlos dentro de la carpeta creada anteriormente, en una subcarpeta que se le llamara "DATA".

Para descargar los datos se enviará un correo electronico a "aazkonobieta31@gmail.com" indicando el proposito de uso de los datos. Si este proposito se considera correcto se facilitará al correo remitente un link con el enlace de descarga.

FRONTEND PARA EL USUARIO

Se ha creado una interfaz del usuario para que cualquier persona pueda utilizar el programa creado. Para esto se ha utilizado "Streamlit". Para utilizar el frontend hay que ejecutar en la linea de comandos lo siguiente:

    streamlit run FRONTEND.py

El frontend es muy intuitivo, hay que elegir entre las opciones dadas para cada elemento y darle al boton calcular, el cual devolverá el precio del cilindro.


