
peso_peixes = float(input("Digite o peso dos peixes (em quilos): "))


limite_peso = 50

excesso = max(0, peso_peixes - limite_peso)
multa = excesso * 4.00


print("Peso de peixes:" ,peso_peixes, "kg")
if excesso > 0:
    print("Excesso:",excesso, "kg")
    print(f"Multa a ser paga: R$ {multa:.2f}")
else:
    print("Não há excesso. Nenhuma multa será aplicada.")
