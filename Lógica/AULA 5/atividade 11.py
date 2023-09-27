preço = float(input("digite o preço"))
pagamento1 = input("ira pagar á vista em dinheiro ou cheque? digite apenas sim caso seja dessa forma")
pagamento2 = input("ira pagar á vista no cartão de credito? digite apenas sim caso seja dessa forma")
pagamento3 = input("ira dividir em duas vezes sem juros? digite apenas sim se for dessa forma")
pagamento4 = input("ira pagar em duas vezes o preço normal da etiqueta com juros? digite apenas sim se for dessa forma")
if pagamento1:
    input(preço-(preço * 0.10))
elif pagamento2:
    input(preço - (preço * 0.15))
if pagamento3:
    input(preço)
elif pagamento4:
    input(preço + (preço * 0.10))