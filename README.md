# unittest-practice

## Instalar unittest

Para comprobar su funcionamiento se puede ejecutar l siguiente instrucción:

> python -m unittest -h

## Clase para agrupar pruebas

Se recomienda agrupar las pruebas en clases, a su vez, estas clases están en el paquete 'tests' en la raíz del proyecto, y la clase debe llamarse <<nombreClase>>TestCase

## Comandos para ejecutar pruebas

- Desde la raíz del proyecto, para ejecutar una prueva se utiliza el comando:

> python -m unittest tests/test_persona.py

- Correr las pruebas con mayor nivel de detalle en los mensajes: Para lograr esto se utiliza la instrucción:

> python -m unittest -v tests/test_persona.py

- Ejecutar todas las pruebas de la carpeta tests: Se realiza al ejecutar

> python -m unittest

- Listar las opciones de unittest: Para obtener la ayuda de unittest se ejecuta la siguiente instrucción:

> python -m unittest -h

## Métodos para ejecutar y verificar las pruebas

Los dos métodos principales para ejecutar las pruebas son:

- setUp(): Es un método que se llama antes de llamar los métodos con las pruebas, se utiliza para preparar los objetos que se utilizarán en el conjunto de pruebas. Por defecto, su implementación no realiza acción alguna.

- tearDown(): Es un método que se llama justo después de llamar la última instrucción en las pruebas y luego de guardar los resultados, y es generalmente utilizado para capturar las excepciones de los métodos con las pruebas para definir qué sucedió al ejecutarlas.

Los métodos utilizados para verificar las pruebas también se conocen como los métodos assert, los cuales permiten, al momento de correr las pruebas, verificar las condiciones que se establecen en el llamado al método, y en caso de que estas condiciones no se cumplan, se encargan de desencadenar o reportar los fallos.

A continuación, la lista de metodos assert: https://docs.python.org/3/library/unittest.html#assert-methods

## Generación de datos aleatorios

Para garantizar que las pruebas sean lo más exhaustivas posible, es recomendable utilizar generadores aleatorios de datos. Estos permiten probar los desarrollos con una variedad de valores, lo que ayuda a identificar errores que podrían no ser detectados con datos predefinidos. Se utilizará Faker, una librería de Python que genera valores aleatorios.

Para instalar Faker se usa la siguiente instrucción:

> pip install faker

## Cobertura de código con coverage.py

Coverage.py es una herramienta que permite identificar qué partes del se están ejecutando. Se utiliza comúnmente en pruebas unitarias para determinar qué porcentaje del código está cubierto por esas pruebas.

Para instalar Coverage.py, se debe ejecutar el siguiente comando en la terminal:

> pip install coverage

Para generar un informe de cobertura de código, se reemplaza la palabra "python" por "coverage run" en la línea de comando que se utiliza para ejecutar las pruebas. Por ejemplo, si la línea de comando para ejecutar las pruebas es la siguiente:

> python -m unittest tests/test_persona.py

Para verificar la cobertura de código se utiliza la siguiente instrucción:

> coverage run -m unittest tests/test_persona.py

La salida de las pruebas mostrará los mismos resultados que si se ejecutaran con el comando python. Sin embargo, después de ejecutar coverage, se puede generar un informe en pantalla con el porcentaje de código cubierto utilizando la siguiente instrucción:

> coverage report -m

Para ver el código que no está cubierto por las pruebas, primero es necesario borrar la información de la cobertura de las pruebas. Esto se puede hacer con la siguiente instrucción:

> coverage erase

Se ejecutan nuevamente las pruebas y, finalmente, se genera de nuevo el reporte con la instrucción:

> coverage report -m

Para visualizar la cobertura de código en un formato diferente al de la consola, se puede utilizar el comando:

> coverage html.

Este comando genera una carpeta llamada *htmlcov* con un archivo HTML para cada archivo de salida del reporte. Por ejemplo, el archivo htmlcov/Comunidad_persona_py.html corresponde a los resultados del reporte sobre Comunidad\persona.py.

Al abrir el archivo HTML, se puede observar la cobertura de la siguiente manera:

- A la izquierda, se muestran los números de línea de la clase o módulo.
- Frente a cada número de línea, se muestra una barra verde o roja.
- La barra verde indica que la línea de código se ejecutó durante las pruebas.
- La barra roja indica que la línea de código no se ejecutó.
- La línea de código se muestra a continuación de la barra.

En la parte superior del archivo HTML, se muestra la información general del archivo, así como el resumen de la cantidad de líneas que tiene, las ejecutadas y no ejecutadas, así como las excluidas.