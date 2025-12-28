# Implementa tu solución aquí
from datetime import datetime

fecha_dt = lambda f: datetime.strptime(f, "%d/%m/%Y")
cambiar_formato = lambda f: fecha_dt(f).strftime("%Y-%m-%d")


