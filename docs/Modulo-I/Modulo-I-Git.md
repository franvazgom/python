<img src="../../images/LogoMagicPython.png" width="100">

# Git - Comandos basicos

## Verificación de instalación
```
git --version
```

## Configuraci[on de usuario]
<img src="../../images/GitConfig.png" width="600">

## SSH - Autenticación 
Revisa los pasos a seguir de acuerdo con el sistema operativo que tengas instalado
[SSH - Doc](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

### Pasos a seguir
+ Generar una clave SSH basada en llave pública y privada 
+ Iniciar el agente SSH 
+ Agregar la clave SSH al ssh-agent 
    + Indicar que se realice de manera automática
+ Prueba de conexión con github 
## Clonar repositorio
### Obtener el link de nuestro repositorio
<img src="../../images/GitProjectLink.png" width="600">

```
git clone https.... 
```
## El archivo .gitignore
<img src="../../images/GitIgnore.png" width="600">

## ¿Cómo funciona? 
El repositorio local está compuesto por 3 árboles 
+ Directorio de trabajo
+ Index  (Stage)
+ Head  (Apunta al último commit realizado)

## Colocar un archivo en el Stage 
```
git add <ficher>
gitt add .      #Sube todo el contenido de la carpeta
git add -A      #Sube todo
```
## status 
```
git status
```

## Deshacer un que no se ha hecho commit
```
git restore <fichero>
```

## Commit 
```
git commit -m "Notas de los cambios para identificar mejor el cambio" 
```

## Deshacer un cambio
```
git reset -hard             #Deshace todos los cambios hasta el último commit 
git reset AHEAD <fichero>   #Deshace los cambios del fichero
```

## Push  (subir un cambio)
```
git push origin <rama>
ejemplo:  git push origin main 
```

## Pull  (Actualizar el repostorio local)
```
git push origin <rama>
ejemplo:  git push origin main 
```

## Referencias
[https://rogerdudler.github.io/git-guide/index.es.html](https://rogerdudler.github.io/git-guide/index.es.html) <br>
[https://docs.github.com/es/get-started/quickstart/hello-world](https://docs.github.com/es/get-started/quickstart/hello-world)
