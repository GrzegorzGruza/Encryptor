# -*- coding: utf-8 -*-
def name():
    return 'Bacona'


def encrypt(text):
    wynik = ''
    pol = 'ąćęłńóśźż'
    Pol = 'ĄĆĘŁŃÓŚŹŻ'
    npol = 'acelnoszz'
    Npol = 'ACELNOSZZ'
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
           'y', 'z', 'j', 'u']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'v', 'W', 'X',
           'Y', 'Z', 'J', 'U']
    tab1 = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 'abaaa', 'abaab', 'ababa', 'ababb',
            'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb',
            'abaaa', 'baabb']
    Tab1 = ['Aaaaa', 'Aaaab', 'Aaaba', 'Aaabb', 'Aabaa', 'Aabab', 'Aabba', 'Aabbb', 'Abaaa', 'Abaab', 'Ababa', 'Ababb',
            'Abbaa', 'Abbab', 'Abbba', 'Abbbb', 'Baaaa', 'Baaab', 'Baaba', 'Baabb', 'Babaa', 'Babab', 'Babba', 'Babbb',
            'Abaaa', 'Baabb']

    i = 1
    for char in text:
        if char in pol:
            char = npol[pol.index(char)]
        elif char in Pol:
            char = Npol[Pol.index(char)]

        if char in tab:
            wynik += tab1[tab.index(char)]
        elif char in Tab:
            wynik += Tab1[Tab.index(char)]

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
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
           'y', 'z', 'j', 'u']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'v', 'W', 'X',
           'Y', 'Z', 'J', 'U']
    tab1 = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 'abaaa', 'abaab', 'ababa', 'ababb',
            'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb',
            'abaaa', 'baabb']
    Tab1 = ['Aaaaa', 'Aaaab', 'Aaaba', 'Aaabb', 'Aabaa', 'Aabab', 'Aabba', 'Aabbb', 'Abaaa', 'Abaab', 'Ababa', 'Ababb',
            'Abbaa', 'Abbab', 'Abbba', 'Abbbb', 'Baaaa', 'Baaab', 'Baaba', 'Baabb', 'Babaa', 'Babab', 'Babba', 'Babbb',
            'Abaaa', 'Baabb']

    i = 1
    for char in text:
        if char == 'a' or char == 'b' or char == 'A' or char == 'B':
            pom += char
            if i % 5 == 0:
                if pom in tab1:
                    wynik += tab[tab1.index(pom)]
                elif pom in Tab1:
                    wynik += Tab[Tab1.index(pom)]
                else:
                    wynik += pom
                pom = ''
        else:
            wynik += char
            i -= 1
        i += 1
    return wynik


def info():
    return '''Szyfr Bacona jest szyfrem, w którym tekst zaszyfrowany zawiera pięcioliterowe ciągi złożone z liter a i b. 
Szyfrowanie i odszyfrowanie przebiega według schematu:
a  = aaaaa      f  = aabab      l  = ababa      q  = abbbb      w  = babaa
b  = aaaab      g  = aabba      m  = ababb      r  = baaaa      x  = babab
c  = aaaba      h  = aabbb      n  = abbaa      s  = baaab      y  = babba
d  = aaabb      i/j = abaaa     o  = abbab      t  = baaba      z  = babbb
e  = aabaa      k  = abaab      p  = abbba      u/v = baabb     
Jeżeli chcemy zapisać wielką literę, np. "A", to pierwszy znak jest wielką literą, np. A=Aaaaa, B=Aaaab.
Przykładowo słowo "Harcerz" to "Aabbbaaaaabaaaaaaabaaabaabaaaababbb"'''
