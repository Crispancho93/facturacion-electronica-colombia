# Proyecto facturacion-electronica-colombia

Este proyecto facturacion-electronica-colombia es una aplicación web desarrollada en Python utilizando el framework FastAPI. Proporciona una API para enviar facturas, notas crédito y prontamente notas débito a la DIAN en Colombia.

Actualmente está operando en ambiente de habilitación. Para más detalles acerca de cómo correr y depurar el proyecto, puedes consultar este video de YouTube:

[Facturación electrónica DIAN COLOMBIA software propio - API GRATIS](https://youtu.be/EaDoYikq-DI?si=W-lIRWI1gwBewll2)

En caso tal de necesitar ayuda me pueden contactar al WhatsApp +57 301 305 4253

---

## Instalación

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/Crispancho93/facturacion-electronica-colombia.git
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd facturacion-electronica-colombia
    ```

3. Crea un entorno virtual e instala las dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate    # Linux / macOS
    .\venv\Scripts\activate     # Windows
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el servidor de desarrollo:

    ```bash
    uvicorn app:app --reload
    ```

2. Accede a la documentación de la API en tu navegador:

    ```
    http://localhost:8000/docs
    ```

3. Realiza solicitudes HTTP a la API utilizando herramientas como cURL o Postman.

## Contribución

¡Agradecemos las contribuciones! Si deseas contribuir al proyecto, sigue estos pasos:

1. Fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y commitealos (`git commit -am 'Agrega nueva característica'`).
4. Sube los cambios a tu repositorio (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Estructura del Proyecto

## Pendiente por validar
1. Validar campo IndustryClasificationCode - Código de actividad que registra en el RUT

---

## Licencia

Este proyecto está licenciado bajo la misma licencia de código abierto que el kernel de Linux: [Licencia GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html). Esto significa que puedes usar, modificar y distribuir el software bajo los términos de la licencia.
