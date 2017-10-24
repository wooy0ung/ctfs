from Crypto.Cipher import AES

key='pctf2016pctf2016pctf2016pctf2016'
enc="x/nzolo0TTIyrEISd4AP1spCzlhSWJXeNbY81SjPgmk=+".decode('base64')

cryptor=AES.new(key,AES.MODE_ECB)
plain=cryptor.decrypt(enc)
print plain