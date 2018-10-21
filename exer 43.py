peso = float(input('Qual é o seu peso?(Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo so peso normal')
elif 18.5 <= imc < 25:
    print('Voce esta na faixa de peso normal')
elif 30 <= imc < 40:
    print('Voce está em sobrepeso')
elif imc >= 40:
    print('Voce esta em obesidade morbida, cuidado.')
