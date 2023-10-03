import string
import random

alphabet_string=string.ascii_lowercase
uppercase_alphabet_string=string.ascii_uppercase  
numbers_string=string.digits

keys= open("key.txt","r")
alphabet_and_numbers=keys.readline()     #CORE OF THE PASSAWORD (GONNA ADD RANDOMIZER IN FUTURE)
alphabet_sembols_numbers=keys.readline()

selected_key=int(input("Enter the number of shifts: "))
type=input("İf you wanna encyrpt a sentence type 'e',if you wanna decyrpt type 'd'.").lower()
upper_or_lower=(input("Should it be uppercase?(y or n)")).lower()


hashed=""



# def manager():
if (type=="e" and upper_or_lower=="n"):
    pas=input("Enter the passaword you want to enycrpt: ")
    for i in range(len(pas)):
        key=selected_key% len(alphabet_string)
        
        try:
            shifted_word=alphabet_and_numbers[alphabet_and_numbers.index(pas[i])+selected_key]
            if shifted_word=="\n":
                raise IndexError
            else:
                hashed+=shifted_word
        except IndexError:
            if(alphabet_and_numbers[alphabet_and_numbers.index(pas[i])]==alphabet_and_numbers[len(alphabet_and_numbers)-1]):
                shifted_word=alphabet_and_numbers[selected_key-1]
                hashed+=shifted_word
            else:
                surplus=(len(alphabet_and_numbers)-2)-alphabet_and_numbers.index(pas[i])
                shifted_word=alphabet_and_numbers[selected_key-surplus-1]
                # alphabet_and_numbers.index(pas[i])+key
                hashed+=shifted_word
# elif(type=="d" and upper_or_lower==)



