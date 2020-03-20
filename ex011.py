l = float(input('Digite a largura da parede'))
a = float(input('Digite a altura da parede'))

area = l*a

print('Sua dimensão é de {}x{} e sua área é de {}m². '.format(l,a,area))
tinta = area/2
print('você precisara de {} de tinta para pintar sua parede '.format(tinta))