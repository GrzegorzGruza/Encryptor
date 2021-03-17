# -*- coding: utf-8 -*-
def name():
    return 'liczbowy'


def encrypt(text):
    wynik = ''
    pop = ''
    pol = 'ąćęńóśźż'
    Pol = 'AĆĘŃÓŚŹŻ'
    npol = 'acenoszz'
    Npol = 'ACELNOSZZ'
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w',
           'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W',
           'Y', 'Z']
    tab1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24']

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
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w',
           'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W',
           'Y', 'Z']
    tab1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24']
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
    return '''W szyfrze korzystamy z następującego alfabetu:
A B C D E F G H I J K L Ł M N O P R S T U W Y Z
Każdej liczbie przyporządkowujemy liczbę rowną pozycji, na której ona występuje, np. A=1, B=2.
Przykładowo "HARCERZ" to "8 1 18 3 5 19 24"'''
