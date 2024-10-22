# Nome: Samara Victoria Ferraz dos Santos
# RA: 558719

-----------------------------------------------------------------------------------------------------------------------------------------------


# Exercício 1 - 4 Pontos

Tabelas de memória são importantes, e seu uso é fundamental para trabalhar com os dados inseridos nas operações executadas dentro da solução em desenvolvimento, e neste contexto:


DADOS:

RA	        Nome	    Curso   Turma	Semestre	CP1	    CP2	    CP3	    CP4	    CP5	    CP6
551234	    Fulano	    TDS	    1TDSPO	1	        5	    6,5	    7,5	    6	    6,5	    9
551235	    Beltrana	TDS	    1TDSPZ	1	        8	    7,5	    0	    5,5	    6,8	    7,8
551236	    Joaninha	CD	    1CDPA	2	        5	    6	    8,8	    0	    7,5	    9
551237	    Joaozinho	CD	    1CDPI	2	        8	    7	    0	    8	    8	    0
551238	    Joca	    GD	    1GDPD	1	        7,8	    5,5	    6,5	    5,2	    7,8	    8
551239	    Juju	    GD	    1GDPC	1	        9	    10	    0	    0	    8	    9


## 1-A Agora vamos inverter as informações acima para o formato dicionário com chave e lista de valores (1 Ponto):

# Dados Alunos:
alunos_data = [
    [551234, 'Fulano', 'TDS', '1TDSPO', 1, 5, 6.5, 7.5, 6, 6.5, 9],
    [551235, 'Beltrana', 'TDS', '1TDSPZ', 1, 8, 7.5, 0, 5.5, 6.8, 7.8],
    [551236, 'Joaninha', 'CD', '1CDPA', 2, 5, 6, 8.8, 0, 7.5, 9],
    [551237, 'Joaozinho', 'CD', '1CDPI', 2, 8, 7, 0, 8, 8, 0],
    [551238, 'Joca', 'GD', '1GDPD', 1, 7.8, 5.5, 6.5, 5.2, 7.8, 8],
    [551239, 'Juju', 'GD', '1GDPC', 1, 9, 10, 0, 0, 8, 9]
]

# Chaves do dicionário:
headers = ['RA', 'Nome', 'Curso', 'Turma', 'Semestre', 'CP1', 'CP2', 'CP3', 'CP4', 'CP5', 'CP6']

# Criar o dicionário invertido com chaves e listas de valores:
dicionario_tabela_2 = {header: [] for header in headers}

# Preencher o dicionário com os valores dos alunos:
for aluno in alunos_data:
    for i, header in enumerate(headers):
        dicionario_tabela_2[header].append(aluno[i])

# Exibindo o dicionário resultante:
print(dicionario_tabela_2)

# /////////////////////////////////////////////////////////////////////

## 1-B Use os dados fornecidos acima para construir uma lista de dicionários (1 Ponto): 

def inserir_lista(lista, dicionario):
   
    # Seu código começa aqui:
    # Pegar a quantidade de alunos:
    num_alunos = len(next(iter(dicionario.values()))) 
    
    for i in range(num_alunos):

        # Cria um novo dicionário para cada aluno
        novo_aluno = {}

        # Para cada chave no dicionário
        for chave in dicionario:

            # Adiciona o valor correspondente na posição i do dicionário para esse aluno
            novo_aluno[chave] = dicionario[chave][i]
            
        # Adiciona o dicionário criado à lista
        lista.append(novo_aluno)
    
    # Seu código termina aqui!
    return lista

# Testando: 
# Lista inicialmente vazia
lista_tabela_1 = []

# Chamada da função
lista_tabela_1 = inserir_lista(lista_tabela_1, dicionario_tabela_2)

# Exibindo o resultado
print(lista_tabela_1)

# /////////////////////////////////////////////////////////////////////

### 1-C Desenvolva duas funções que façam a 'inserção' de um novo Aluno em ambas as tabelas (uma para a primeira e uma para a segunda) (1 ponto):

# Função para inserir o novo aluno na lista de dicionários:
def inserir_lista(lista, novo_aluno):
    lista.append(novo_aluno)
    return lista

# Função para inserir o novo aluno no dicionário de listas:
def inserir_dicionario(dicionario, lista):
    chaves = list(dicionario.keys())
    
    # Seu código começa aqui:
    for i, chave in enumerate(chaves):
        dicionario[chave].append(lista[i])

    # Seu código termina aqui!
    return dicionario

