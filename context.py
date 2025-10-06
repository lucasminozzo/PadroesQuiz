# context.py
import strategies as s
import random
import pergunta_Factory as pf
from observers import PontuacaoObserver

class Quiz:
    def __init__(self, dados_json):
        self.dados_json = dados_json
        self.strategy = None # Agora é a estratégia de PONTUAÇÃO
        self.perguntas = []
        self._observers = [] # Lista de observadores

    # Métodos para o padrão Observer
    def register(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def escolher_dificuldade(self):
        print("=== Bem-vindo ao Quiz de One Piece ===\n")
        print("Escolha a dificuldade:")
        print("1. Fácil (1 ponto por acerto)")
        print("2. Médio (1.5 pontos por acerto)")
        print("3. Difícil (2 pontos por acerto)")
        print("4. Misto (3 pontos por acerto)")

        escolha = int(input("\nDigite o número da dificuldade: "))

        dificuldades = self.dados_json["quiz"]["dificuldade"]
        
        if escolha == 1:
            self.strategy = s.FacilPontuacaoStrategy()
            self.perguntas = dificuldades["facil"]
        elif escolha == 2:
            self.strategy = s.MedioPontuacaoStrategy()
            self.perguntas = dificuldades["medio"]
        elif escolha == 3:
            self.strategy = s.DificilPontuacaoStrategy()
            self.perguntas = dificuldades["dificil"]
        elif escolha == 4:
            self.strategy = s.MistoPontuacaoStrategy()
            self.perguntas = (dificuldades["facil"] + 
                              dificuldades["medio"] + 
                              dificuldades["dificil"])
        else:
            print("Opção inválida, saindo...")
            exit()

    def jogar(self):
        if not self.strategy:
            self.escolher_dificuldade()

        # Cria e registra o observador de pontuação com a estratégia escolhida
        pontuacao_observer = PontuacaoObserver(self.strategy)
        self.register(pontuacao_observer)

        random.shuffle(self.perguntas)
        perguntas_obj = [pf.criar(p) for p in self.perguntas]
        acertos = 0

        for idx, pergunta in enumerate(perguntas_obj, 1):
            alternativas = pergunta.exibir(idx)

            while True:
                resposta = input("Sua resposta: ").strip()
                if not resposta.isdigit() or not 1 <= int(resposta) <= len(alternativas):
                    print("⚠️ Digite um número válido entre 1 e 4.")
                    continue
                break
            
            resposta = int(resposta)
            if alternativas[resposta - 1]["correct"]:
                acertos += 1
                self.notify() # Notifica os observadores (PontuacaoObserver) sobre o acerto
            else:
                print("❌ Errado!")
                correta = next(alt['alt'] for alt in alternativas if alt['correct'])
                print(f"A resposta correta era: {correta}")

        pontos_finais = pontuacao_observer.get_pontos()
        print("\n=== Fim do quiz! ===")
        print(f"Você acertou {acertos} de {len(perguntas_obj)} perguntas.")
        print(f"Sua pontuação final foi: {pontos_finais} pontos.")