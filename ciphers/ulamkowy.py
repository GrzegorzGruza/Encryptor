# -*- coding: utf-8 -*-
def name():
    return 'ułamkowy'


def encrypt(text):
    wynik = ''
    pop = ''
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w',
           'x', 'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W',
           'X', 'Y', 'Z']
    tab1 = ['1/1', '2/1', '3/1', '4/1', '5/1', '1/2', '2/2', '3/2', '4/2', '5/2', '1/3', '2/3', '3/3', '4/3', '5/3',
            '1/4', '2/4', '3/4', '4/4', '5/4', '1/5', '2/5', '3/5', '4/5', '5/5']

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
    Npol = 'ACELNOSZZ'
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w',
           'x', 'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W',
           'X', 'Y', 'Z']
    tab1 = ['1/1', '2/1', '3/1', '4/1', '5/1', '1/2', '2/2', '3/2', '4/2', '5/2', '1/3', '2/3', '3/3', '4/3', '5/3',
            '1/4', '2/4', '3/4', '4/4', '5/4', '1/5', '2/5', '3/5', '4/5', '5/5']

    i = 1
    for char in text:
        if char == ' ' or i == len(text) or char == '\n':
            if len(pom) == 0:
                pom = ' '
            if pom in tab1:
                wynik += tab[tab1.index(pom)]
            else:
                wynik += pom
            pom = ''
        elif char != '\n':
            pom += char
        if char == '\n':
            wynik += char
    i += 1
    return wynik


def info():
    return '''W szyfrze korzystamy z następujących grup:
(1)ABCDE, (2)FGHIJ, (3)KLŁMN, (4)OPRSTU, (5)UWXYZ.
 
Każda litera po zaszyfrowaniu jest postaci a/b
(gdzie b to numer grupy, natomiast a to pozycja na której występuje w tej grupie)
Np. litera „e” występuje na 5. miejscu w 1. grupie, zatem po zaszyfrowaniu będzie ona wyglądała następująco: „5/1”.
Przykładowo słowo "harcerz" to "3/2 1/1 3/4 3/1 5/1 3/4 5/5" '''
