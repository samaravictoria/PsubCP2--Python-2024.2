# Nome: Samara Victoria Ferraz dos Santos
# RA: 558719

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
