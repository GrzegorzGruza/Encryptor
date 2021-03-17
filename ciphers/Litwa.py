# -*- coding: utf-8 -*-

import random


def name():
    return 'Litwa'


def encrypt(text):
    wynik = ''
    pop = ''
    i = 0
    for char in text:
        i += 1
        if i > 1 and wynik[-1] != ' ' and pop != '\n':
            wynik += " "
        if char == 'L' or char == 'l':
            wynik += "1"
        elif char == 'I' or char == 'i':
            wynik += "2"
        elif char == 'T' or char == 't':
            wynik += "3"
        elif char == 'W' or char == 'w':
            wynik += "4"
        elif char == 'O' or char == 'o':
            wynik += str(random.sample([5, 6, 13, 15], 1)[0])
        elif char == 'J' or char == 'j':
            wynik += str(random.sample([7, 16], 1)[0])
        elif char == 'C' or char == 'c':
            wynik += "8"
        elif char == 'Z' or char == 'z':
            wynik += str(random.sample([9, 11], 1)[0])
        elif char == 'Y' or char == 'y':
            wynik += "10"
        elif char == 'N' or char == 'n':
            wynik += "12"
        elif char == 'M' or char == 'm':
            wynik += "14"
        elif char == 'A' or char == 'a':
            wynik += "17"
        else:
            wynik += char
        pop = char
    # print (wynik[len(wynik)-1])
    # if wynik[-1]==',':
    #	return wynik[:-1]
    return wynik


def decrypt(text):
    wynik = ''
    pom = ''
    i = 1
    for char in text:
        if char == ' ' or i == len(text) or char == '\n':
            if len(pom) == 0:
                pom = ' '
            if pom == '1':
                wynik += 'l'
            elif pom == '2':
                wynik += 'i'
            elif pom == '3':
                wynik += 't'
            elif pom == '4':
                wynik += 'w'
            elif pom in ['5', '6', '13', '15']:
                wynik += 'o'
            elif pom in ['7', '16']:
                wynik += 'j'
            elif pom == '8':
                wynik += 'c'
            elif pom in ['9', '11']:
                wynik += 'z'
            elif pom == '10':
                wynik += 'y'
            elif pom == '12':
                wynik += 'n'
            elif pom == '14':
                wynik += 'm'
            elif pom == '17':
                wynik += 'a'

            else:
                wynik += pom
            pom = ''
        else:
            pom += char
        if char == '\n':
            wynik += char
        i += 1
    return wynik


def info():
    return '''Cała umiejętność szyfrowania tym sposobem, 
polega na zamienieniu litery w cyfrę za pomocą następującego klucza:
	L I T W O O J C Z Y  Z  N  O  M  O  J  A
	1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
Np. litera A to 17, litera O to 5 (ale też 6, 13 czy 15), itd.
Jeżeli litery nie ma w kluczu, piszemy ją w podstawowej formie, jak np. literę d.
Dla przykładu słowo HARCERSTWO to „H 17 R 8 E R S 3 4 15” lub "H 17 R 8 E R S 3 4 6".

Rozszyfrowywanie polega na wykonywaniu operacji odwrotnych'''
