[Uploading README.md…]()
# Sistema de Gerenciamento de Alunos

Sistema de linha de comando (CLI) em Python para cadastro e gerenciamento de alunos, com cálculo de estatísticas, busca, ordenação por desempenho e exportação de relatórios.

Projeto desenvolvido como parte dos meus estudos em Python, aplicando conceitos de estruturas de dados, funções, manipulação de arquivos e lógica de programação.

## Funcionalidades

- **Cadastro de alunos**: registra nome e nota de cada aluno
- **Listagem**: exibe todos os alunos cadastrados com status (Aprovado/Reprovado)
- **Estatísticas da turma**: calcula média geral e maior nota
- **Busca por nome**: localiza um aluno específico na lista
- **Ordenação por nota**: gera um ranking dos alunos da maior para a menor nota
- **Exportação de relatório**: salva um relatório completo em arquivo `.txt`

## Tecnologias utilizadas

- Python 3
- Estruturas de dados nativas (listas e dicionários)
- Manipulação de arquivos com `open()`
- Funções lambda para ordenação

## Como executar

1. Certifique-se de ter o Python 3 instalado
2. Clone este repositório:
   ```bash
   git clone https://github.com/Eduardo-G-Costa/sistema-gerenciamento-alunos.git
   ```
3. Execute o script:
   ```bash
   python sistema-gerenciamento-alunos.py
   ```
4. Use o menu interativo para cadastrar, listar, buscar e gerar relatórios de alunos

## Exemplo de uso

```
1 - Cadastrar aluno
2 - Listar alunos
3 - Estatísticas
4 - Buscar aluno por nome
5 - Ordenar lista por nota
6 - Salvar em arquivo .txt com open()
0 - Sair
Opcão(0-6):
```

## Critério de aprovação

Alunos com nota igual ou superior a **7.0** são considerados Aprovados; abaixo disso, Reprovados.

## Autor

Desenvolvido por Eduardo G. Costa, estudante de Engenharia de Software, durante estudos práticos de Python.
