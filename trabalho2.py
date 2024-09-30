numAlunos = int(input("digite a quantidade de alunos:"))

for i in range(numAlunos):
    nome=input(f"Nome do {1+1}º aluno:")

    n1= float(input("Primeira nota do aluno:"))

    n2= float(input("Segunda nota do aluno:"))

    media = (n1+n2)/2

situacao = "Aprovado" if media >= 6 else "Reprovado"

print(f"{nome} ficou com média {media}\n logo {situacao}")