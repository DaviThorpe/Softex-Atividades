#Instruções do projeto
#Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

#aluno: Nome do aluno;
#nota_1: Primeira nota;
#nota_2: Segunda nota;
#faltas: Número de faltas;

#O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

#O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

#Por fim, o programa deverá mostrar na tela:
#- o maior número de faltas;
#- a média geral das notas dos alunos;
#- e a maior média.

#Veja em anexo um exemplo do arquivo “notas_alunos.csv”.

# Inicio do código

import pandas as pd
df = pd.read_csv('notas_alunos.csv')
media = (df['nota_1'] + df['nota_2']) / 2
df['media'] = media
situacao = str('')

df.loc[df['faltas'] > 5, 'situacao'] = 'REPROVADO'
df.loc[df['media'] < 7, 'situacao'] = 'REPROVADO'
df.loc[df['situacao'] != 'REPROVADO', 'situacao'] = 'APROVADO'

max_faltas = df['faltas'].max()
ger_media = df['media'].median()
max_media = df['media'].max()

print('O maior número de faltas foi: {}'.format(max_faltas))
print('A média geral foi: {}'.format(ger_media))
print('A maior média foi: {}'.format(max_media))

df.to_csv(r'D:\Meus projetos\Softex-Atividades\Atividades\alunos_situacao.csv', index=False)