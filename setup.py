# -*- coding: UTF-8 -*-
import glob
from setuptools import setup, find_packages

setup(
    name="jukebox",
    packages=find_packages(),
    version="0.4.1",
    description="Democratic Jukebox - your democratic music player",
    author="Jens Nistler",
    author_email="opensource@jensnistler.de",
    url="http://jensnistler.de/",
    download_url='http://github.com/lociii/jukebox',
    keywords=["jukebox", "music", "mp3"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Players",
    ],
    install_requires=[
        "Django==1.6.2",
        "mutagen==1.22",
        "django-social-auth==0.7.20",
        "djangorestframework==2.3.13",
        "simplejson==3.3.3",
        "South==0.8.4",
    ],
    include_package_data=True,
    scripts=glob.glob("bin/*"),
    long_description=open("README.rst").read()
)
