# Nome: Samara Victoria Ferraz dos Santos
# RA: 558719

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
