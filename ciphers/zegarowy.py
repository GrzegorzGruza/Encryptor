# -*- coding: utf-8 -*-
def name():
    return 'zegarowy'


def encrypt(txt):
    wynik = ''
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    tab1 = 'abcdefghijklłmnoprstuwyz'
    Tab1 = 'ABCDEFGHIJKLŁMNOPRSTUWYZ'
    i = 0;
    pop = ''
    for char in txt:
        i += 1
        if char in pol:
            char = npol[pol.index(char)]
        if char in Pol:
            char = Npol[Pol.index(char)]
        if i > 1 and wynik[-1] != ' ' and pop != '\n':
            wynik += " "
        if char in tab1:
            for i in range(0, 24):
                if tab1[i] == char:
                    wynik += str(i + 1)

        elif char in Tab1:
            for i in range(0, 24):
                if Tab1[i] == char:
                    wynik += str(i + 1)
        else:
            wynik += char
        pop = char
    return wynik


def decrypt(text):
    # print (len(text))
    wynik = ''
    pom = ''
    i = 1
    tab1 = 'abcdefghijklłmnoprstuwyz'
    Tab1 = 'ABCDEFGHIJKLŁMNOPRSTUWYZ'
    tab = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24']

    for char in text:
        if char == ' ' or i == len(text) or char == '\n':
            if len(pom) == 0:
                pom = ' '
            if pom in tab:
                wynik += tab1[tab.index(pom)]
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
    return '''W szyfrując korzystamy z następującego alfabetu:
A B C D E F G H I J K L Ł M N O P R S T U W Y Z.
Powyższy alfabet posiada 24 znaki. 
Każdemu z nich przypisujemy wartość równą pozycji, na której występuje w alfabecie,
np. A=1, B=2, J=10, Z=24. Po zaszyfrowaniu wszystkie znaki odzielamy spacjami. 
Przykładowo słowo "WILK" to "22 9 12 11"
Odszyfrowujemy w sposób odwrotny.'''
