# Autor: Marcelo Rodrigues
# Projeto: Analise de dados de Excel

#importando bibliotecas (pandas para manipulação de dados)
import pandas as pd

# Carregando o arquivo Excel
pd.read_excel('ocupacao.xlsx')
planilha = pd.read_excel('ocupacao.xlsx')

# Agrupar os registros por nome

resultado = planilha.groupby(["Registro","Nome"])["Horas"].sum()

# Loop para exivir os resultados
for (registro,nome), horas in resultado.items():
    print(f"Registro: {registro}, Nome: {nome}, Total de Horas: {horas}")
    


