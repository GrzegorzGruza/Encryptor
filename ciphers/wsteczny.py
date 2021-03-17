# -*- coding: utf-8 -*-
def name():
    return 'wsteczny'


def encrypt(text):
    wynik = ''
    for char in text[:-1]:
        wynik = char + wynik
    return wynik


def decrypt(text):
    return encrypt(text)


def info():
    return '''Polega na zapisaniu tekstu od tyłu,
np. "Robert Baden-Powell" to "llewoP-nedaB treboR"'''
