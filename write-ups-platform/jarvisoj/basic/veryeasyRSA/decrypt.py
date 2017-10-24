#!/usr/bin/python
# -*- coding:utf8 -*-

import gmpy2

p = 3487583947589437589237958723892346254777
q = 8767867843568934765983476584376578389
e = 65537

d = gmpy2.invert(e, (p-1) * (q - 1))
print d