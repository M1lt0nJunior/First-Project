import math
math.factorial(5)#5 é um exemplo pode ser qq n

import datetime
datetime.date.today()
datetime.date.isoformat(datetime.date.today()) #incrementa a apresentacao do resultado

from datetime import date #dessa forma peço a importaçado apenas do date entao uso a funçao do mesmo jeito de forma mais simples
date.isoformat(date.today())


dia = datetime.date.today()
#dia = datetime.date.today().day isto fara com que ele traga somente o dia, ou seja é uma parametro
print (dia)

f = math.factorial(5)
print(f)
