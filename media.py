try:
    nomeAluno = (input('Digite o nome do aluno: ')).title()
    primeiraNota = int(input('Primeira Nota do aluno: '))
    segundaNota = int(input('Segunda Nota do aluno: '))
    terceiraNota = int(input('terceira Nota do aluno: '))
    quartaNota = int(input('quarta Nota do aluno: '))
    mediaTotal = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4

    if mediaTotal >= 5:
        alunoAprovacao = 'Aprovado'
    else:
        alunoAprovacao = 'Reprovado'
    # Mostra a nota do aluno
    print(f'\tNota média do aluno {nomeAluno}\t')
    print(f'\nMédia: {mediaTotal}\n1° Bimestre: {primeiraNota}\n2° Bimestre: {segundaNota}\n3° Bimestre: {terceiraNota}\n4° Bimestre: {quartaNota}')
    print(f'\nSITUAÇÃO: {alunoAprovacao}')
   
except:
    print('Ocorreu um erro...')