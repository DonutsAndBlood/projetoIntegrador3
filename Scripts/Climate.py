import pandas as pd 

df = pd.read_csv('empreendimentos.csv', delimiter=';', encoding='Windows 1252')

x = pd.DataFrame(df)

#print(x.columns)

colunas = x.columns

y = ['DatGeracaoConjuntoDados','NomEmpreendimento','SigUFPrincipal','SigTipoGeracao','NomFonteCombustivel','MdaPotenciaFiscalizadaKw','MdaPotenciaOutorgadaKw']

conjunto1 = set(colunas)
conjunto2 = set(y)

conjunto_resultado = conjunto1 - conjunto2

coluninhas = lista_resultado = list(conjunto_resultado)

x = x.drop(columns=coluninhas)






