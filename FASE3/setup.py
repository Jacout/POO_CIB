from distutils.core import setup
import py2exe
setup(
name = 'Payload',
description = 'Python-based App',
version = '1.0',
console=['payload.pyw'],
options = {'py2exe': {'bundle_files': 2,
                      'packages':'ctypes',
                      'includes': 'base64,sys,socket,struct,time,code,platform,getpass,shutil'
                      ,}},
zipfile = None,
)
