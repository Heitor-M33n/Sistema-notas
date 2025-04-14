import lib

print('Bem vindo ao sistema de notas da turma.')

while True:
    print('\nComandos:\n1. Cadastrar aluno\n2. Ver boletim do aluno\n3. Ver estatísticas da turma\n4. Ver alunos da turma\n5. Lista de alunos aprovados\n6. Lista de alunos reprovados\n7.\n8.\n9. Deletar turma\n0. Sair')
    turma = lib.ler_csv()

    comando = input('').strip(); print()

    match comando:
        case '1': 
            lib.cadastrar_aluno(turma)
        case '2':
            lib.exibir_boletim(lib.escolher_aluno(turma))
        case '3':
            lib.estatisticas(turma)
        case '4':
            lib.print_turma(lib.listar_turma(turma, lib.filtro_listar()))
        case '5':
            lib.print_turma(lib.aprovados_e_reprovados(lib.listar_turma(turma), 'Aprovado'))
        case '6':
            lib.print_turma(lib.aprovados_e_reprovados(lib.listar_turma(turma), 'Reprovado'))
        case '7': #para fazer
            pass
        case '8': #para fazer
            pass
        case '9':
            lib.deletar_turma()
        case '0':
            break
        case _:
            print('Comando inexistente.')