# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="PaloPelo", 
 version="1.0", 
 description="Clon malo de Arkanoid", 
 author="Javier Sala", 
 author_email="javisala.ca@gmail.com", 
 url="url del proyecto", 
 license="tipo de licencia", 
 scripts=["Arkanoid.py"], 
 console=["Arkanoid.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)