# -*- coding: utf-8 -*-
def name():
    return 'tabliczka mnożenia'


def encrypt(text):
    wynik = ''
    pop = ''
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'r', 's', 't', 'u',
           'w', 'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'O', 'Ó', 'P', 'R', 'S', 'T', 'U',
           'W', 'Y', 'Z']
    tab1 = ['1x1', '1x2', '1x3', '1x4', '1x5', '2x1', '2x2', '2x3', '2x4', '2x5', '3x1', '3x2', '3x3', '3x4', '3x5',
            '4x1', '4x2', '4x3', '4x4', '4x5', '5x1', '5x2', '5x3', '5x4', '5x5']

    i = 1
    for char in text:
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
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'r', 's', 't', 'u',
           'w', 'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'O', 'Ó', 'P', 'R', 'S', 'T', 'U',
           'W', 'Y', 'Z']
    tab1 = ['1x1', '1x2', '1x3', '1x4', '1x5', '2x1', '2x2', '2x3', '2x4', '2x5', '3x1', '3x2', '3x3', '3x4', '3x5',
            '4x1', '4x2', '4x3', '4x4', '4x5', '5x1', '5x2', '5x3', '5x4', '5x5']

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
    return '''W szyfrze korzystamy z następującej tabelki:
	  1 2 3 4 5
	1 A B C D E
	2 F G H I J
	3 K L Ł M N
	4 O Ó P R S
	5 T U W Y Z
Odnajdujemy szyfrowaną literę w tabelce, po czy zamiast niej wpisujemy wyrażenie: nr_wiersza x nr_kolumny,
np. "HARCERZ" to 2x3 1x1 4x4 1x3 1x5 4x4 5x5'''
