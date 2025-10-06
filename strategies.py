from abc import ABC, abstractmethod
import random
class DificuldadeStrategy(ABC):
    @abstractmethod
    def selecionar_perguntas(self, dados):
        pass
    
class FacilStrategy(DificuldadeStrategy):
    def selecionar_perguntas(self, dados):
        return dados["quiz"]["dificuldade"]["facil"]


class MedioStrategy(DificuldadeStrategy):
    def selecionar_perguntas(self, dados):
        return dados["quiz"]["dificuldade"]["medio"]


class DificilStrategy(DificuldadeStrategy):
    def selecionar_perguntas(self, dados):
        return dados["quiz"]["dificuldade"]["dificil"]
    
class MistoStrategy(DificuldadeStrategy):
    def selecionar_perguntas(self, dados):
        todas = (
            dados["quiz"]["dificuldade"]["facil"]
            + dados["quiz"]["dificuldade"]["medio"]
            + dados["quiz"]["dificuldade"]["dificil"]
        )
        random.shuffle(todas)
        return todas