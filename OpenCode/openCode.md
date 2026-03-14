

curl -fsSL https://opencode.ai/install | bash

Ejecuta este comando en tu terminal de WSL. Esto obliga a Linux a leer de nuevo el archivo .bashrc y reconocer el nuevo comando:
source ~/.bashrc
opencode --init
opencode config set provider groq
opencode config set model llama-3.3-70b-versatile
