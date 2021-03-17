# -*- coding: utf-8 -*-
def name():
    return 'MA-LI-NO-WE-BU-TY'


def encrypt(text):
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    tab1 = 'malinowebuty'
    tab2 = 'amilonewubyt'
    Tab1 = 'MALINOWEBUTY'
    Tab2 = 'AMILONEWUBYT'
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
    return '''W treści wiadomości zamieniamy parami litery (M, A), (L, I), (N, O), (W, E), (B, U), (T, Y).
Pozostałe litery pozostawiamy. Np. słowo "WILKI" po zaszyfrowaniu wygląda następująco: "ELIKL".'''
