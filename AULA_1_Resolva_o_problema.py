meme_dict = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "STALKEAR": "Investigar a vida de alguém online",
    "VDD": "Abreviação da palavra verdade",
    "BISCOITAR": "Postar algo apenas para chamar a atenção",
    "HATER": "Pessoa que está constantemente criticando os outros",
    "VLW": "Abreviação da palavra valeu"
}

for i in range(5):
    word = input("Digite uma palavra moderna que você não entende (escreva toda a palavra em letras maiúsculas): ")

    if word in meme_dict.keys():
        print(word + " significa: " + meme_dict[word])
    else:
        print("Essa palavra não está no dicionário ainda...")