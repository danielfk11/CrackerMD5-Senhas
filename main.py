import hashlib
import os

flag = 0

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
YELLOW = "\033[0;93m"

hash_select = input("-> Selecione 1 para escolher uma palavra \n-> Selecione 2 para hash MD5\n-> ")

if hash_select not in ['1', '2']:
    print("Selecione um numero valido!")
    exit()

if hash_select == '1':

    hashMD5 = input("Escolha uma palavra para hashMD5: ")

    crypt = hashMD5.encode()
    hash = hashlib.md5(crypt)
    result = hash.hexdigest()
    
if hash_select == '2':

    has = input("Escolha o seu hash em MD5: ")
    result = has

arqs = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.txt')]

print("-------------------------------------------------")
print("-> WORDLISTS")
print(arqs)
print("-------------------------------------------------")

wrlist = input("Selecione uma wordist: ")

if wrlist not in arqs:
    print("Selecione uma wordlist valida!")
    print("->", arqs)
    exit()
else:
    pass_wrl = open(wrlist, 'r')
    

for passwrd in pass_wrl:

    pass_found = passwrd.encode('utf-8')
    digest = hashlib.md5(pass_found.strip()).hexdigest()

    print(RED, "->", passwrd)
    print(BLUE,"->", digest)
    print(YELLOW,"->", result)

    if digest == result:
        print(" Senha encontrada!")
        print(" ->", passwrd)
        flag = 1
        exit()

if flag == 0:
    print("Senha nao encontrada!")  