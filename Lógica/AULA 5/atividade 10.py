peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print("peso normal")
if imc >= 25 and imc <= 30:
    print("acima do peso")
elif imc > 25:
    print("obeso")