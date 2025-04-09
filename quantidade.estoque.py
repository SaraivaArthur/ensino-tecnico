estoque_minimo = 10

quantidade_desejada = int(input("Digite a quantidade desejada: "))

if quantidade_desejada < estoque_minimo:
    print("Produto disponível em estoque!")
else 
    print("Quantidade indisponível. Estoque insuficiente.")
