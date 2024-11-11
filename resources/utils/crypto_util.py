import base64
import json

from Crypto import Random
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from django.conf import settings

PRIVATE_KEY: str = settings.PRIVATE_KEY


class CryptoUtil:

    @classmethod
    def generate_keys(cls):
        """
        Genera un par de claves RSA (pública y privada).
        Retorna las claves en formato PEM.
        """
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    @classmethod
    def decode_base64(cls, encrypted_data: str, count: int = 1) -> dict:
        """
        Decodifica el query parameter en Base64 y lo convierte en un JSON.

        :param encrypted_data: Datos cifrados en formato Base64 del query parameter.
        :return: Diccionario con el IV, clave AES cifrada y datos cifrados.
        """
        data = base64.b64decode(encrypted_data).decode('utf-8')
        return json.loads(data) if count <= 1 else CryptoUtil.decode_base64(data, count-1)

    @classmethod
    def decrypt_aes_key(cls, encrypted_key: bytes) -> bytes:
        """
        Descifra la clave AES usando la clave privada RSA.

        :param encrypted_key: Clave AES cifrada en Base64.
        :return: Clave AES en bytes.
        """
        private_key = RSA.import_key(PRIVATE_KEY)
        rsa_cipher = PKCS1_OAEP.new(private_key)
        aes_key = rsa_cipher.decrypt(encrypted_key)  # FALLA AQUI
        return aes_key

    @classmethod
    def decrypt_data(cls, encrypted_data: str, aes_key: bytes, iv: str) -> dict:
        """
        Descifra los datos JSON utilizando la clave AES y el IV.

        :param encrypted_data: Texto cifrado en Base64.
        :param aes_key: Clave AES en bytes.
        :param iv: IV en Base64.
        :return: Diccionario JSON original.
        """
        cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=base64.b64decode(iv))
        decrypted_data = cipher_aes.decrypt(base64.b64decode(encrypted_data))
        return json.loads(decrypted_data.decode("utf-8"))

    @classmethod
    def decrypt(cls, encrypted_data: str) -> dict:
        """
        Realiza todo el proceso de descifrado y retorna los datos originales.

        :param encrypted_data: Datos cifrados en formato Base64 del query param.
        :return: Diccionario JSON con los datos originales.
        """
        # Decodificar el query param

        decoded_data = cls.decode_base64(encrypted_data)
        encrypted_key_b64 = decoded_data["key"]
        iv_b64 = decoded_data["iv"]
        encrypted_text_b64 = decoded_data["data"]
        # Decodificar de Base64 a bytes
        encrypted_key = base64.b64decode(encrypted_key_b64)
        iv = base64.b64decode(iv_b64)
        encrypted_text = base64.b64decode(encrypted_text_b64)
        # Descifrar la clave AES con RSA
        aes_key = cls.decrypt_aes_key(encrypted_key)  # FALLA AQUI
        # Descifrar los datos con AES

        decrypted_data = cls.decrypt_data(encrypted_data=encrypted_text_b64,
                                          aes_key=aes_key,
                                          iv=iv_b64)
        return decrypted_data
