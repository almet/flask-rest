# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='Flask-REST',
    version='1.0',
    url='http://github.com/ametaireau/flask-rest/',
    license='BSD',
    author=u"Alexis Métaireau",
    author_email="alexis@notmyidea.org",
    description="A simple REST toolkit for Flask",
    long_description=open('README.rst').read(),
    install_requires=['Flask',],
    py_modules=['flask_rest'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
