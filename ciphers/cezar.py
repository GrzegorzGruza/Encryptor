# -*- coding: utf-8 -*-
def name():
    return 'cezar'


def encrypt(txt):
    wynik = ""
    for char in txt:
        char = ord(char)
        if 97 <= char and char <= 122:
            char += 3
            if (char > 122):
                char = 97 + char % 123
        elif 65 <= char and char <= 90:
            char += 3
            if (char > 90):
                char = 65 + char % 91
        char = chr(char)
        wynik = wynik + char
    return wynik


def decrypt(txt):
    wynik = ""
    for char in txt:
        char = ord(char)
        if 97 <= char and char <= 122:
            char += 23
            if (char > 122):
                char = 97 + char % 123
        elif 65 <= char and char <= 90:
            char += 23
            if (char > 90):
                char = 65 + char % 91
        char = chr(char)
        wynik = wynik + char
    return wynik


def info():
    return '''Kodowanie polega na zamienieniu każdej litery na literę stojącą o 3 dalej.
Szyfrujemy zapętlonym alfabetem łacińskim (po a jest z).
np. słowo KOT  zaszyfrujemy jako NRW.

Rozkodowywanie polega na zamienia litery na literę o 3 miejsca bliżej.
Rozszyfrowujemy alfabetem łacińskim. Np. słowo ZLON oznacza WILK.'''
