GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that run tests whenever you push a change to your repository, or that deploy merged pull requests to production.

#########################
.github/workflows/pylint.yml
#########################

name: Pylint Validation
on: [push]
env:
  # Esto elimina el warning de Node.js 20 que te está ensuciando el log
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pylint

      - name: Analysing the code with pylint
        run: |
          # Ejecutamos pylint y capturamos el resultado.           
          pylint --fail-under=9.0 $(git ls-files '*.py')

#########################
.pylintrc
#########################

[MASTER]
# Ignora carpetas comunes de entorno virtual
ignore=venv,env,.venv,dist,build

[MESSAGES CONTROL]
# Desactivamos todo primero para tener control total
disable=all
# Activamos solo lo relacionado con documentación (Missing Docstrings)
# C0114: Missing module docstring
# C0115: Missing class docstring
# C0116: Missing function or method docstring
enable=C0114,C0115,C0116

[REPORTS]
# Muestra una puntuación del 1 al 10
reports=yes
# No mostrar estadísticas aburridas, solo el puntaje
score=yes

[BASIC]
# Aquí podrías configurar el tamaño mínimo de los docstrings si quisieras
docstring-min-length=5

#########################
Rules
#########################
Require a pull request before merging
Require status checks to pass
    build 
Block force pushes