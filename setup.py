#!/usr/bin/python3
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name="algoritmo_google",
    version="0.1.0",
    description="Projeto de Modelagem Matemática - PageRank"
    long_description=readme,
    author="Gabriel, Guilherme, Milton, Richard"
    author_email=""
    url="https://github.com/bmac2020/projeto_google"
    license=license,
    packages=find_packages(exclude="tests")
)
