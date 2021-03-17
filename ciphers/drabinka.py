# -*- coding: utf-8 -*-
def name():
    return 'drabinka'


def encrypt(txt):
    wynik = ''
    tab1 = 'abcdefghijkl'
    tab2 = 'łmnoprstuwyz'
    Tab1 = 'ABCDEFGHIJKL'
    Tab2 = 'ŁMNOPRSTUWYZ'
    pol = 'ąćęłńóśźż'
    Pol = 'ĄĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    for char in txt:
        if char in pol:
            char = npol[pol.index(char)]
        elif char in Pol:
            char = Npol[Pol.index(char)]

        if char in tab1:
            for i in range(0, 12):
                if tab1[i] == char:
                    wynik += tab2[i]
                    break
        elif char in tab2:
            for i in range(0, 12):
                if tab2[i] == char:
                    wynik += tab1[i]
                    break
        elif char in Tab1:
            for i in range(0, 12):
                if Tab1[i] == char:
                    wynik += Tab2[i]
                    break
        elif char in Tab2:
            for i in range(0, 12):
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
Korzystamy z następującego klucza:
A B C D E F G H I J K L
Ł M N O P R S T U W Y Z
Zamieniamy literę z górnego szeregu na literę z dolnego szeregu i na odwrót, 
np. literę A zapisujemy jako Ł, literę O jako D.
Przykładowo słowo "WILK" wygląda tak: "JUZY" '''
