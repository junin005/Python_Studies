l = int(input('Informe a largura da parede: '))
a = int(input('Informe a altura da parede: '))
area = l * a
litro_tinta = 2
quant_tinta = area / litro_tinta
print(f'Voce precisara de {quant_tinta} litros para pintar uma parede de {area} metros quadrados.')