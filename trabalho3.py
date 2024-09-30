numAlunos = int(input("Digite a quantidade de alunos:"))
soma=0
maiorMedia=0
menorMedia=float('inf')
nomeMaiorMedia=""
nomeMenorMedia=""

for i in range(numAlunos):
    nome=input(f"Nome do {i+1}º aluno:")
    n1 = float(input("Primeira nota do aluno:"))
    n2 = float(input("Segunda nota do aluno:"))
    media = (n1+n2)/2
    soma+=media
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    print (f"{nome} ficou com media {media} logo {situacao}")

    if media > maiorMedia:
        maiorMedia=media
        nomeMaiorMedia=nome
    
    if media < menorMedia:
        menorMedia=media
        nomeMenorMedia=nome

    mediaTurma=soma/numAlunos
    print(f"\n A media da turma é: {mediaTurma:.2f}")
    print(f"Aluno com maior media é:{nomeMaiorMedia}")
    print(f"Aluno com menor media é:{nomeMenorMedia}")