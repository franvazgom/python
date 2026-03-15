# Configuración inicial
```bash
git config --global user.name "Francisco Vazquez"
git config --global user.email "franvazgom@gmail.com"
git config --global color.ui auto
```
## Generación de llave -> keyGitHub 
```bash
ssh-keygen -t ed25519 -C "franvazgom@gmail.com"
```

## Crea la carpeta .ssh si no existe y mueve la llave 
```bash 
mkdir -p ~/.ssh
mv keyGitHub* ~/.ssh/
```

## Archivo config 
Cuando usas un nombre personalizado, SSH no sabe automáticamente que debe usar esa llave para GitHub. Para solucionar esto "para siempre", crea un archivo de configuración:
```bash
nano ~/.ssh/config
```

```sh
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/keyGitHub
```
==> Ctrl + O, luego Enter) y sal (Ctrl + X).

## Seguridad en archivos
```bash 
chmod 700 ~/.ssh
chmod 600 ~/.ssh/keyGitHub
chmod 644 ~/.ssh/keyGitHub.pub
```
## Agente encendido
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/keyGitHub
```

## Configuración en Github
```bash
cat ~/.ssh/keyGitHub.pub
```

+ Entra a tu cuenta -> Settings -> SSH and GPG keys.
+ Haz clic en New SSH key.
+ Ponle un título (ej: WSL-Laptop-Ubuntu) y pega el contenido en el cuadro de "Key".
+ Dale a Add SSH key.

## Verificación de la autenticación 
```bash
ssh -T git@github.com
```

## Clonar proyecto
```bash
cd ~
mkdir proyectos && cd proyectos
git clone git@github.com:tu-usuario/tu-proyecto.git
cd tu-proyecto
code .
```

