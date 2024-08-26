primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')

if primeiro_valor > segundo_valor:
    print('O primeiro valor de:',primeiro_valor,'é maior que o segundo valor de:',segundo_valor)
elif primeiro_valor == segundo_valor:
    print('O primeiro valor de:',primeiro_valor,'é igual ao segundo valor de:',segundo_valor)
else:
    print('O segundo valor de:',segundo_valor,'é maior que o primeiro valor de:',primeiro_valor)