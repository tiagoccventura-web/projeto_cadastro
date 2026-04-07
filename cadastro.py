import hashlib
import pandas as pd # type: ignore
from tabulate import tabulate

usuarios = []


# Lista simulando emails já cadastrados

usuarios_cadastrados = ["teste@email.com", "outro@email.com"]

nome = (input("Digite o seu nome: "))
sobrenome = (input("Digite o seu sobrenome: "))

#Validdação de CPF

cpf = input("Digite o seu CPF: ").strip()  # remove espaços

cpf = cpf.replace(".", "").replace("-", "") # remove pontos e traços, se houver

# validação
cpf_valido = cpf.isdigit() and len(cpf) == 11
if not cpf_valido:
    print("CPF inválido, digite apenas números com 11 dígitos.")
    exit()  # encerra o programa se inválido

#Validação de idade

idade = int(input("Digite a sua idade: "))
if idade < 18:
    print("Desculpe, você precisa ser maior de idade para se cadastrar.")
    exit()  # encerra o programa
email = (input("Digite o seu email: "))
senha1 = (input("Digite a sua senha: "))
senha2 = (input("Confirme a sua senha: "))


#Validação de email ja cadastrado

if email in usuarios_cadastrados:   
    print("Email já cadastrado, por favor, tente outro.")
    exit()

#Validação de senha

if senha2 != senha1:
    print("As senhas não são iguais, por favor, tente novamente.")
    exit()  # encerra o programa

# Transformando a senha em hash
senha_hash = hashlib.sha256(senha1.encode()).hexdigest()

#Adiciona o e-mail à lista de usuários cadastrados

usuarios_cadastrados.append(email)

# Criando um dicionário com todos os dados do usuário
usuario = {
    "nome": nome,
    "sobrenome": sobrenome,
    "cpf": cpf,
    "idade": idade,
    "email": email,
    "senha": senha_hash  # guarda o hash

}

# Adicionando à lista de usuários
usuarios.append(usuario)
print(f"Cadrasto realizado com sucesso! Seja bem-vindo(a) {nome}!")

#print(usuario)  # mostra os dados armazenados

df = pd.DataFrame(usuarios) #armazena os dados em tabela 
df.to_csv("usuarios.csv", index=False) #armazena pra colocar no Excel
print(tabulate(df, headers='keys', tablefmt='grid'))