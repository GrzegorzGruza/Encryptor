# -*- coding: utf-8 -*-
from tkinter import *
import sys, os, random

# inicjacja pliku result.py
link = os.getcwd()
file_list = os.listdir(link + '/ciphers')

plik = open('result.py', 'w')
plik.write("#-*- coding: utf-8 -*-\n")
plik.write("#!/usr/bin/env python\n")
plik.write("import random\n")
for i in file_list:
    if i[-3:] == '.py':
        msg = "import %s\n" % i[:-3]
        plik.write(msg)
plik.write("def result(name, option, txt):")

for i in file_list:
    if i[-3:] == '.py':
        msg = '''\n\tif name=='%s' and option=='encrypt':
		return %s.encrypt(txt)''' % (i[:-3], i[:-3])
        plik.write(msg)
        msg = '''\n\tif name=='%s' and option=='decrypt':
		return %s.decrypt(txt)''' % (i[:-3], i[:-3])
        plik.write(msg)
        msg = '''\n\tif name=='%s' and option=='info':
		return %s.info()''' % (i[:-3], i[:-3])
        plik.write(msg)
        msg = '''\n\tif name=='%s' and option=='name':
		return %s.name()''' % (i[:-3], i[:-3])
        plik.write(msg)
plik.close()
sys.path.append(link + '/ciphers')
import result

c1 = "#85A314"
c2 = "white"
# Tworzenie głównego okna
root = Tk()
root.title("Szyfrator")
root.configure(bg=c1)

# --------------------PRZYCISKI----------------------
f1x = Frame(root, bg=c1)
# tworzenie napisu do przycisku wyboru szyfrowanie
msg_check1 = Message(f1x, text="Szyfruj", width="200", bg=c1, font=("Museo 300", "15"), fg="white")
msg_check1.pack(side=LEFT, anchor=NW)
# tworzenie napisu do przycisku wyboru rozszyfrowywanie
msg_check2 = Message(f1x, text="Rozszyfruj", width="200", bg=c1, font=("Museo 300", "15"), fg="white")
msg_check2.pack(side=LEFT, anchor=NW, padx=60)
f1x.pack(side=LEFT and TOP, anchor=NW, padx=50)

f1 = Frame(root, bg=c1)
# tworzenie przycisku wyboru szyfrowanie
check1 = Checkbutton(f1, text="", bg=c1, activebackground=c1, font=("Museo 300", "15"))
check1.select()
check1.pack(side=LEFT, expand=NO, padx=25)
# tworzenie przycisku wyboru rozszyfrowanie
check2 = Checkbutton(f1, text="", bg=c1, activebackground=c1, font=("Museo 300", "15"))
check2.pack(side=LEFT and TOP, padx=100, expand=NO)
f1.pack(side=LEFT and TOP, anchor=NW, padx=50)
# ----------------------------------------------------


# -------NAPISY DO LISTY WYBORU I INFO O SZYFRZE-------
f2 = Frame(root, bg=c1)
msg_lbox = Message(f2, text="Lista dostępnych szyfrów:", width="300", bg=c1, font=("Museo 300", "15"), fg="white")
msg_lbox.pack(side=LEFT, anchor=NW)
msg_info = Message(f2, text="Informacja o szyfrze:", width=300, padx=200, anchor=NW, bg=c1, font=("Museo 300", "15"),
                   fg="white")
msg_info.pack(side=LEFT)
f2.pack(side=LEFT and TOP, anchor=NW, padx=50)
# -----------------------------------------------------


# ------LISTA WYBORU I INFO O SZYFRZE-------------------
f3 = Frame(root, bg=c1)
f3x = Frame(f3, bg=c1)
# scrollbar
scrollbar = Scrollbar(f3x)
scrollbar.pack(side=RIGHT, expand=YES, fill=Y)
lbox = Listbox(f3x, width=50, bg=c2)
list_name = []
for i in file_list:
    if i[-3:] == '.py':
        lbox.insert(END, result.result(i[:-3], 'name', ''))
        list_name.append(i[:-3])
lbox.pack(side=BOTTOM, expand=YES, fill=Y)
lbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbox.yview)
f3x.pack(side=LEFT, anchor=NW, expand=YES, fill=Y, padx=25)

info = Text(f3, width=150, height=10, bg=c2)
info.pack(side=LEFT, expand=YES, fill=Y, padx=25)

f3.pack(side=LEFT and TOP, anchor=NW, padx=25)

