

curl -fsSL https://opencode.ai/install | bash

Ejecuta este comando en tu terminal de WSL. Esto obliga a Linux a leer de nuevo el archivo .bashrc y reconocer el nuevo comando:
source ~/.bashrc
33cSLpbzI657LIEzPQkCWGdyb3FYjr9Ccx5mC73ZghSGTkrF9IaK
"gsk _ 33"
echo 'export GROQ_API_KEY="XXX"' >> ~/.bashrc
source ~/.bashrc


opencode --init
opencode config set provider groq
opencode config set model llama-3.3-70b-versatile

# Init
+ Entrar a la ruta del proyecto
+ opencode
+ /init

# Hacer preguntas
Se utiliza la tecla @ para realizar una búsqueda aproximada de archivos dentro del proyecto.
Ejemplo 
```bash 
¿Cómo se maneja la autenticación en @packages/functions/src/api/index.ts ? 
```

# Modo Plan
## Ejemplo
Cuando un usuario elimine una nota, queremos marcarla como eliminada en la base de datos. Luego, cree una pantalla que muestre todas las notas eliminadas recientemente. Desde esa pantalla, el usuario podrá restaurar una nota o eliminarla de forma permanente.

## Iterar sobre un plan
Una vez que OpenCode le proponga un plan, puede darle comentarios o agregar más detalles.
Queremos diseñar esta nueva pantalla usando un diseño que ya hemos usado antes. [Imagen #1] Revise esta imagen y úsela como referencia.

# Modo Build
Implementar la funcionalidad, cuando esté conforme con el plan, vuelva al modo Build presionando de nuevo la tecla Tab.

## Ejemplo
Necesitamos agregar autenticación a la ruta /settings. Revise cómo se maneja esto en la ruta /notes en @packages/functions/src/notes.ts e implemente la misma lógica en @packages/functions/src/settings.ts.

# undo - redo
/undo  
/redo

# Configuración
Las fuentes de configuración se cargan en este orden (las fuentes posteriores anulan las anteriores):

+ Configuración remota (de .well-known/opencode): valores predeterminados de la organización
+ Configuración global (~/.config/opencode/opencode.json) - preferencias del usuario
+ Configuración personalizada (OPENCODE_CONFIG env var): anulaciones personalizadas
+ Configuración del proyecto (opencode.json en el proyecto): configuración específica del proyecto
+ Directorios .opencode - agentes, comandos, complementos
+ Configuración en línea (OPENCODE_CONFIG_CONTENT env var): anulaciones del tiempo de ejecución

## Global
Coloque su configuración global OpenCode en ~/.config/opencode/opencode.json. Utilice la configuración global para las preferencias de todo el usuario, como temas, proveedores o combinaciones de teclas.

## Por proyecto
Agregue opencode.json en la raíz de su proyecto. La configuración del proyecto tiene la mayor prioridad entre los archivos de configuración estándar: anula las configuraciones globales y remotas.

## Ruta personalizada
Especifique una ruta de archivo de configuración personalizada utilizando la variable de entorno OPENCODE_CONFIG.
```bash
export OPENCODE_CONFIG=/path/to/my/custom-config.json
opencode run "Hello world"
``` 
### Esquema
+ El archivo de configuración tiene un esquema definido en opencode.ai/config.json.
+ Su editor debería poder validar y autocompletar según el esquema.

https://opencode.ai/config.json

## Modelos
Puede configurar los proveedores y modelos que desea utilizar en su configuración OpenCode a través de las opciones provider, model y small_model.

```bash
opencode.json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {},
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5"
}
```
La opción small_model configura un modelo separado para tareas livianas como la generación de títulos. De forma predeterminada, OpenCode intenta utilizar un modelo más económico si su proveedor tiene uno disponible; de ​​lo contrario, recurre a su modelo principal.

## Agentes
Puedes configurar agentes especializados para tareas específicas a través de la opción agent.
```bash
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for best practices and potential issues",
      "model": "anthropic/claude-sonnet-4-5",
      "prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",
      "tools": {
        // Disable file modification tools for review-only agent
        "write": false,
        "edit": false,
      },
    },
  },
}
```
### Agente predeterminado
Puede configurar el agente predeterminado usando la opción default_agent. Esto determina qué agente se utiliza cuando no se especifica ninguno explícitamente.
```bash
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "plan"
}
```

# Proveedores
## Credenciales
Cuando agrega las claves API de un proveedor con el comando /connect, se almacenan en ~/.local/share/opencode/auth.json.

## OpenCode Zen
OpenCode Zen es una lista de modelos proporcionados por el equipo OpenCode que han sido probado y verificado para funcionar bien con OpenCode. Más información.

Ejecute el comando /connect en TUI, seleccione opencode y diríjase a opencode.ai/auth.

/connect
┌ API key
│
│
└ enter

Ejecute /models en TUI para ver la lista de modelos que recomendamos.

## OpenCode Go
OpenCode Go es un plan de suscripción de bajo costo que brinda acceso confiable a modelos de codificación abiertos populares proporcionados por el equipo de OpenCode que han sido probado y verificado para funcionar bien con OpenCode.

Ejecute el comando /connect en TUI, seleccione OpenCode Go y diríjase a opencode.ai/auth.

