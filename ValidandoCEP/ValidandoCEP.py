from pycep_correios import get_address_from_cep, WebService, exceptions
import pandas as pd

# Cria um DataFrame a partir de um arquivo csv
data = pd.read_excel("Enderecos.xlsx")

for i, nome in enumerate(data['CepEndereco']):
    try:
        cep = data.loc[i, 'CepEndereco']
        #Realiza a consulta do cep
        address = get_address_from_cep(str(cep), webservice=WebService.APICEP)

    except exceptions.InvalidCEP as eic:
        print(eic)
        print(cep)
        #Exclui a linha de número (i)
        data.drop(i, axis=0, inplace=True)

#Salvando o DataFrame em Excel
data.to_excel('./Enderecos_Cep_validado.xlsx',  encoding='utf-8', index=False)