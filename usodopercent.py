#variaveis:
fruta = input('Qual fruta?')
cor1 = 'azul'
cor2 = 'branco'
conta = 17/3

#imprimir na tela:
print('Meu suco favorito é de %s' %fruta)
print('meu cuco favorito é de {}'.format(fruta))
print('meu carro é {1}, porém o teto é {0} e as rodas são na cor {1}'.format(cor1, cor2, cor1))
print(conta)
print('formatando o valor de conta {:.2f} para duas casas decimais depois da virgula'.format(conta))
# %s = string, %d = decimal, %f = floating
