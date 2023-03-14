'''Devemos utilizar o yield ou o generator quando há
 uma lista muito grande que queremos lidar, 
 para não termos que salvar esta na memória'''

def utilizandoYield(x):
  for i in range(x):
    if(i % 2 == 0):
      yield 'par'
    else:
      yield 'impar'

novogenerator = utilizandoYield(10)

for i in novogenerator:
  print(i)