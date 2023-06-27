"""
Data Scientist Jr.: Karina Gonçalvess Soares

entity_recognition.py
=====================
Objetivo: Este script é um módulo que serve para o Reconhecimento 
          de Entidades Nomeadas (NER) através do uso de um modelo
          pré-treinado do spaCy. Isto é construido numa classe do 
          Python.
Versão: 1.0.0
Data: 23/06/2023
Autor: Dr.Eddy Giusepe
"""
import spacy

class EntityRecognizer:
    """Está classe realiza a extração de Entidades Nomeadas."""
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_lg") # pt_core_news_sm
        
    def recognize_entities(self, text):
        doc = self.nlp(text)
        entities = []
        
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_
            })
        
        return entities