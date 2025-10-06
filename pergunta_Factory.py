from models import Pergunta 

def criar(pergunta_dict: dict) -> Pergunta:
        return Pergunta(
            enunciado=pergunta_dict["pergunta"],
            alternativas=pergunta_dict["alternativas"]
        )