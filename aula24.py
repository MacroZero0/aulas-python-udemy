# Operadores in e not in
# Strings são interáveis
# 0 1 2 3 4 5
# O t á v i o
#-6-5-4-3-2-1
#nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
#print('á' in nome)
#print('z' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')