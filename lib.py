from operator import itemgetter
from json import loads
import csv
import os

def deletar_turma() -> None:
    if (input('Digite "sim, quero deletar a turma" para concluir a ação').lower()).strip() == 'sim, quero deletar a turma':
        os.remove('dados.csv')
    else:
        print('Ação cancelada.')

def escrever_csv(turma: list[dict]) -> None:
    with open('dados.csv', newline='', mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, ['Nome', 'Matrícula', 'Notas', 'Média', 'Situação'])
        writer.writeheader()
        for aluno in turma:
            writer.writerow(aluno)

def ler_csv() -> list[dict]:
    turma = []

    if 'dados.csv' not in os.listdir():
        return turma

    with open('dados.csv', newline='', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Notas'] = loads(row['Notas'])
            turma.append(row)

    return turma

def print_turma(turma: list[dict]) -> None: #organizar isso
    if not turma:
        print('Turma vazia...')
        return
    
    print(turma[0].keys())
    for aluno in turma:
        print(aluno.items())

def media_e_situacao(aluno: dict) -> list[int, str]:
    total = 0
    divisor = 0

    for i in aluno['Notas']:
        divisor += 1
        total += i

    media = total/divisor
    if media >= 60:
        return [media, 'Aprovado']
    else:
        return [media, 'Reprovado']

def cadastrar_aluno(turma: list[dict]) -> None:
    aluno = {}
    notas = []
    c = 1

    aluno['Nome'] = (input('Nome do aluno: ').strip()).title()
    aluno['Matrícula'] = (input('Matrícula do aluno: ').strip()).title()

    while c < 5:
        inp = (input(f'Insira a {c}ª nota ("x" para parar): ').strip()).lower()

        if inp == 'x':
            if c == 1:
                notas.append(0)
            break
       
        try:
            if int(inp) > 100 or int(inp) < 0:
                raise ValueError
            notas.append(int(inp))
        except ValueError:
            print('\nInsira uma nota válida, de 0 a 100\n')
            continue

        c += 1

    aluno['Notas'] = notas
    aluno['Média'], aluno['Situação'] = media_e_situacao(aluno)
    print('Média e situação do aluno calculados.')
    turma.append(aluno)
    escrever_csv(turma)

def exibir_boletim(aluno: dict) -> None:
    if not aluno:
        return

    for key in aluno.keys():
        if key == 'Nome':
            print(f'\nBoletim escolar de {aluno[key]}.\n')
            continue
        elif key == 'Notas':
            print('Notas: ', end='')
            first = True

            for i in aluno[key]:
                if first:
                    first = False
                    print(f'{i}', end='')
                    continue

                print(f', {i}', end='')

            print()

            continue

        print(f'{key}: {aluno[key]}')

def escolher_aluno(turma: list[dict], dado: str = '') -> dict:
    if not dado:
        dado = (input('Digite o nome ou matrícula do aluno que deseja ver o boletim: ').strip()).title()
    
    for aluno in turma:
        try:
            if dado == aluno['Nome'][:len(dado)] or dado == str(aluno['Matrícula'][:len(dado)]):
                return aluno
            else:
                continue
        except IndexError:
            continue

    print('Aluno não encontrado')
    return {}

def estatisticas(turma: list[dict]) -> None:
    medias, aprovados, reprovados = (0, 0, 0)

    if not turma:
        print('Turma vazia...')
        return

    for aluno in turma:
        medias += float(aluno['Média'])

        if aluno['Situação'] == 'Aprovado':
            aprovados += 1
        else:
            reprovados += 1

    print(f'Estatísticas da turma:\nQuantidade de alunos: {len(turma)}\nMédia da turma: {round(medias/len(turma), 2)}\nQuantidade de aprovados: {aprovados} ({round((aprovados/len(turma)) * 100, 2)}%)\nQuantidade de reprovados: {reprovados} ({round((reprovados/len(turma)) * 100, 2)}%)')

def filtro_listar() -> str:
    print('Modos de filtro:\n1. Ordem alfabética\n2. Matrícula\n3. Média')
    filtro = input('').strip()

    match filtro:
        case '1':
            return 'Nome'
        case '2':
            return 'Matrícula'
        case '3':
            return 'Média'
        case _:
            print('Filtro inexistente, ação cancelada.')
            return ''

def listar_turma(turma: list[dict], filtro: str = 'Nome') -> list[dict]:
    new_turma = []

    if filtro == 'Nome':
        r = False
    elif filtro == 'Matrícula' or filtro == 'Média':
        r = True
    else:
        return []
        
    print(f'Lista de alunos ordenada por {filtro}')
    return sorted(turma, key=itemgetter(filtro), reverse=r)

def aprovados_e_reprovados(turma: list[dict], looking_for: str) -> list[dict]:
    turma_new = []

    for aluno in turma:
        if aluno['Situação'] == looking_for:
            turma_new.append(aluno)

    return turma_new