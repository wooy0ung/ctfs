#!/usr/bin/python
# -*- coding:utf8 -*-

from Crypto.Cipher import AES
import hashlib

key = hashlib.md5("QR").hexdigest()
enc = "3ukka4wZf2Q9H8PEI5YKFA=="

plain = AES.new(key,AES.MODE_ECB).decrypt(enc.decode("base64"))

print plain
# 1Znmpr4jzChwxXqB

key = "s776051080zum92N"
enc = "bqIGBfOGuOsxLYV16OI7xRNAZrcFdYLJtHaDym2O7so="

plain = AES.new(key,AES.MODE_ECB).decrypt(enc.decode("base64"))

print plain
# XCTF{W0W_U_G0T_TH3_FL4G}