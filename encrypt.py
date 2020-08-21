#!/usr/bin/env python
import os
import sys

password = sys.argv[1]
cmd = "staticrypt index_unencrypted.html -e -f password_template.html {password}".format(password=password)
os.system(cmd)

cmd = "mv index_unencrypted_encrypted.html index.html"
os.system(cmd)
