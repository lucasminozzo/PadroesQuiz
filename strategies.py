# strategies.py
from abc import ABC, abstractmethod

class PontuacaoStrategy(ABC):
    @abstractmethod
    def calcular_pontos(self, pontos_atuais):
        pass

class FacilPontuacaoStrategy(PontuacaoStrategy):
    def calcular_pontos(self, pontos_atuais):
        return pontos_atuais + 1

class MedioPontuacaoStrategy(PontuacaoStrategy):
    def calcular_pontos(self, pontos_atuais):
        return pontos_atuais + 1.5

class DificilPontuacaoStrategy(PontuacaoStrategy):
    def calcular_pontos(self, pontos_atuais):
        return pontos_atuais + 2

class MistoPontuacaoStrategy(PontuacaoStrategy):
    def calcular_pontos(self, pontos_atuais):
        return pontos_atuais + 3