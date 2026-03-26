Bruteforce.

Cómo ejecutar el programa.

Se guarda el código en un archivo llamado bruteforce.py.
Se abre la terminal en Visual Code con Ctrl + J y se navega en la carpeta en donde se guardo el archivo bruteforce.py, con cd /ruta/a/tu/carpeta.
Y por ultimo se coloca: python bruteforce.py 

Ejemplos de salida.

Contraseña encontrada: abcd

Intentos: 9005082

Tiempo: 1.0167505741119385

Intentos totales: 9005082

Reflexión: ¿qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?

Si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos, el número de combinaciones aumenta, haciendo que el bruteforce tarde demasiado, demostrando la importancia del uso de contraseñas seguras.

Grafica 

Adicionalmente se realizó una gráfica que muestra el crecimiento exponencial del número de combinaciones en un ataque de fuerza bruta.

La gráfica se basa en la fórmula de: 

combinaciones = alfabeto ^ longitud

Gracias a esto se puede demostrar que al aumentar la longitud de la contraseña, el número de intentos crece de forma exponencial.
