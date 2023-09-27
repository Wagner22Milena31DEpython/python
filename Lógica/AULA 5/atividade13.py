bruto = float(input("digite seu salario bruto"))
if  bruto <= 2112.00:
    print("voce não precisa pagar imposto de renda")
elif bruto <= 2826.65 and bruto > 2112.00:
    print("voce tera que pagar 7.5% de imposto de renda")
elif bruto >= 2826.66 and bruto < 3751.05:
    print("voce tera que pagar 15% de imposto de renda")
else:
    print("voce tera que pagar 27.5% de imposto de renda")