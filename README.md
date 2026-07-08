# mi_proyecto

Proyecto Django 5 listo para ejecutar. Incluye la app `core` con un
formulario (`ModelForm`) que guarda un campo `texto` (CharField, 200
caracteres) en SQLite.

## Requisitos

- Python 3.10+
- pip

## Instalación y ejecución

```bash
# 1. (Opcional pero recomendado) Crear entorno virtual
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones (ya vienen incluidas, pero por si acaso)
python manage.py makemigrations
python manage.py migrate

# 4. (Opcional) Crear superusuario para acceder al admin
python manage.py createsuperuser

# 5. Ejecutar el servidor de desarrollo
python manage.py runserver
```

Luego abre tu navegador en: http://127.0.0.1:8000/

El panel de administración está disponible en: http://127.0.0.1:8000/admin/

## Estructura del proyecto

```
mi_proyecto/
├── manage.py
├── requirements.txt
├── README.md
├── mi_proyecto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── core/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    └── templates/
        └── core/
            └── index.html
```

## Funcionalidad

- Formulario en la página principal (`/`) con un campo de texto (`texto`,
  CharField de máximo 200 caracteres).
- Al enviar el formulario, el dato se guarda en la base de datos SQLite
  (`db.sqlite3`) mediante `NotaForm` (un `ModelForm` basado en el modelo
  `Nota`).
- Lista de notas guardadas mostrada debajo del formulario.
- Modelo `Nota` registrado en el panel de administración de Django.
