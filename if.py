# oredem de procedencia aritimetica
#1 (), 2 **, 3 * / // %
#4 + -

a=int(input('dig um n.'))
b=int(input('dig outro n.'))
s= (a + b)

if s == 8:
    print(s)

elif s == 9:
    print('n é 8')
elif s == 0:
    print('n nao é nda')
else:
    print('n é 8 é', s)

if s != 8: # se s é diferente de 8:
    print(s * 4)