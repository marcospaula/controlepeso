import pandas as pd

# Lê o arquivo XLSX com os dados das pessoas
dff = pd.read_excel('functions/profiles.xlsx')

def get_persons():
   # Retorna lista com todas as pessoas ordenadas pelo nome
   names = dff['name'].sort_values().tolist()
   # Adiciona a opção de selecionar um exemplo no início da lista (base zero)
   names.insert(0, "(digite seu nome ou selecione um exemplo)")
   return names

# Retorna os dados de uma pessoa específica
def get_person(name):
    if name == "(digite seu nome ou selecione um exemplo)":
        return None
    user = dff[dff['name'] == name]
    if user.empty:
        return None
    return user.iloc[0] # Retorna a primeira linha do DataFrame (base zero)