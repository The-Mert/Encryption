import string
import random

alphabet_string=string.ascii_lowercase
uppercase_alphabet_string=string.ascii_uppercase  
numbers_string=string.digits


keys= open("key.txt","r")
alphabet_and_numbers=keys.readline()     #CORE OF THE PASSAWORD (GONNA ADD RANDOMIZER IN FUTURE)
alphabet_sembols_numbers=keys.readline()
alphabet_and_numbers_uppercase=keys.readline()

selected_key=int(input("Enter the number of shifts: "))
type=input("İf you wanna encyrpt a sentence type 'e',if you wanna decyrpt type 'd'.").lower()
upper_or_lower=(input("Should it be uppercase?(y or n)")).lower()

hashed=""



    

def encyrpt():    #  Encyrpt
    global hashed,alphabet_and_numbers,alphabet_and_numbers_uppercase
    pas=input("Enter the passaword you want to enycrpt: ")

    if(upper_or_lower=="y"):
        core_line=alphabet_and_numbers_uppercase
    else:
        core_line=alphabet_and_numbers

    for i in range(len(pas)):
        key=selected_key% len(f"{core_line}")
        
        try:
            shifted_word=core_line[core_line.index(pas[i])+key]

            if shifted_word=="\n":
                raise IndexError
            else:
                hashed+=shifted_word

        except IndexError:
            surplus=(len(f"{core_line}")-2)-f"{core_line}".index(pas[i])
            shifted_word=f"{core_line}"[key-surplus-1]
            hashed+=shifted_word

# def decyrpt():

if(type=="e"):
    encyrpt()
# elif(type=="d"):
#     decyrpt()




print(hashed)
