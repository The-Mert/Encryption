import string
import random
from tkinter import *
from tkinter import messagebox


alphabet_string=string.ascii_lowercase
uppercase_alphabet_string=string.ascii_uppercase  
numbers_string=string.digits


keys= open("key.txt","r",encoding='utf-8')
alphabet_and_numbers=keys.readline()     #CORE OF THE PASSAWORD (GONNA ADD RANDOMIZER IN FUTURE)
alphabet_sembols_numbers=keys.readline()
alphabet_and_numbers_uppercase=keys.readline()


selected_key=int(input("Enter the number of shifts: "))
upper_or_lower=(input("Should it be uppercase?(y or n)")).lower()


def show_info(hashed):
    info_box=Tk()
    info_box.geometry("")
    text=StringVar()
    text.set(hashed)
    pass_label=Entry(info_box,font=("Helvetica",25),bd=0,state="readonly",textvariable=text)
    pass_label.pack(pady=30)
    info_box.mainloop()

def encyrpt():    #  Encyrpt
    global hashed,alphabet_and_numbers,alphabet_and_numbers_uppercase,app
    pas=input("Enter the passaword you want to enycrpt: ")
    hashed=""
    app=input("Type the name the app or site you want to encyrpt: ")

    if(upper_or_lower=="y"):
        core_line=alphabet_and_numbers_uppercase
    else:
        core_line=alphabet_and_numbers

    for i in range(len(pas)):
        key=selected_key% len(core_line)
        
        try:
            shifted_word=core_line[core_line.index(pas[i])+key]

            if shifted_word=="\n":
                raise IndexError
            else:
                hashed+=shifted_word

        except IndexError:
            surplus=(len(core_line)-2)-core_line.index(pas[i])
            shifted_word=core_line[key-surplus-1]
            hashed+=shifted_word
    save(app)
    show_info(hashed)
    
def save(name):
    global selected_key,app

    cyrpted_file=open(r".\SSS.txt","r")
    last_line=cyrpted_file.readline()
    if(last_line==""):
        cyrpted_file=open(r".s\SSS.txt","a")
        cyrpted_file.writelines([f"{name} ,  {selected_key}"])
    else:
        cyrpted_file=open(r".\SSS.txt","a")
        cyrpted_file.writelines([f"\n{name} ,  {selected_key}"])

encyrpt()

