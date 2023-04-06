from cryptographyFramework import *
from func_usuarios import *
from func_senha import *
import re

def valida_login():
    usuario = input("Crie um nome de usuário: ")
    letramaiuscula(usuario)
    userx(usuario)
    espacouser(usuario)
    maxuser(usuario)
    senha = input("Crie uma senha: ")
    minpass(senha)
    passx(senha)
    numpass(senha)
    passmaiuscula(senha)
    passminuscula(senha)
    print("Login realizado com sucesso.")
    initializeWrite()
    user = usuario
    password = senha
    mensagem = input("Digite uma mensagem para criptografar:")
    mencript = encryptMessage(user, password, mensagem)
    saveNewLine(mencript)
    if len(mensagem) > 70:
        print("Erro! a mensagem deve ter no máximo 70 caracteres.")
    else:
        print("Mensagem criptografada com sucesso.")



valida_login()



