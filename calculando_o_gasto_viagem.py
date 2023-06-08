distancia =float(input('Qual a distancia da viagem?\n'))
print('Sua viagem de {}km, começa agora'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else :
    preço = distancia *0.45
print(' Sua viagem custará a bagatela de R${:.2f}.Lets bora ?'.format(preço))
