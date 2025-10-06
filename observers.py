# observers.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class PontuacaoObserver(Observer):
    def __init__(self, strategy):
        self.pontos = 0
        self.strategy = strategy # Recebe a estratégia de pontuação

    def update(self):
        # Quando notificado (acerto), calcula os pontos usando a estratégia
        self.pontos = self.strategy.calcular_pontos(self.pontos)
        print(f"✅ Correto! Você ganhou pontos. Pontuação atual: {self.pontos}")

    def get_pontos(self):
        return self.pontos