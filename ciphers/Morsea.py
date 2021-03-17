# -*- coding: utf-8 -*-
def name():
    return "Morse'a"


def encrypt(txt):
    wynik = ''
    tab1 = 'abcdefghijklmnopqrstuvwxyz1234567890'
    pol = 'ąćęłńóśźż'
    Pol = 'AĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    Tab1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tab = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
           '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..--', '...--',
           '...-', '.....', '-....', '--...', '---..', '----.', '-----']
    i = 1;
    for char in txt:
        if char in pol:
            char = npol[pol.index(char)]
        if char in Pol:
            char = Npol[Pol.index(char)]
        elif char in tab1:
            wynik += tab[tab1.index(char)]
        elif char in Tab1:
            wynik += tab[Tab1.index(char)]
        elif char != ' ' and char != '.':
            wynik += char
        if char != '\n':
            wynik += '/'
        if char == '.':
            wynik += '/'
        i += 1
    return wynik


def decrypt(txt):
    ostatni = '.'
    wynik = ''
    pom = ''
    tab1 = 'abcdefghijklmnopqrstuvwxyz1234567890'
    Tab1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tab = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
           '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..--', '...--',
           '...-', '.....', '-....', '--...', '---..', '----.', '-----']
    for char in txt:
        if char == '/' and ostatni == ' ':
            wynik = wynik[:-1]
            wynik += '.'
        elif char == '/' and pom == '':
            wynik += ' '
            ostatni = ' '
        elif char == '/':
            if pom in tab:
                wynik += tab1[tab.index(pom)]
            else:
                wynik += pom
            pom = ''
            ostatni = '.'
        elif char != '\n':
            pom += char
            ostatni = '.'
        if char == '\n':
            wynik += '\n'
    return wynik


def info():
    return '''Każdemu znakowi odopoiada ciąg kropek i kresek. Poniżej znajduje się spos znaków łacińskich oraz cyfr zaszyfrowanych "Morse'm":
A • —          H • • • •        O — — —         U • • —         1 • — — — —        6 — • • • •
B — • • •      I • •            P • — — •       V • • • —       2 • • — — —        7 — — • • • 
C — • — •      J • — — —        Q — — • —       W • — —         3 • • • — —        8 — — — • • 
D — • •        K — • —          R • — •	        X — • • —       4 • • • • —        9 — — — — •
E •            L • — • •        S • • •         Y — • — —       5 • • • • •        0 — — — — —
F • • — •      M — —            T —             Z — — • •
G — — •        N— •
Znaki odziela się pojedynczym ukośnikiem('/'), słowo podwójnym('//'), a zdania postrójnym('///')'''
