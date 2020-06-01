import time
contador = 0
while contador < 10: #conta de 0 a 9, logo o loop vira infinito
      print('anda n')
      contador = contador + 1 #com esse comando ele conta ate o 9 e acrescenta + 1 faz contador = 10 e para
      if contador == 6:
          print('chegamos no 6')
          break
      time.sleep(1)#aguarda 1 segundo para seguir cada linha
print('agora deu')
