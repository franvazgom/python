

|Comando|Acción|Tip Senior|
|-------|-------|-------|
|sudo apt update && sudo apt upgrade -y | Actualiza el SO | -- |
|ls -la|Lista archivos (incluyendo ocultos como .env).|Usa -h para ver tamaños en KB/MB.|
|cd ~|Te lleva a tu carpeta personal (home).|cd - te regresa a la carpeta anterior.|
|cd /mnt/c/Users/Francisco|Cambio de directorio MNT | -- |
|pwd|Muestra la ruta actual completa.|Útil para configurar rutas en scripts.|
|mkdir -p dir/sub|Crea carpetas anidadas de un solo golpe.|El -p evita errores si ya existe.|
|cp -r|Copia directorios completos.|Imprescindible para respaldar carpetas de código.|
|rm -rf|Borra carpetas y archivos recursivamente.|Peligro: No pide confirmación. Úsalo con cuidado.|
|ip addr show eth0| IP de tu Linux (útil si necesitas conectar apps externas). | |


|Comando|Acción|Contexto|
|-------|-------|-------|
|sudo|Ejecuta comandos como administrador.|Te pedirá tu contraseña de Linux.|
|top o htop|Monitor de procesos y RAM en tiempo real.|Instala htop (sudo apt install htop) es más visual.|
|"grep -r ""texto"" ."|Busca una cadena de texto dentro de archivos.|Ejemplo: grep -r "Hace" ./*.txt|
|chmod +x script.sh|Da permisos de ejecución a un archivo.|Necesario para tus scripts de despliegue.|
|chown user:group|Cambia el dueño de un archivo/carpeta.|Se usa mucho cuando Docker crea archivos con root.|
|history|Muestra los últimos comandos usados.|Usa `history|


|Atajo|Acción|
|-------|-------|
|Ctrl + C| Detiene el proceso actual (matar el servidor de React o Python que está corriendo).|
|Ctrl + L| Limpia la pantalla (equivalente a clear).|
|Ctrl + R| Búsqueda inversa. Empieza a escribir un comando que usaste ayer y Linux lo encontrará.|
|Ctrl + A / Ctrl + E| Salta al inicio o al final de la línea que estás escribiendo.|
|Ctrl + U| Borra toda la línea desde el cursor hacia atrás.|