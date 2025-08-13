# PH Parking - Gestión de Comitentes

Script para procesar comitentes desde base de datos y actualizar grupo PH Parking.

## �� Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repositorio>
   cd Proyecto-PH-PARKING
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
   ```

## ⚙️ Configuración

Configurar el archivo `.env` con tus credenciales:

```env
API_BASE_URL=https://api-risk.demo.matrizoms.com.ar/oms-webservices/rest
API_USERNAME=tu_usuario
API_PASSWORD=tu_password
GROUP_ID=16
GROUP_NAME=CABLE 2
```

## 🎯 Uso

Ejecutar el script:

```bash
python process_accounts.py
```

## 📁 Estructura del proyecto
Proyecto PH-PARKING/
├── .env # Variables de entorno (no subir a git)
├── .env.example # Plantilla de variables
├── .gitignore # Archivos a ignorar
├── README.md # Documentación
├── config.py # Configuración
├── process_accounts.py # Script principal
├── requirements.txt # Dependencias
└── app/
├── api_client.py # Cliente de API
└── utils.py # Utilidades

## ✅ Funcionalidades

- ✅ Conexión con API externa
- ✅ Procesamiento de comitentes
- ✅ Validación de datos
- ✅ Actualización de grupos
- ✅ Manejo de errores

