


|Comando|Descripción|
|-------|-------|
|wsl --list --online | Muestra las distribuciones disponibles para instalar.|
|wsl --list --verbose |Lista tus distros instaladas y qué versión de WSL usan (debe ser 2).|
|wsl --terminate <Distro> |"Apaga una instancia específica si se queda ""congelada""."|
|wsl --shutdown | Apaga todo el motor de WSL (útil para liberar RAM).|
|wsl --export <Distro> <Ruta.tar> | Crea un backup de tu entorno (hazlo antes de experimentos locos).|
|wsl -d <Distro> -u root |Entra a la distro como superusuario si olvidaste tu password.|
|wsl --install -d Ubuntu-24.04 | Instala Ubuntu versión 24.04 |
|wsl.exe -d Ubuntu-24.04 | Ejecuta una versión particular |

