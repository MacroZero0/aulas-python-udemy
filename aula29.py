"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

#print(1234)
#print(456)
#int('a')

numero_str = input('Vou dobrar o número que voce digitar: ')

try:
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')