# Testando:
# Definindo uma lista de dicionários (lista_tabela_1):
lista_tabela_1 = [
    {'RA': 551234, 'Nome': 'Fulano', 'Curso': 'TDS', 'Turma': '1TDSPO', 'Semestre': 1, 'CP1': 5, 'CP2': 6.5, 'CP3': 7.5, 'CP4': 6, 'CP5': 6.5, 'CP6': 9}
]

# Definindo um dicionário de listas (dicionário_tabela_2):
dicionario_tabela_2 = {
    'RA': [551234],
    'Nome': ['Fulano'],
    'Curso': ['TDS'],
    'Turma': ['1TDSPO'],
    'Semestre': [1],
    'CP1': [5],
    'CP2': [6.5],
    'CP3': [7.5],
    'CP4': [6],
    'CP5': [6.5],
    'CP6': [9]
}

# Dados do novo aluno:
novo_aluno = {'RA': 551244, 'Nome': 'Aluno_Novo', 'Curso': 'TDS', 'Turma': '1TDSPO', 'Semestre': 1, 'CP1': 5.5, 'CP2': 5.5, 'CP3': 6.0, 'CP4': 6.0, 'CP5': 7.0, 'CP6': 8.0}

# Lista com os valores do novo aluno para inserção no dicionário:
lista_novo_aluno = [551244, 'Aluno_Novo', 'TDS', '1TDSPO', 1, 5.5, 5.5, 6.0, 6.0, 7.0, 8.0]

# Inserindo o novo aluno na lista de dicionários:
lista_tabela_1 = inserir_lista(lista_tabela_1, novo_aluno)

# Inserindo o novo aluno no dicionário de listas:
dicionario_tabela_2 = inserir_dicionario(dicionario_tabela_2, lista_novo_aluno)

# Exibindo os resultados:
print("Lista de dicionários atualizada:")
print(lista_tabela_1)

print("\nDicionário de listas atualizado:")
print(dicionario_tabela_2)

# /////////////////////////////////////////////////////////////////////


## 1-D Desenvolva duas funções, uma para cada modelo que façam a 'extração' de um aluno em ambas as tabelas, utilizando o 'RA' para encontrar e extrair o Aluno (1 ponto):

def extrair_lista(lista, RA):
    
    # Seu código começa aqui:
    for aluno in lista:
        if aluno['RA'] == RA:
            return aluno  
    return None  

    # Seu código termina aqui!

def extrair_dicionario(dicionario, RA):

    # Seu código começa aqui:
    if RA in dicionario['RA']:
        index = dicionario['RA'].index(RA)  
        # Cria um dicionário para retornar os dados do aluno:
        aluno_extraido = {chave: dicionario[chave][index] for chave in dicionario}
        return aluno_extraido  
    return None  

    # Seu código termina aqui!

# Testando:
# RA a ser extraído:
ra_a_extrair = 551234

# Extraindo da lista de dicionários:
aluno_da_lista = extrair_lista(lista_tabela_1, ra_a_extrair)
print("Aluno extraído da lista de dicionários:")
print(aluno_da_lista)

# Extraindo do dicionário de listas:
aluno_do_dicionario = extrair_dicionario(dicionario_tabela_2, ra_a_extrair)
print("\nAluno extraído do dicionário de listas:")
print(aluno_do_dicionario)

# ///////////////////////////////////////////////////////////////////// 

# Exercício 2 : Usando  a função 'open()' e a variável de contexto 'with' salve o 'dicionário_tabela_2' em um arquivo '.csv'! - 2 Pontos

import csv

# Dicionário_tabela_2 :
dicionario_tabela_2 = {
    'RA': [551234, 551235, 551236, 551237, 551238, 551239],
    'Nome': ['Fulano', 'Beltrana', 'Joaninha', 'Joaozinho', 'Joca', 'Juju'],
    'Curso': ['TDS', 'TDS', 'CD', 'CD', 'GD', 'GD'],
    'Turma': ['1TDSPO', '1TDSPZ', '1CDPA', '1CDPI', '1GDPD', '1GDPC'],
    'Semestre': [1, 1, 2, 2, 1, 1],
    'CP1': [5, 8, 5, 8, 7.8, 9],
    'CP2': [6.5, 7.5, 6, 7, 5.5, 10],
    'CP3': [7.5, 0, 8.8, 0, 6.5, 0],
    'CP4': [6, 5.5, 0, 8, 5.2, 0],
    'CP5': [6.5, 6.8, 7.5, 8, 7.8, 8],
    'CP6': [9, 7.8, 9, 0, 8, 9]
}

