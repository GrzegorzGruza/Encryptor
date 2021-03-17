# -*- coding: utf-8 -*-
def name():
    return 'Mafeking'


def encrypt(text):
    wynik = ''
    pop = ''
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'x',
           'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'X',
           'Y', 'Z']
    tab1 = ['M1', 'A1', 'F1', 'E1', 'K1', 'I1', 'N1', 'G1', 'M2', 'A2', 'F2', 'E2', 'K2', 'I2', 'N2', 'G2', 'M3', 'A3',
            'F3', 'E3', 'K3', 'I3', 'N3', 'G']

    i = 1
    for char in text:
        if char in pol:
            char = npol[pol.index(char)]
        elif char in Pol:
            char = Npol[Pol.index(char)]

        if i > 1 and wynik[-1] != ' ' and pop != '\n':
            wynik += " "
        if char in tab:
            wynik += tab1[tab.index(char)]

        elif char in Tab:
            wynik += tab1[Tab.index(char)]
        else:
            wynik += char
        i += 1
        pop = char
    return wynik


def decrypt(text):
    wynik = ''
    pom = ''
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'x',
           'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'X',
           'Y', 'Z']
    tab1 = ['M1', 'A1', 'F1', 'E1', 'K1', 'I1', 'N1', 'G1', 'M2', 'A2', 'F2', 'E2', 'K2', 'I2', 'N2', 'G2', 'M3', 'A3',
            'F3', 'E3', 'K3', 'I3', 'N3', 'G3']

    i = 1
    for char in text:
        if char == ' ' or i == len(text) or char == '\n':
            if len(pom) == 0:
                pom = ' '
            if pom in tab1:
                wynik += tab[tab1.index(pom)]
            else:
                if pom != '\n':
                    wynik += pom
            pom = ''
        elif char != '\n':
            pom += char
        if char == '\n':
            wynik += char
    i += 1
    return wynik


def info():
    return '''W szyfrze korzystamy z następującego klucza:
  M A F E K I N G
1 A B C D E F G H
2 I J K L M N O P
3 R S T U W X Y Z
Przykładowo słowo "HARCERZ" to "G1 M1 M3 F1 K1 M3 G"'''
