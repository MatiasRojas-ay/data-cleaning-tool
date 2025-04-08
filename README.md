# 🧹 Data Cleaner

**Data Cleaner** es una aplicación web sencilla y efectiva que te permite limpiar y transformar archivos de datos.  
Ideal para profesionales que necesiten limpiar rápidamente archivos CSV, JSON, TSV y más, aplicando operaciones de limpieza como la eliminación de columnas vacías, la normalización de texto y mucho más.

---

## 🎯 Objetivo

Brindar una herramienta eficiente y fácil de usar para:

- Subir un archivo de datos.
- Seleccionar operaciones de limpieza a aplicar.
- Descargar el archivo limpio listo para análisis.

---

## 🛠️ Stack

- **Frontend:** Vue 3 + Vite + Tailwind CSS
- **Backend:** Django 5 + Django REST Framework
- **Base de datos:** SQLite (en este caso no se requiere para el funcionamiento básico)
- **Estética:** Tailwind CSS para un diseño moderno y limpio
- **Funciones:** Limpiar datos mediante operaciones como eliminar columnas vacías, normalizar texto, entre otros.

---

## 🧩 Operaciones de limpieza

### 🔹 Operaciones disponibles
- Eliminar columnas vacías
- Eliminar filas vacías
- Eliminar filas duplicadas
- Eliminar columnas con valores constantes
- Eliminar columnas con altos valores nulos
- Filtrar valores atípicos
- Rellenar valores faltantes
- Normalizar texto (quitar espacios, caracteres especiales, etc.)
- Conversión de tipos de datos
- Transformación de fechas
- Redondear valores numéricos

---

## 🚀 Instalación

### 1. Clonar el proyecto

```bash
git clone https://github.com/MatiasRojas-ay/data-cleaning-tool.git
cd data-cleaning-tool
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear el archivo .env

```bash
SECRET_KEY=django-insecure-tu-clave-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Ejecutar el servidor

```bash
python backend/manage.py runserver
```

## 📁 Estructura del proyecto

```bash
data-cleaning-tool/
├── backend/                 # Proyecto Django
│   ├── cleaner/             # Lógica de limpieza de datos
│   ├── manage.py
├── frontend/                # Proyecto Vue.js con Tailwind CSS
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
├── .env                     # Variables de entorno
├── requirements.txt         # Dependencias del backend
└── README.md                # Este archivo
```

## 📸 Captura de pantalla

![Pagina de inicio](screenshot.png)

## ✨ Autor

Desarrollado por [Matías Rojas]