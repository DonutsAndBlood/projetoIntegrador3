import pandas as pd

df = pd.read_csv('2022\INMET_CO_DF_A001_BRASILIA_01-01-2022_A_31-12-2022.CSV', delimiter=';', encoding='Windows 1252', nrows=7)

x = pd.DataFrame(df)

x.set_index('REGIAO:', inplace=True)
x = x.transpose().reset_index(drop = True)

colunas_x = x.columns

remover = ['CODIGO (WMO):','DATA DE FUNDACAO:','ESTACAO:']

conjunto1 = set(colunas_x)
conjunto2 = set(remover)

conjunto_resultado = conjunto1 & conjunto2

coluninhas = list(conjunto_resultado)

x = x.drop(columns=coluninhas)

df2 = pd.read_csv('2022\INMET_CO_DF_A001_BRASILIA_01-01-2022_A_31-12-2022.CSV', delimiter=';', encoding='Windows 1252', skiprows=8)

y = pd.DataFrame(df2)


colunas_y = y.columns

remover = ['Data','Hora UTC','PRECIPITAÇÃO TOTAL, HORÁRIO (mm)','VENTO, VELOCIDADE HORARIA (m/s)','TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','RADIACAO GLOBAL (Kj/m²)','UMIDADE RELATIVA DO AR, HORARIA (%)']

conjunto1 = set(colunas_y)
conjunto2 = set(remover)

conjunto_resultado = conjunto1 - conjunto2

coluninhas = list(conjunto_resultado)

y = y.drop(columns=coluninhas)

print(y.columns)