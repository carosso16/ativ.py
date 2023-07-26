import math


area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))


cobertura_tinta_litros_por_m2 = 1 / 6

capacidade_lata_tinta_litros, preco_lata_tinta = 18, 80.00

capacidade_galao_tinta_litros, preco_galao_tinta = 3.6, 25.00

litros_tinta_necessarios = area_a_ser_pintada * cobertura_tinta_litros_por_m2 * 1.1

quantidade_latas_tinta = math.ceil(litros_tinta_necessarios / capacidade_lata_tinta_litros)
quantidade_galoes_tinta = math.ceil(litros_tinta_necessarios / capacidade_galao_tinta_litros)

preco_total_latas = quantidade_latas_tinta * preco_lata_tinta

preco_total_galoes = quantidade_galoes_tinta * preco_galao_tinta

quantidade_latas_mistura = math.ceil(litros_tinta_necessarios / capacidade_lata_tinta_litros)
quantidade_galoes_mistura = math.ceil((litros_tinta_necessarios % capacidade_lata_tinta_litros) / capacidade_galao_tinta_litros)

preco_total_mistura = (quantidade_latas_mistura * preco_lata_tinta) + (quantidade_galoes_mistura * preco_galao_tinta)

print(f"Quantidade de latas de tinta a serem compradas: {quantidade_latas_tinta}")
print(f"Preço total comprando apenas latas de 18 litros: R$ {preco_total_latas:.2f}")

print(f"Quantidade de galões de tinta a serem comprados: {quantidade_galoes_tinta}")
print(f"Preço total comprando apenas galões de 3,6 litros: R$ {preco_total_galoes:.2f}")

print(f"Quantidade de latas de tinta na mistura: {quantidade_latas_mistura}")
print(f"Quantidade de galões de tinta na mistura: {quantidade_galoes_mistura}")
print(f"Preço total misturando latas e galões: R$ {preco_total_mistura:.2f}")
