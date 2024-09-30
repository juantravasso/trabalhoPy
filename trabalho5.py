numAlunos = int(input("Digite a quantidade de alunos:"))
soma = 0
for i in range(numAlunos):
    nome=input(f"nome do {i}º aluno:")
    n1 = float(input("Primeira nota do aluno:"))
    n2 = float(input("Segunda nota do aluno:"))
    media = (n1+n2)/2
    soma+=media
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    print(f"{nome} ficou com media{media}\n logo esta {situacao}")

    mediaTurma = soma/numAlunos
    print(f"\n A media da turma é: {mediaTurma:.2f}")