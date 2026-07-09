# Sistema Escolar

Este repositorio contenía varios proyectos Django separados (altas y bajas,
calificaciones, horarios, billetera, registro de empresas), cada uno subido
por un equipo distinto. Ahora está unificado en un solo sistema Django, en
la carpeta [`sistema_escolar/`](sistema_escolar/), con login compartido y un
panel de inicio que enlaza a cada módulo.

## Módulos

- **Alumnos y Maestros** (`alumnos_maestros`) — altas, bajas y edición de
  alumnos, maestros, materias e inscripciones.
- **Calificaciones** (`calificaciones`) — captura de calificaciones, firma
  digital de actas y generación de reporte en PDF.
- **Horarios** (`horarios`) — registro y edición de horarios de clase.
- **Empresas** (`empresas`) — registro de empresas vinculadas a la escuela.
- **Billetera** (`billetera`) — movimientos de ingresos y egresos con saldo
  acumulado.

## Cómo correrlo

```bash
cd sistema_escolar
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`, inicia sesión y navega entre los módulos
desde el panel de inicio. El panel de administración de Django está en
`/admin/`.

También puede correrse con Docker:

```bash
cd sistema_escolar
docker compose up --build
```
