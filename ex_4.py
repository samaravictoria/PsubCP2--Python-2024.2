# Nome: Samara Victoria Ferraz dos Santos
# RA: 558719

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

