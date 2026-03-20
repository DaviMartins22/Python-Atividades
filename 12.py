alunos = []

# cadastro de 3 alunos
for i in range(3):
    print(f"\nCadastro do {i+1}º aluno")
    
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    notas = []
    for j in range(3):
        nota = float(input(f"Digite a {j+1}ª nota: "))
        notas.append(nota)
    
    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }
    
    alunos.append(aluno)

# exibindo resultados
print("\nMédias dos alunos:\n")

for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"{aluno['nome']} - Média: {media:.2f}")