try:
    # Usando open com o modo 'x' para criar um novo arquivo:
    with open('dicionario_tabela_2.csv', 'x', newline='', encoding='utf-8') as arquivo:

        # Obter chaves e valores do dicionário:
        chaves = list(dicionario_tabela_2.keys())
        valores = list(dicionario_tabela_2.values())

        # Escrever as chaves no arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(chaves) 

        # Escrever os valores no arquivo:
        for i in range(len(valores[0])):
            linha = [valores[j][i] for j in range(len(valores))]  
            writer.writerow(linha) 

except FileExistsError:  # Captura se o arquivo já existe
    print('Arquivo já existe!')
except Exception as e:  # Captura qualquer outro erro
    print(f'Ocorreu um erro: {e}')
else:
    print('Arquivo salvo!')
finally:
    print('Programa finalizado!')


------------------------------------------------------------------------------------------------------------------------------------------------

# /////////////////////////////////////////////////////////////////////

# Exercício 3: Usando a função 'open()', salve os dados do 'dicionário_tabela_2' criado acima em um arquivo '.txt'! - 2 Pontos

# Dicionário_tabela_2 :
dicionario_tabela_2 = {
    'RA': [551234, 551235, 551236, 551237, 551238, 551239],
    'Nome': ['Fulano', 'Beltrana', 'Joaninha', 'Joaozinho', 'Joca', 'Juju'],
    'Curso': ['TDS', 'TDS', 'CD', 'CD', 'GD', 'GD'],
    'Turma': ['1TDSPO', '1TDSPZ', '1CDPA', '1CDPI', '1GDPD', '1GDPC'],
    'Semestre': [1, 1, 2, 2, 1, 1],
    'CP1': [5, 8, 5, 8, 7.8, 9],
    'CP2': [6.5, 7.5, 6, 7, 5.5, 10],
    'CP3': [7.5, 0, 8.8, 0, 6.5, 0],
    'CP4': [6, 5.5, 0, 8, 5.2, 0],
    'CP5': [6.5, 6.8, 7.5, 8, 7.8, 8],
    'CP6': [9, 7.8, 9, 0, 8, 9]
}

try:
    # Abrindo o arquivo em modo 'x' para criação, sem sobrescrever se já existir:
    arquivo = open('dicionario_tabela_2.txt', 'x', encoding='utf-8')

except FileExistsError:
    print('Arquivo já existe!')

else:
    # Iterando chaves do dicionário:
    for chave in dicionario_tabela_2:
        # Escreve a chave e os dados no arquivo, separando por ":" e uma nova linha:
        arquivo.write(f"{chave}: {repr(dicionario_tabela_2[chave])}\n")

    print('Arquivo Salvo!')

finally:
    if 'arquivo' in locals() and not arquivo.closed:  # Garante que o arquivo seja fechado, se aberto:
        arquivo.close()
    print('Programa finalizado!')


------------------------------------------------------------------------------------------------------------------------------------------------

# /////////////////////////////////////////////////////////////////////


# Exercício 4: Usando a bilbioteca 'json' faça primeiramente um 'dumps' do 'dicionário_tabela_2', em uma variável e depois com 'open' salve o arquivo no disco!! - 2 Pontos

import json

# Dicionário_tabela_2 :
dicionario_tabela_2 = {
    'RA': [551234, 551235, 551236, 551237, 551238, 551239],
    'Nome': ['Fulano', 'Beltrana', 'Joaninha', 'Joaozinho', 'Joca', 'Juju'],
    'Curso': ['TDS', 'TDS', 'CD', 'CD', 'GD', 'GD'],
    'Turma': ['1TDSPO', '1TDSPZ', '1CDPA', '1CDPI', '1GDPD', '1GDPC'],
    'Semestre': [1, 1, 2, 2, 1, 1],
    'CP1': [5, 8, 5, 8, 7.8, 9],
    'CP2': [6.5, 7.5, 6, 7, 5.5, 10],
    'CP3': [7.5, 0, 8.8, 0, 6.5, 0],
    'CP4': [6, 5.5, 0, 8, 5.2, 0],
    'CP5': [6.5, 6.8, 7.5, 8, 7.8, 8],
    'CP6': [9, 7.8, 9, 0, 8, 9]
}

# 'dumps' do dicionário:
dumped = json.dumps(dicionario_tabela_2, ensure_ascii=False, indent=4)

try:
    # Abrindo o arquivo para escrita com codificação 'utf-8' e modo 'x' (não sobrescrever):
    with open('dicionario_tabela_2.json', 'x', encoding='utf-8') as arquivo:
        # Escreve o JSON no arquivo:
        arquivo.write(dumped)

except FileExistsError:
    print('Arquivo já existe!')

else:
    print('Arquivo Salvo!')

finally:
    print('Programa finalizado!')
