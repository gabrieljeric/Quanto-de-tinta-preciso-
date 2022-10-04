'''
Quanto de tinta será necessário para pintar uma parede?
O usuário deve informar a altura e largura da parede e rendimento da lata de tinta para obter a quantidade necessária de tinta.
O programa irá informar quanto de tinta vocÊ precisa.
'''

rendimento = input('Qual é o rendimento na embalagem da lata?')
altura = input('Qual é a altura da parede a ser pintada?')
largura = input('Qual é a largura da parede a ser pintada?')

def calculo_tinta():
  area = altura * largura
  total = area / rendimento
  print(f'Você precisa de {total} latas de tinta')

calculo_tinta