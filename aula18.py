# if / elif      / else
# se / se não se / se não

# usando o debuger com python e breakpoint
# settings.json > gliph = para mostrar o ponto vermelho do lado da linha de codigo

condicao1 = True    #marcando o breakpoint nessa linha esta condição não sera carregada
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1') # condição falsa então não será executado
elif condicao2:
    print('Código para condição 2') # condição falsa então não será executado
elif condicao3:
    print('Código para condição 3') # condição Verdadeira então será executado
elif condicao4:
    print('Código para condição 4') # condição falsa então não será executado
else:
    print('Nenhuma condição foi satisfeita') # se nenhum if por executado, else será exec.

if 10 == 10:
    print('Outro if')
    
print('Fora do if')