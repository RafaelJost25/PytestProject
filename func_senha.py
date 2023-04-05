import re
from atividade import *
def minpass():
    if len(senha) < 10:
        print("ERRO! Requisitos de criação de senha não atingidos.")
        quit() 
    else:
        return
def passx():
    especiais = "^[a-zA-Z0-9_\s]*$"
    if re.match(especiais, senha):
        print("ERRO! Requisitos de criação de senha não atingidos.")
        quit() 
    else: 
        return
def numpass():
    numero = False
    for num in senha:
        if num.isdigit():
            numero = True
            break
    if not numero:
        print("ERRO! Requisitos de criação de senha não atingidos.")
def passmaiuscula(): 
    maiuscula = False
    for x in senha:
        if x.isupper():
            maiuscula = True
            return
    if not maiuscula:
        print("ERRO! Requisitos de criação de senha não atingidos.")   
def passminuscula(): 
    minuscula = False
    for x in senha:
        if x.islower():
            minuscula = True
            return
    if not minuscula:
        print("ERRO! Requisitos de criação de senha não atingidos.")    