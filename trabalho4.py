numBoiMaisGordo=0
pesoBoiMaisGordo=0
numBoiMaisMagro=0
pesoBoiMaisMagro=(float("inf"))

for i in range(1, 51):
    peso=float(input(f"Digite o peso do {i}º boi"))

    if peso>pesoBoiMaisGordo:
        numBoiMaisGordo=i
        pesoBoiMaisGordo=peso

    if peso>pesoBoiMaisMagro:
        numBoiMaisMagro=i
        pesoBoiMaisMagro=peso

    print(f"\n O boi mais gordo é o numero:{numBoiMaisGordo}, com {pesoBoiMaisGordo}Kg")
    print(f" O boi mais magro é o numero:{numBoiMaisMagro}, com {pesoBoiMaisMagro}Kg")