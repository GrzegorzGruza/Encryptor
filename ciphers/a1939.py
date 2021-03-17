# -*- coding: utf-8 -*-
def name():
    return '1939'


def encrypt(text):
    wynik = ''
    pop = ''
    pol = 'ąćęńóśźż'
    Pol = 'ĄĆĘŃÓŚŹŻ'
    npol = 'acenoszz'
    Npol = 'ACELNOSZZ'
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w',
           'y', 'z']
    Tab = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W',
           'Y', 'Z']
    tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    plus = [1, 9, 3, 9]
    plus_index = 0
    i = 1
    for char in text:
        if char in pol:
            char = npol[pol.index(char)]
        elif char in Pol:
            char = Npol[Pol.index(char)]
        if i > 1 and wynik[-1] != ' ' and pop != '\n':
            wynik += " "
        if char in tab:
            char = tab1[int(tab.index(char))] + plus[plus_index]
            plus_index += 1
            if plus_index == 4:
                plus_index = 0
            wynik += str(char)
        elif char in Tab:
            char = int(tab1[int(Tab.index(char))]) + int(plus[plus_index])
            plus_index += 1
            if plus_index == 4:
                plus_index = 0
            wynik += str(char)
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
    plus = [1, 9, 3, 9]
    plus_index = 0
    i = 1
    for char in text:
        if char == ' ' or i == len(text) or char == '\n':
            if len(pom) == 0:
                pom = ' '
            if pom in tab1:
                wynik += str(tab[tab1.index(pom) - int(plus[plus_index])])
                plus_index += 1
                if plus_index == 4:
                    plus_index = 0
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
Każdej liczbie przyporządkowujemy liczbę rowną pozycji, na której ona występuje, 
np literze B przyporząkowujemy liczbę 2.
Następnie do uzyskanych liczb dodajemy kolejne cyfry licbzy 1939,
Poniżej przedstawiony jest sposób szyfriwania słowa "HARCERZ":
	  (H) (A) (R)  (C) (E) (R)  (Z)
	  8    1   18   3   5   18   24 
	+ 1    9   3    9   1   9    3 
	= 9    10  21   12  6   27   27
'''
