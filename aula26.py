"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
(Caractere)(><^)(quantidade)
> - Esquerda
< - direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')       
print(f'{variavel: >10}')   #adiciona 10 espaços á direita
print(f'{variavel: <10}')   #adiciona 10 espaços á esquerda
print(f'{variavel: ^10}')   #adiciona espaços dos dois lados para centralizar
print(f'{1000.1241241244124:,.1f}')