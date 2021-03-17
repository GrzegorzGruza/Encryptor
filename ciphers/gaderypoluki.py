# -*- coding: utf-8 -*-
def name():
    return 'GA-DE-RY-PO-LU-KI'


def encrypt(text):
    wynik = ''
    for char in text:
        if char == 'G':
            wynik += 'A'
        elif char == 'A':
            wynik += 'G'
        elif char == 'D':
            wynik += 'E'
        elif char == 'E':
            wynik += 'D'
        elif char == 'R':
            wynik += 'Y'
        elif char == 'Y':
            wynik += 'R'
        elif char == 'P':
            wynik += 'O'
        elif char == 'O':
            wynik += 'P'
        elif char == 'L':
            wynik += 'U'
        elif char == 'U':
            wynik += 'L'
        elif char == 'K':
            wynik += 'I'
        elif char == 'I':
            wynik += 'K'
        elif char == 'g':
            wynik += 'a'
        elif char == 'a':
            wynik += 'g'
        elif char == 'd':
            wynik += 'e'
        elif char == 'e':
            wynik += 'd'
        elif char == 'r':
            wynik += 'y'
        elif char == 'y':
            wynik += 'r'
        elif char == 'p':
            wynik += 'o'
        elif char == 'o':
            wynik += 'p'
        elif char == 'l':
            wynik += 'u'
        elif char == 'u':
            wynik += 'l'
        elif char == 'k':
            wynik += 'i'
        elif char == 'i':
            wynik += 'k'
        else:
            wynik += char
    return wynik


def decrypt(text):
    wynik = ''
    for char in text:
        if char == 'G':
            wynik += 'A'
        elif char == 'A':
            wynik += 'G'
        elif char == 'D':
            wynik += 'E'
        elif char == 'E':
            wynik += 'D'
        elif char == 'R':
            wynik += 'Y'
        elif char == 'Y':
            wynik += 'R'
        elif char == 'P':
            wynik += 'O'
        elif char == 'O':
            wynik += 'P'
        elif char == 'L':
            wynik += 'U'
        elif char == 'U':
            wynik += 'L'
        elif char == 'K':
            wynik += 'I'
        elif char == 'I':
            wynik += 'K'
        elif char == 'g':
            wynik += 'a'
        elif char == 'a':
            wynik += 'g'
        elif char == 'd':
            wynik += 'e'
        elif char == 'e':
            wynik += 'd'
        elif char == 'r':
            wynik += 'y'
        elif char == 'y':
            wynik += 'r'
        elif char == 'p':
            wynik += 'o'
        elif char == 'o':
            wynik += 'p'
        elif char == 'l':
            wynik += 'u'
        elif char == 'u':
            wynik += 'l'
        elif char == 'k':
            wynik += 'i'
        elif char == 'i':
            wynik += 'k'
        else:
            wynik += char
    return wynik


def info():
    return '''W treści wiadomości zamieniamy parami litery (G, A), (D, E), (R, Y), (P, O), (L, U), (K, I).
Pozostałe litery pozostawiamy. Np. słowo W I L K I po zaszyfrowaniu wygląda następująco: WKUIK.'''