lbox.selection_set(0, last=None)
lbox_select = 0
# ---------------------------------------------------

# --------------POLA Z TEKSTEM-----------------------
f4 = Frame(root, bg=c1)
# pole do wpisywania tekstu
msg_input = Message(f4, text="Tu wpisz tekst:", width=200, bg=c1, font=("Museo 300", "15"), fg="white")
msg_input.pack(side=TOP, expand=NO)
txt_input = Text(f4, width=150, height=5, bg=c2)
txt_input.pack(side=TOP, expand=YES, fill=BOTH)
# ple wypisywania tekstu
msg_output = Message(f4, text="Rezultat:", width=200, bg=c1, font=("Museo 300", "15"), fg="white")
msg_output.pack(side=TOP, expand=NO)
txt_output = Text(f4, width=150, height=5, bg=c2)
txt_output.pack(side=TOP, expand=YES, fill=BOTH)

# ---------------------------------------------------


# -----------POLE DODANIA SZYFRÓW--------------------
add = Message(f4, text="Chcesz dodać więcej szyfrów? Kliknij tutaj.", font=("Museo 300", "10"), width=400, bg='red2',
              fg='white')
add.pack(side=LEFT and TOP, anchor=S)
f4.pack(side=LEFT, anchor=NW, padx=50, pady=20, expand=YES, fill=BOTH)
# ---------------------------------------------------


# -----------------ZDARZENIA-----------------------
# pola z tekstem
memory_info = ""
con = 1


def code(event):
    if len(lbox.curselection()) != 0:
        globals()["lbox_select"] = lbox.curselection()[0]
    else:
        lbox.selection_set(globals()["lbox_select"], last=None)
    info.delete(0.1, END)
    if len(lbox.curselection()) == 0:
        info.insert(0.1, memory_info)
        return
    name = list_name[lbox_select]
    if con % 2 == 1:
        option = "encrypt"
    else:
        option = "decrypt"
    txt = txt_input.get(0.1, END)
    txt_output.delete(0.1, END)
    txt_output.insert(0.1, result.result(name, option, txt))
    globals()["memory_info"] = result.result(name, "info", txt)
    info.insert(0.1, globals()["memory_info"])


# checkboxy
def changeCheckbutton1(event):
    globals()["con"] += 1
    check1.toggle()


def changeCheckbutton2(event):
    globals()["con"] += 1
    check2.toggle()


def changeMessageCheckbutton(event):
    globals()["con"] += 1
    check1.toggle()
    check2.toggle()


check1.bind("<Button-1>", changeCheckbutton2)
check2.bind("<Button-1>", changeCheckbutton1)
txt_input.bind("<Any-KeyRelease>", code)
lbox.bind("<ButtonRelease-1>", code)
lbox.bind("<Any-KeyRelease>", code)
check1.bind("<ButtonRelease-1>", code)
check2.bind("<ButtonRelease-1>", code)
info.bind("<Any-KeyRelease>", code)
msg_check1.bind("<Button-1>", changeMessageCheckbutton)
msg_check2.bind("<Button-1>", changeMessageCheckbutton)
msg_check1.bind("<ButtonRelease-1>", code)
msg_check2.bind("<ButtonRelease-1>", code)


# info o dodawaniu
def information_add(event):
    toplevel = Toplevel(root, width=700)
    toplevel.title("Instrukcja dodawania szyfrów")
    top_text = '''Żeby dodać szyfr postępuj zgodnie z następującą instrukcją:
1.	Stwórz plik w pythonie o rozszerzeniu ".py", np. "gaderypoluki.py"
2.	Dodaj do pliku następujące funkcje:
	\t-name(), która zwaracca nazwę szyfru, wyświetlaną w liście wyboru
	\t-encrypt(txt), która w zależności od txt zwraca zaszyfrowany tekst
	\t-decrypt(txt), która w zależności od txt zwraca rozszyfrowany tekst
	\t-info(), która zwraca informacje o szyfrze
3.	Utworzony plik dodaj do folderu "ciphers" '''
    msg = Message(toplevel, text=top_text, width=700, font=("Museo 300", "10", "bold"), fg=c1, bg=c2)
    msg.pack(expand=YES, fill=BOTH)


add.bind("<Button-1>", information_add)
# ------------------------------------------------

# root.state('zoomed')
m = root.maxsize()
root.geometry('{}x{}+0+0'.format(*m))
root.mainloop()
