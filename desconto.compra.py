valor_compra = float(input("Informe o valor total da compra: R$ "))

if valor_compra >= 100:
    valor_com_desconto = valor_compra * 0.9  # aplica 10% de desconto
    print(f"Você ganhou 10% de desconto! Valor final: R$ {valor_com_desconto:.2f}")
else:
    print(f"Você não ganhou desconto. Valor final: R$ {valor_compra:.2f}")
