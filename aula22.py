# Operadores lógicso
# and (e) or (ou) not (não)
# and - Todas as condições precisa ser verdadeiras.
# Se qualquer valor considerado falso.
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que voce já viu)
# 0 0.0 '' False
# também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '3020'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'    # aqui foi feito um if na propria variável
print(senha)