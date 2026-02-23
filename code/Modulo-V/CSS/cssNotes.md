# CSS
CSS existe para no "entorpecer" o "ensuciar" al código HTML
Etiquetas como"center, "i", "bold" etc..
Es importante diferenciar entre contenido y formato

CSS poermite separar los Estilos de contenido

## Añadir CSS
### Inline
```html
<tag style="css"/>
```
Va en la misma línea del elemento 
```html
<html style='background:blue'>
</html>
```
Sintaxis:  <Etiqueta style='atributo que se quiere cambiar: valor'>

Son muy útiles para añadir estilos CSS a un único elemento de la página HTML, se recomienda solamente para secciones específicas, o cuando se están realizando pruebas por ejemplo

### Internal
```html
<style>css</style>
```

```html
<html>
    <head>
        <style>
            html {
                background:red;
            }
        </style>
    </head>
<html>
```
El estilo interno se puede aplicar a cualquier lugar dentro del mismo documento HTML

Sintaxis: Selector { .. }

Desventaja: Si es un sitio con varias páginas WEB se tendría que "repetir"

### External
```html
<link href="style.css">
```
Los estilos viven en un archivo 

```html
<html>
    <head>
        <link
            rel='stylesheet'
            href='./styles.css'
        </>
    </head>
<html>
```
rel -> "Relación" cuál es el papel de esto que estamos vinculando
href -> Ubicación 
Esto es lo más común

## Selectores
Selector { property: value }

###
class Selector

.class_name { property:value}

Una clase es un "algo" que se puede añadir como atributo a cualquier elemento

```html
...
.red-text {
    color:Red
}
...
<h2 class='red-text'>Red</h2>
```
### Id Selector

#main {
    color:red
}

```html
...
#main {
    color:Red
}
...
<h2 id='main'>Red</h2>
```

### Attribute Selector
p[draggable]{
    color:red
}
Todos los parrafos que tengan el atributo de "arrastable" 

```html
...
p[draggable]{
    color:red;
}
...
<p draggable="True">Parrafo</p>
```

p[draggable="false"]{
    color:red;
}

### Universal selector
* {
    color:red;
}

https://colorhunt.co/palettes/popular

# Font properties
1px = 1/96 inch = 0.26mm 
1pt = 1/72 inch = 0.35mm 
1em = 100% of parent
1rem = 100% of root



