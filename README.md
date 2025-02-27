# Little Bastard
"Little Bastard" es una herramienta de control remoto (RAT) desarrollada en Python 🐍, diseñada para permitir la ejecución de comandos de forma remota en un sistema comprometido. Consiste en dos partes: un servidor que corre en la máquina atacante y un cliente que se ejecuta en la máquina víctima. El servidor envía comandos al cliente, y este ejecuta tareas como explorar directorios, ejecutar programas, o descargar archivos 📂. Es una demostración educativa de cómo funcionan este tipo de herramientas, y tiene medidas para gestionar las conexiones de forma segura 🔒.

Explicación Técnica:

"Little Bastard" es un RAT (Remote Access Trojan) escrito en Python, que consta de un servidor y un cliente. El servidor escucha en una IP y puerto determinados, esperando una conexión entrante del cliente, que se ejecuta en la máquina víctima. La comunicación se establece mediante sockets TCP, donde el servidor envía comandos al cliente, y este ejecuta diversas tareas:

Comandos básicos: El servidor puede ejecutar comandos como cambiar directorios (cd) 🗂️, listar directorios (dir o ls) 📑, iniciar procesos (start) 🖥️, y descargar archivos desde la máquina víctima (download) 📥.
Recepción de resultados: Los resultados de los comandos se envían de vuelta al servidor, donde se muestran al atacante 👨‍💻. Esto incluye la salida de los comandos ejecutados, los errores 🚫, o el contenido de los archivos solicitados.
Codificación de datos: La transferencia de archivos entre el servidor y el cliente se realiza mediante codificación Base64 🔐 para asegurar que los datos binarios puedan ser transmitidos correctamente a través de la red 🌐.
Conexiones seguras: El cliente está diseñado para intentar reconectar automáticamente 🔄 si la conexión con el servidor se interrumpe.
Este RAT no debe ser utilizado con fines maliciosos ⚠️, ya que se proporciona únicamente como una demostración educativa para comprender cómo funcionan las herramientas de control remoto.


<img width="710" alt="Captura" src="https://github.com/user-attachments/assets/bbeab1d0-29b1-4ee8-9714-162c6daba31e" />


