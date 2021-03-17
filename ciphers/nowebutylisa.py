# -*- coding: utf-8 -*-
def name():
    return 'NO-WE-BU-TY-LI-SA'


def encrypt(text):
    pol = 'ąćęłńóśźż'
    Pol = 'ĄĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    tab1 = 'nowebutylisa'
    tab2 = 'onewubytilas'
    Tab1 = 'NOWEBUTYLISA'
    Tab2 = 'ONEWUBYTILAS'
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
    return '''W treści wiadomości zamieniamy parami litery (N, O), (W, E), (B, U), (T, Y), (L, I), (S, A).
Pozostałe litery pozostawiamy. Np. słowo "WILKI" po zaszyfrowaniu wygląda następująco: "ELIKL".'''
