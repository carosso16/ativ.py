area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

m2 = 1 / 3

lata, preco_lata = 18, 80.00

latas = -(-area * m2 // lata)


preco_total = latas * preco_lata


print("Quantidade de latas de tinta a serem compradas:",latas)
print(f"Preço total das latas de tinta: R$ {preco_total:.2f}")
