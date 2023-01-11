#EX1 - CALCULE OPERADORES
n1 = int(input('Digite numero para saber seu antecessor e seu sucessor '))
antecessor = n1 - 1
sucessor = n1 + 1
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
print('O antecessor é {} e o sucessor é {} O dobro {} O triplo {} e sua raiz quadrada {:.1f}'.format(antecessor,sucessor,dobro,triplo,raiz))

#EX2 - CALCULE A MEDIA DE DUAS NOTAS
n2 = int(input('Digite a primeira nota: '))
n3 = int(input('Digite a segunda nota: '))
med = (n2 + n3)/2
print('A media deste aluno é {:.1f}'.format(med))

#EX3 - TRANSFORME METROS EM CENTIMETROS E MILIMETROS
n4 = int(input('Digite a medida em metros: '))
centimetros = n4 * 100
milimetros = centimetros * 10
print('{} Metros em centimetros é: {} e em milimetros é: {}'.format(n4,centimetros,milimetros))

# EX4 - Real para Dolar
n5 = float(input('Digite seu valor em reais: '))
dolar = 5.21
print('R$: {} em dolares vale USD$: {}'.format(n5, n5 / dolar))
