import pandas as pd
from datetime import datetime
from pandas.io import json

df = pd.read_csv("C:\\Users\\patricia.miranda\\Documents\\GitHub\\curso.python\\EXERCICIO2\\planilha.csv")

vetor = []

# Filtrando regioes por nome
lista = df["Region"].unique()

for i in lista:
    # agrupando os crimes por regiao, mantendo so as regioes com mais de 2 tipos de infracao.
    # contabilizando crimes com mais de 10 ocorrencias na regiao e adicionando a uma nova lista
    df_i = df[(df['Rolling year total number of offences'] > 10) & (df['Region'] == i)].groupby(['Offence'],as_index = False).sum()
    vetor.append({})
    vetor[-1]["Data de processo"] = datetime.now().strftime('%d-%m-%Y %H:%M')
    vetor[-1]["Regiao"] = i
    if len(df_i['Offence'].unique()) > 2:
        vetor[-1]['Crimes'] = df_i.to_dict('records')
        
# printando com forma .json
print(json.dumps(vetor, indent=2))

random_file = open('C:\\Users\\patricia.miranda\\Documents\\GitHub\\curso.python\\EXERCICIO2\\tabela.json', 'w')

random_file.write(json.dumps(vetor, indent=2))