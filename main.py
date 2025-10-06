import json
import context as ctx
if __name__ == "__main__":
    # Carregar JSON
    with open("quiz_onepiece.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    quiz = ctx.Quiz(dados)
    quiz.jogar()