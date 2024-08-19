a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b= {nome2} a={nome1} a={nome1} c={nome3:.2f}' 
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)

# pode usar na hora com as chaves vazias
# ou nomealas para melhor organização do código
# lembrando que tudo que for depois depois do nomeado tbm precisa ser nomeado
# oque vem antes nao precisa.