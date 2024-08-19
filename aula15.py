nome = input('Qual o seu nome? ')
print(f'Olá {nome}, Qual a sua idade? ')
idade = int(input())
ano_atual = 2024
ano_nascimento = ano_atual - idade
print(f'{nome} nasceu no ano de: {ano_nascimento}')