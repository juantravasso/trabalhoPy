for i in range(30):
    nome=(input(f"nome do {i+1}º aluno:"))
    n1 = float(input("Primeira nota:"))
    n2 = float(input("segunda nota:"))
    media = (n1+n2)/2
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    print(f"{nome} ficou com media igual a {media}, logo esta {situacao}")
    