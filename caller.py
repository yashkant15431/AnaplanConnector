# Importando outras bibliotecas do Python
import base64
import json
import requests
import os
import child
from child import anaplanImport as anaplan

#Credenciais para acessar o Anaplan
model = "Planning"
user = "paolovm3@yahoo.com.br"
pwd = "Number28"


#DEFINIR RELACAO IMPORT/ARQUIVOS EM PARES PARA EXECUTAR A MAIN EM LOOP
importList = {"Asset Price from quotes.csv": "quotes.csv"}

# Lista de Processes a serem executados com nome assim como na tab de actions do Anaplan
processName = ["Testing Process"]

# funcao para Import de arquivo
def singleFileImport(conn, importName, fileLocation):
    with open(fileLocation, "rt") as f:
        data_content = f.read()
    f.close()
    # execucao do subprocesso de import
    anaplanImport = anaplan().executeImport(conn, importName, data_content)
    print("999 - Import Complete")

# funcao para execucao de processo
def singleProcessExecution(conn, processName):
    # execucao do subprocesso de import
    anaplanImport = anaplan().executeProcess(conn, processName)
    print("999 - Process Complete")


def main():
    try:
        # conectar ao Anaplan
        conn= anaplan().connectToAnaplanModel(user, pwd, model)
        for importAction, importFile in importList.items():
            singleFileImport(conn, importAction, importFile)
        for each_process in processName:
            singleProcessExecution(conn, each_process)
    except:
        print("998 - An exception occurred.")



if __name__ == '__main__':
    main()

