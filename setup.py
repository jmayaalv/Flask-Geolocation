"""
Flask-Geolocation
-------------

This is the description for that library
"""
from setuptools import setup, find_packages

setup(
    name='Flask-Geolocation',
    version='1.0',
    url='https://github.com/jmayaalv/flask-geolocation',
    license='BSD',
    author='Juan E. Maya',
    author_email='jmayaalv@gmail.com',
    description='Flask IP Geolocation',
    long_description=__doc__,
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
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