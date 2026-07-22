alunos = []
nomes = []
def cadastrar_alunos():
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    alunos.append({"nome": nome, "nota": nota})
    print(f"Aluno cadastrado!\n")
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return
    print("\n   Lista de Alunos   \n")
    for a in alunos:
        status = "Aprovado" if a["nota"] >= 7.0 else "Reprovado"
        print(f" {a['nome']:20} {a['nota']:5.1f} {status}")
    print()
def mostrar_estatisticas():
    if not alunos:
        print("Sem dados suficientes.\n")
        return
    notas = [a["nota"] for a in alunos]
    print(f"\nTurma: {len(alunos)} alunos")
    print(f"Média: {sum(notas)/len(notas): .2f}")
    print(f"Maior nota: {max(notas)}\n")
def busca_nome():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return
    busca = input("Digite o nome que deseja buscar: ")
    for a in alunos:
        if a["nome"] == busca:
            print(f"{busca} encontrado! Nota: {a['nota']}\n")
            return
    print(f"{busca} não foi encontrado.\n")
def lista_por_nota():
    if not alunos:
        print("Nenhum aluno cadastrado\n")
        return
    lista_ordenada = sorted(alunos, key=lambda a: a["nota"], reverse=True)
    print("\nClassificacão dos Alunos (MAIOR NOTA)")
    for posicao, aluno in enumerate(lista_ordenada, start=1):
        print(f"{posicao}º Lugar - {aluno['nome']}: Nota {aluno['nota']}\n")
def salvar_relatorio():
    if not alunos:
        print("Nenhum aluno para salvar.\n")
        return
    with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Relatório de Turma\n\n")
        for a in alunos:
            status = "Aprovado" if a["nota"] >= 7.0 else "Reprovado"
            arquivo.write(f"{a['nome']:<20}{a['nota']:<6.2f}{status}\n")
        notas = [a["nota"] for a in alunos]
        arquivo.write(f"\nMédia da turma: {sum(notas)/len(notas): .2f}")
        arquivo.write(f"Total de alunos: {len(alunos)}\n")
    print("Relatório .txt salvo!\n")
while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Estatísticas")
    print("4 - Buscar aluno por nome")
    print("5 - Ordenar lista por nota")
    print("6 - Salvar em arquivo .txt com open()")
    print("0 - Sair")
    opcao = input("\nOpcão(0-6): ")
    if opcao == "1":
        cadastrar_alunos()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        mostrar_estatisticas()
    elif opcao == "4":
        busca_nome()
    elif opcao == "5":
        lista_por_nota()
    elif opcao == "6":
        salvar_relatorio()
    elif opcao == "0":
        break
    else:
        print("Opcão inválida.\n")
