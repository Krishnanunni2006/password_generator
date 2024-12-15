import random as rd
import string as str
def gen_pass(length=12):
    if length <1:
        raise ValueError("Password must be atleast 1 character .")
    
    character_pool = str.ascii_letters + str.digits + '_' + '@' +'#'
    return ''.join(rd.choices(character_pool,k=length))

a=int(input("Enter the number of characters in the password"))
if __name__ == "__main__":
    print("Generated Password:",gen_pass(length=a))
