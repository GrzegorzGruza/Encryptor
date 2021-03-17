# -*- coding: utf-8 -*-
def name():
    return 'ROT13'


def encrypt(txt):
    wynik = ""
    for char in txt:
        char = ord(char)
        if 97 <= char and char <= 122:
            char += 13
            if (char > 122):
                char = 97 + char % 123
        elif 65 <= char and char <= 90:
            char += 13
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
            char += 13
            if (char > 122):
                char = 97 + char % 123
        elif 65 <= char and char <= 90:
            char += 13
            if (char > 90):
                char = 65 + char % 91
        char = chr(char)
        wynik = wynik + char
    return wynik


def info():
    return '''Jest to szyfr wzorowany na szyfrze Cezara.
Kodowanie polega na zamienieniu każdej litery na literę stojącą o 13 dalej.
Szyfrujemy zapętlonym alfabetem łacińskim (po a jest z).
np. słowo "HARCERZ" zaszyfrujemy jako "UNEPREM". '''
