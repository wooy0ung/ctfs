from Crypto.Cipher import AES
 
key='cGhyYWNrICBjdGYgMjAxNg=='.decode('base64')
enc='sSNnx1UKbYrA1+MOrdtDTA=='.decode('base64')

cryptor=AES.new(key,AES.MODE_ECB)
plain=cryptor.decrypt(enc)
print plain