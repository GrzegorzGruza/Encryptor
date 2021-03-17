# -*- coding: utf-8 -*-
def name():
    return 'AtBash'


def encrypt(txt):
    wynik = ''
    tab1 = 'abcdefghijklm'
    tab2 = 'zyxwvutsrqpon'
    Tab1 = 'ABCDEFGHIJKLM'
    Tab2 = 'ZYXWVUTSRQPON'
    pol = 'ąćęłńóśźż'
    Pol = 'ĄĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    for char in txt:
        if char in pol:
            char = npol[pol.index(char)]
        elif char in Pol:
            char = npol[Pol.index(char)]

        if char in tab1:
            for i in range(0, 13):
                if tab1[i] == char:
                    wynik += tab2[i]
                    break
        elif char in tab2:
            for i in range(0, 13):
                if tab2[i] == char:
                    wynik += tab1[i]
                    break
        elif char in Tab1:
            for i in range(0, 13):
                if Tab1[i] == char:
                    wynik += Tab2[i]
                    break
        elif char in Tab2:
            for i in range(0, 13):
                if Tab2[i] == char:
                    wynik += Tab1[i]
                    break
        else:
            wynik += char
    return wynik


def decrypt(txt):
    return encrypt(txt)


def info():
    return '''Szyfrowanie i rozszyfrowywanie wyglądają identycznie.
Działanie szyfru polega na zamianie litery leżącej w odległości X od początku alfabetu 
na literę leżącą w odległości X od jego końca.

Posługujemy się alfabetem łacińskim:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Przykładowo słowo "HARCERZ" to "SZIXVIA"'''
