import os
import glob

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12
from typing import NamedTuple

from .config import Config
from shared import generic

_config = Config()

class CertificateData(NamedTuple):
    private_key: object
    firmante: object
    emisor: object
    ca_raiz: object
    politica_file: object

class CertificateLoader:
    def __init__(self):
        self._certs_dir = os.path.join(_config.PATH_BASE, 'certificados')
        self._sign_path = os.path.join(self._certs_dir, _config.SIGN_NAME)
        self._sign_password =  _config.SIGN_PASSWORD
        self._security = None
        self._politica_path = os.path.join(self._certs_dir, _config.POLITICA_NAME)

    def load(self):
        with open(self._sign_path, 'rb') as pfx_file:
            pfx_data = pfx_file.read()
        private_key, firmante, additional_certs = pkcs12.load_key_and_certificates(
            pfx_data,
            self._sign_password.encode(),
            default_backend()
        )

        # Resuelve la cadena (emisor + raiz) desde los certificados embebidos en
        # el .pfx y, como respaldo, desde los .crt/.cer/.pem de la carpeta
        # certificados. Asi funciona tanto para .pfx que traen la cadena
        # (ej. Camerfirma) como para los que no la traen (ej. GSE).
        emisor, ca_raiz = self._resolve_chain(firmante, additional_certs)

        data = {
            'private_key': private_key,
            'firmante': firmante,
            'emisor': emisor,
            'ca_raiz': ca_raiz,
            'politica_file': ''
            # 'politica_file': generic.read_file(path=self._politica_path, mode='rb')
        }

        self._security = CertificateData(**data)

    def _resolve_chain(self, firmante, additional_certs):
        # Junta los certificados disponibles indexados por su subject.
        pool = {}
        for cert in (additional_certs or []):
            pool[cert.subject.rfc4514_string()] = cert
        for cert in self._load_ca_files():
            pool.setdefault(cert.subject.rfc4514_string(), cert)

        # El emisor es el certificado cuyo subject coincide con el issuer del
        # firmante; la raiz es el emisor del emisor.
        emisor = pool.get(firmante.issuer.rfc4514_string())
        if emisor is None:
            raise ValueError(
                "No se encontro el certificado EMISOR (intermedio) de la cadena. "
                f"El firmante fue emitido por: {firmante.issuer.rfc4514_string()}. "
                "El .pfx no lo trae embebido; coloque el certificado del emisor "
                f"(.crt/.cer/.pem) en la carpeta: {self._certs_dir}"
            )

        ca_raiz = pool.get(emisor.issuer.rfc4514_string())
        if ca_raiz is None:
            raise ValueError(
                "No se encontro el certificado RAIZ de la cadena. "
                f"El emisor fue emitido por: {emisor.issuer.rfc4514_string()}. "
                "Coloque el certificado raiz (.crt/.cer/.pem) en la carpeta: "
                f"{self._certs_dir}"
            )

        return emisor, ca_raiz

    def _load_ca_files(self):
        certs = []
        for pattern in ('*.crt', '*.cer', '*.pem'):
            for file_path in glob.glob(os.path.join(self._certs_dir, pattern)):
                try:
                    with open(file_path, 'rb') as f:
                        raw = f.read()
                    try:
                        certs.append(x509.load_pem_x509_certificate(raw, default_backend()))
                    except ValueError:
                        certs.append(x509.load_der_x509_certificate(raw, default_backend()))
                except Exception:
                    # Ignora archivos que no sean certificados validos.
                    continue
        return certs

    @property
    def security(self):
        if not self._security:
            raise ValueError("Certificate data has not been loaded.")
        return self._security

certificate_loader = CertificateLoader()