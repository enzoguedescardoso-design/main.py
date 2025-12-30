import random
import datetime

# ===============================
# FUNÇÕES DE JOGOS
# ===============================

def cara_ou_coroa():
    return random.choice(["cara", "coroa"])

def emoji():
    lista = [
        '😀','😂','😎','😍','🤩','😜','🤖','👻','🐱','🐶','🦊','🐼',
        '⚽','🎮','🎲','🎵','🚀','🔥','🎉','💎','🧠','🕹️'
    ]
    return random.choice(lista)

# ===============================
# FUNÇÃO DE AJUDA
# ===============================

def mostrar_ajuda():
    return (
        "\n📘 COMANDOS DISPONÍVEIS\n"
        "─────────────────────\n"
        "cara → jogar cara ou coroa\n"
        "emoji → sortear um emoji\n"
        "ajuda → ver esta lista\n"
        "sair → encerrar o bot\n\n"
        "💬 PERGUNTAS QUE POSSO RESPONDER\n"
        "- quem é você?\n"
        "- que horas são?\n"
        "- que dia é hoje?\n"
        "- você gosta de programação?\n"
        "- o que é python?\n"
        "- você gosta de jogos?\n"
        "- como aprender python?\n"
        "- estou triste / estou feliz\n"
        "- você é inteligente?\n"
    )

# ===============================
# FUNÇÃO PRINCIPAL DE RESPOSTAS
# ===============================

def responder(pergunta):
    p = pergunta.lower()

    # Cumprimentos
    if p in ["oi", "olá", "ola", "eae", "e aí", "bom dia", "boa tarde", "boa noite"]:
        return "Olá! 😄 Em que posso te ajudar?"

    # Identidade
    if "quem é você" in p or "o que você é" in p:
        return "Eu sou um chatbot feito em Python para conversar e ajudar você 🤖"

    # Hora e data
    if "hora" in p:
        return f"Agora são {datetime.datetime.now().strftime('%H:%M')}."
    if "dia" in p or "data" in p:
        return f"Hoje é {datetime.date.today().strftime('%d/%m/%Y')}."

    # Programação
    if "python" in p and "o que" in p:
        return "Python é uma linguagem de programação simples, poderosa e muito usada 🐍"
    if "aprender python" in p or "estudar python" in p:
        return "Comece com o básico: variáveis, if, loops e funções. Praticar é essencial!"

    # Jogos
    if "jogo" in p or "jogar" in p:
        return "Jogos são ótimos para aprender lógica e se divertir 🎮"

    # Sentimentos
    if "triste" in p:
        return "Sinto muito 😕 Quer conversar sobre isso?"
    if "feliz" in p:
        return "Que notícia boa! 😄 Fico feliz por você!"
    if "cansado" in p:
        return "Descansar um pouco também é importante 🛌"

    # Agradecimento
    if "obrigado" in p or "valeu" in p:
        return "De nada! Sempre que precisar estou aqui 😊"

    # Inteligência
    if "inteligente" in p:
        return "Eu tento ser útil, mas quem está aprendendo mesmo é você 🧠"

    # Perguntas de sim ou não
    if p.startswith("é") or p.startswith("vai") or p.startswith("posso"):
        return "Depende da situação, mas é possível."

    # Despedida
    if p in ["tchau", "adeus", "até mais"]:
        return "Até mais! 👋 Volte quando quiser."

    # Caso não entenda
    return (
        "Não entendi muito bem 🤔\n"
        "Digite 'ajuda' para ver tudo que posso responder."
    )

# ===============================
# INÍCIO DO BOT
# ===============================

print("🤖 Chatbot Python iniciado!")
print(mostrar_ajuda())

while True:
    usuario = input("\nVocê: ")

    if usuario.lower() == "sair":
        print("Bot: Até logo! 👋")
        break

    elif usuario.lower() == "ajuda":
        print(mostrar_ajuda())

    elif usuario.lower() == "cara":
        print("Bot:", cara_ou_coroa())

    elif usuario.lower() == "emoji":
        print("Bot:", emoji())

    else:
        print("Bot:", responder(usuario))
