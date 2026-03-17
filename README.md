# 📱 APLICACIÓN DE FIDELIZACIÓN CON PUNTOS Y RECOMPENSAS PARA PYMES

Esta aplicación móvil, desarrollada con Flutter, tiene como objetivo difundir los derechos laborales y sociales de los ciudadanos ecuatorianos mediante el acceso a documentos oficiales en formato PDF, como la Constitución, el Código del Trabajo y más.

# 🎯 Funcionalidades principales
- Visualización rápida y sencilla de documentos PDF relevantes.
- Navegación intuitiva entre distintas pantallas.
- Integración con un backend en Flask para la gestión y visualización de archivos.

# 🧱 Estructura del Proyecto
 # Frontend (Flutter)
- /derechos_app/lib/screens: contiene las distintas pantallas de la app, cada una cargando un PDF específico.
- /derechos_app/lib/main.dart: punto de entrada de la aplicación, configuración de rutas y temas.
- Uso de la librería flutter_cached_pdfview para cargar PDFs desde URLs.
 # Backend (Flask)
- app.py: servidor principal, permite:
    - Servir archivos PDF almacenados en una carpeta local.
    - Subir nuevos archivos PDF desde el panel administrador.
    - Eliminar archivos PDF existentes.
- Rutas protegidas y con CORS habilitado para acceso desde la app Flutter.
- Carpeta /derechos_server/uploads/pdfs/: almacena los documentos visibles desde la app.
