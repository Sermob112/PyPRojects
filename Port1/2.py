import pyAesCrypt

password = input('insert password ')

# #encrypt
# pyAesCrypt.encryptFile('test.txt','encrypted.txt', password)

# #decrypt
pyAesCrypt.decryptFile('encrypted.txt', 'data.txt',password)