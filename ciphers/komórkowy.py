# -*- coding: utf-8 -*-
def name():
    return 'komórkowy'


def encrypt(text):
    wynik = ''
    pop = ''
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    tab1 = ['2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7', '77', '777',
            '7777', '8', '88', '888', '9', '99', '999', '9999']

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
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    tab1 = ['2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7', '77', '777',
            '7777', '8', '88', '888', '9', '99', '999', '9999']

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
(2)ABC, (3)DEF, (4)GHI, (5)JKL, (6)MNO, (7)PQRS, (8)TUV, (9)WXYZ.
 
Każda litera po zaszyfrowaniu jest ciągiem cyfr. Jeżeli występuje ona na 
k-tej pozycji w n-tej grupie, to ciąg ten składa się z cyfry n powtórzonej k-krotnie,
np. litera „e” występuje na 2. miejscu w 3. grupie, zatem po zaszyfrowaniu będzie ona wyglądała następująco: „33”.
Przykładowo słowo "harcerz" to "44 2 777 222 33 777 9999" '''
