# -*- coding: utf-8 -*-
def name():
    return 'MO-TY-LE-CU-DA-KI'


def encrypt(text):
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    tab1 = 'motylecudaki'
    tab2 = 'omytelucadik'
    Tab1 = 'MOTYLECUDAKI'
    Tab2 = 'OMYTELUCADIK'
    wynik = u''
    for char in text:
        if char in pol:
            char = npol[pol.index(char)]
        elif char in Pol:
            char = Npol[Pol.index(char)]
        if char in tab1:
            char = tab2[tab1.index(char)]
        elif char in Tab1:
            char = Tab2[Tab1.index(char)]
        wynik += char
    return wynik


def decrypt(text):
    return encrypt(text)


def info():
    return '''W treści wiadomości zamieniamy parami litery (M, O), (T, Y), (L, E), (C, U), (D, A), (K, I).
Pozostałe litery pozostawiamy. Np. słowo "WILKI" po zaszyfrowaniu wygląda następująco: "WKEIK".'''
