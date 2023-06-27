"""
Data Scientist.: PhD.Eddy Giusepe Chirinos Isidro
main.py
=======
Objetivo: Este script ativa o FastAPI e faze um Reconhecimento 
          de Entidades Nomeadas (NER) através do uso de um modelo
          pré-treinado do spaCy.
Versão: 1.0.0
Data: 23/06/2023
Autor: Dr.Eddy Giusepe
Método de execução:
                   $ uvicorn main:app --reload
"""
from fastapi import FastAPI
from modules.entity_recognition import EntityRecognizer

app = FastAPI(title='🤗 Usando FastAPI para o NER com spaCy 🤗',
              version='1.0',
              description="""Data Scientist.: PhD. Eddy Giusepe Chirinos Isidro\n
              Projeto end-to-end para a Extração de Entidades Nomeadas""")
entity_recognizer = EntityRecognizer()

"""
Usar o método HTTP GET para a rota /analyze não é considerado uma boa prática quando 
se trata de operações que modificam ou atualizam dados no servidor. O método GET é 
geralmente usado para recuperar informações do servidor, sem fazer alterações ou efeitos colaterais.
"""
# @app.get("/analyze")
# def analyze_query(query: str):
#     entities = entity_recognizer.recognize_entities(query)
#     return {"entities": entities}

@app.post("/analyze") # O método POST é comumente usado para enviar dados para o servidor, o que se encaixa com nossa intenção de enviar uma query para ser processada.
def analyze_query(query: str):
    entities = entity_recognizer.recognize_entities(query)
    return {"entities": entities}
