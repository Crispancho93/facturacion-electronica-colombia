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

## Certificados y cadena de certificación

La firma XAdES que exige la DIAN necesita **tres** certificados: el del **firmante**, el de la **entidad emisora** (CA intermedia) y el de la **CA raíz**. Estos se cargan en [shared/certificate.py](shared/certificate.py).

Los certificados se buscan en la carpeta `certificados` dentro de `PATH_BASE` (definido en el `.env`). Con `PATH_BASE=C:\FE` la ruta es `C:\FE\certificados\`:

```
C:\FE\certificados\
├── certificado.pfx      ← tu certificado + llave privada (nombre = SIGN_NAME del .env)
├── CA_SUB01.crt         ← emisor / CA intermedia (opcional, ver abajo)
├── CA_ROOT.crt          ← CA raíz (opcional, ver abajo)
└── politicadefirmav2.pdf
```

### ¿Por qué a veces hacen falta CA_SUB01.crt y CA_ROOT.crt?

Depende de cómo la certificadora arme el archivo `.pfx`:

- **Algunas certificadoras (ej. Camerfirma) embeben la cadena completa dentro del `.pfx`.** En ese caso `emisor` y `ca_raiz` se extraen directo del archivo y **no necesitas agregar nada**.
- **Otras (ej. GSE) entregan el `.pfx` solo con tu certificado, sin la cadena.** En ese caso hay que colocar el certificado del emisor y el de la raíz como archivos aparte en la carpeta `certificados`.

El código resuelve la cadena automáticamente: primero usa los certificados embebidos en el `.pfx` y, si faltan, los busca entre los archivos `.crt / .cer / .pem` de la carpeta. **No importa el nombre del archivo**: se identifican por su contenido (comparando los campos `issuer` / `subject`), no por el nombre.

Si falta algún eslabón, la carga falla con un mensaje claro indicando qué certificado falta y dónde ponerlo.

### Cómo obtener la cadena cuando el `.pfx` no la trae

El propio certificado indica la URL de descarga en su extensión AIA (`caIssuers`). Ejemplo con la cadena de **GSE**:

```bash
# Emisor / CA intermedia
curl -k https://certs2.gse.com.co/CA_SUB01.crt -o C:\FE\certificados\CA_SUB01.crt

# CA raíz
curl -k https://certs2.gse.com.co/CA_ROOT.crt  -o C:\FE\certificados\CA_ROOT.crt
```

> Para otra certificadora, revisa la URL `caIssuers` de tu propio certificado (dentro del `.pfx`) y descarga en cadena hasta llegar a la raíz autofirmada.

> **Importante:** estos `.crt` deben existir en la carpeta `certificados` de **cada PC/servidor** donde corra la aplicación. Cópialos junto con el `.pfx` al desplegar.

### Versión de `cryptography`

El `requirements.txt` fija `cryptography==3.4.8` (OpenSSL 1.1.1). Las versiones más nuevas usan OpenSSL 3.x, que deshabilita algoritmos legacy (RC2) y puede devolver la cadena embebida vacía al leer `.pfx` exportados por Windows. Si necesitas actualizar `cryptography`, re-exporta el `.pfx` con cifrado moderno (AES) para evitar ese problema.

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
