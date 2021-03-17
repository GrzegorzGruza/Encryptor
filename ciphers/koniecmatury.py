# -*- coding: utf-8 -*-
def name():
    return 'KO-NI-EC-MA-TU-RY'


def encrypt(text):
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    tab1 = 'koniecmatury'
    tab2 = 'okinceamutyr'
    Tab1 = 'KONIECMATURY'
    Tab2 = 'OKINCEAMUTYR'
    wynik = u''
    for char in text:
        if char in pol:
            char = npol[pol.index(char)]
        elif char in Pol:
            char = npol[Pol.index(char)]
        if char in tab1:
            char = tab2[tab1.index(char)]
        elif char in Tab1:
            char = Tab2[Tab1.index(char)]
        wynik += char
    return wynik


def decrypt(text):
    return encrypt(text)


def info():
    return '''W treści wiadomości zamieniamy parami litery (K, O), (N, I), (E, C), (M, A), (T, U), (R, Y).
Pozostałe litery pozostawiamy. Np. słowo "WILKI" po zaszyfrowaniu wygląda następująco: "WNLON".'''
