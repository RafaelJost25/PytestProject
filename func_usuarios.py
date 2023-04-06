import re
def letramaiuscula(usuario): 
    if usuario[0].isupper():
        return
    else:
        print("ERRO! Requisitos de criação de usuário não atingidos.")
        quit()
def userx(usuario):
    especiais = "^[a-zA-Z0-9_\s]*$"
    if re.match(especiais, usuario):
        return 
    else: 
        print("ERRO! Requisitos de criação de usuário não atingidos.")
        quit() 
def espacouser(usuario):
    if " " in usuario or usuario.isspace():
        print("ERRO! Requisitos de criação de usuário não atingidos.")
        quit() 
    else: 
        return   
def maxuser(usuario):
    if len(usuario) > 30:
        print("ERRO! Requisitos de criação de usuário não atingidos.")
        quit()
    else: 
        return   