from atividade import *
import re
def letramaiuscula(): 
    if usuario[0].isupper():
        return
    else:
        print("ERRO! Requisitos de criação de usuário não atingidos.")
        quit()
def userx():
    especiais = "^[a-zA-Z0-9_\s]*$"
    if re.match(especiais, usuario):
        return 
    else: 
        print("ERRO! Requisitos de criação de usuário não atingidos.")
        quit() 
def espacouser():
    if " " in usuario or usuario.isspace():
        print("ERRO! Requisitos de criação de usuário não atingidos.")
        quit() 
    else: 
        return   
def maxuser():
    if len(usuario) > 30:
        print("ERRO! Requisitos de criação de usuário não atingidos.")
        quit()
    else: 
        return   