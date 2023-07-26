hora= int(input("Quanto você ganha por hora: "))
horastrabalhadas=int(input("Quantas horas você trabalhou esse mês: "))

bruto = hora* horastrabalhadas

imposto_renda = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05

liquido = bruto-imposto_renda-inss-sindicato

print("Salário bruto: R$" ,bruto,)
print("IR: R$",imposto_renda)
print("INSS: R$" ,inss)
print("Sindicato: R$",sindicato)
print("Liquido: R$",liquido)