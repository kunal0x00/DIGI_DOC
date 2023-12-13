from Crypto.Cipher import AES
from Crypto.Random import new as Random
from hashlib import sha256
from base64 import b64encode, b64decode

class AESCipher:
    def __init__(self, key):
        self.block_size = 16
        self.key = sha256(key.encode()).digest()[:32]
        self.pad = lambda s: s + (self.block_size - len(s) % self.block_size) * bytes([self.block_size - len(s) % self.block_size])
        self.unpad = lambda s: s[:-s[-1]]

    def encrypt(self, data):
        plain_text = self.pad(data)
        iv = Random().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        encrypted_bytes = cipher.encrypt(plain_text)
        return b64encode(iv + encrypted_bytes).decode()

    def decrypt(self, encrypted_data):
        try:
            # Ensure the length of the base64-encoded string is a multiple of 4
            padding = len(encrypted_data) % 4
            if padding > 0:
                encrypted_data += '=' * (4 - padding)

            # Decode the input using base64
            encrypted_data = b64decode(encrypted_data.encode('utf-8'))

            iv = encrypted_data[:AES.block_size]
            cipher = AES.new(self.key, AES.MODE_OFB, iv)
            decrypted_bytes = cipher.decrypt(encrypted_data[AES.block_size:])
            return self.unpad(decrypted_bytes).decode('utf-8')
        except Exception as e:
            return f"Error during decryption: {e}"