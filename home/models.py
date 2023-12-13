from django.db import models

#@T
#file encryption
#from django_cryptography.fields import EncryptedFileField
#from cryptography.hazmat.backends import default_backend
#from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
'''
class EncryptedFile(models.Model):
    file = EncryptedFileField(upload_to='uploads/')
    

    def encrypt_file(file_content, key):
        cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(file_content) + encryptor.finalize()
        return encrypted_data

    def decrypt_file(encrypted_data, key):
        cipher = Cipher(algorithms.AES(key), modes.CFB8(), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        return decrypted_data
'''



# Create your models here.
class Contact(models.Model):
    sno= models.AutoField(primary_key=True)#django automatically takes it as primarly even if i not write primary_key=true
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content= models.TextField()
    timeStamp =models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) :
        return 'Message from' + self.name + '-' + self.email
    
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    file_encrypted = models.FileField(upload_to='uploads/encrypted/', blank=True)
    key = models.TextField(blank=True)
    #file = models.FileField(upload_to='user_files/', null=True, blank=True)  # Adjust 'user_files/' to your desired upload path
    '''
    #@T : add file for upload document
    file = models.FileField(default=None, null=True, blank=True)
    file = models.FileField()
    '''



def default_file():
    return 'default_file.txt'
'''
class EncryptedFile(models.Model):
    file = models.FileField(upload_to='uploads/', default=default_file)

    # Other fields if needed

    def __str__(self):
        return self.file.name

'''

class EncryptedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    file_encrypted = models.FileField(upload_to='uploads/encrypted/', blank=True)
    key = models.TextField(blank=True)
'''
# models.py
file = models.FileField(upload_to='uploads/')
file_encrypted = models.FileField(upload_to='uploads/encrypted/', blank=True)
'''
'''
class EncryptedFile(models.Model):
    encrypted_file = models.FileField(upload_to='encrypted_files/')

class ModelWithFile(models.Model):
    file = models.FileField(upload_to='uploads/')
'''