# -*- coding: utf-8 -*-
def name():
    return 'PO-LI-TY-KA-RE-NU'


def encrypt(text):
    wynik = u''
    for char in text:
        if char == 'P':
            wynik += 'O'
        elif char == 'O':
            wynik += 'P'
        elif char == 'L':
            wynik += 'I'
        elif char == 'I':
            wynik += 'L'
        elif char == 'T':
            wynik += 'Y'
        elif char == 'Y':
            wynik += 'T'
        elif char == 'K':
            wynik += 'A'
        elif char == 'A':
            wynik += 'K'
        elif char == 'R':
            wynik += 'E'
        elif char == 'E':
            wynik += 'R'
        elif char == 'N':
            wynik += 'U'
        elif char == 'U':
            wynik += 'N'
        elif char == 'p':
            wynik += 'o'
        elif char == 'o':
            wynik += 'p'
        elif char == 'l':
            wynik += 'i'
        elif char == 'i':
            wynik += 'l'
        elif char == 't':
            wynik += 'y'
        elif char == 'y':
            wynik += 't'
        elif char == 'k':
            wynik += 'a'
        elif char == 'a':
            wynik += 'k'
        elif char == 'r':
            wynik += 'e'
        elif char == 'e':
            wynik += 'r'
        elif char == 'n':
            wynik += 'u'
        elif char == 'u':
            wynik += 'n'
        else:
            wynik += char
    return wynik


def decrypt(text):
    wynik = ''
    for char in text:
        if char == 'P':
            wynik += 'O'
        elif char == 'O':
            wynik += 'P'
        elif char == 'L':
            wynik += 'I'
        elif char == 'I':
            wynik += 'L'
        elif char == 'T':
            wynik += 'Y'
        elif char == 'Y':
            wynik += 'T'
        elif char == 'K':
            wynik += 'A'
        elif char == 'A':
            wynik += 'K'
        elif char == 'R':
            wynik += 'E'
        elif char == 'E':
            wynik += 'R'
        elif char == 'N':
            wynik += 'U'
        elif char == 'U':
            wynik += 'N'
        elif char == 'p':
            wynik += 'o'
        elif char == 'o':
            wynik += 'p'
        elif char == 'l':
            wynik += 'i'
        elif char == 'i':
            wynik += 'l'
        elif char == 't':
            wynik += 'y'
        elif char == 'y':
            wynik += 't'
        elif char == 'k':
            wynik += 'a'
        elif char == 'a':
            wynik += 'k'
        elif char == 'r':
            wynik += 'e'
        elif char == 'e':
            wynik += 'r'
        elif char == 'n':
            wynik += 'u'
        elif char == 'u':
            wynik += 'n'
        else:
            wynik += char
    return wynik


def info():
    return '''W treści wiadomości zamieniamy parami litery (P, O), (L, I), (T, Y), (K, A), (R, E), (N, U).
Pozostałe litery pozostawiamy. Np. słowo WILKI po zaszyfrowaniu wygląda następująco: WLIAL.'''
