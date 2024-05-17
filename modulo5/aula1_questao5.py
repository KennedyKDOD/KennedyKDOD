import emoji

#emojis disponíveis
print("Emojis disponíveis:")
print(f"❤️ - :red_heart:")
print(f"👍 - :thumbs_up:")
print(f"🤔 - :thinking_face:")
print(f"🥳 - :partying_face:")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")

# Converte a frase codificada para uma frase com emojis
frase_emojizada = emoji.emojize(frase_codificada)

# Exibe a frase emojizada
print("\nFrase emojizada:")
print(frase_emojizada)
