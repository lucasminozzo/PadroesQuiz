from models import Pergunta 

def criar(pergunta_dict):
        return Pergunta(
            enunciado=pergunta_dict["pergunta"],
            alternativas=pergunta_dict["alternativas"]
        )