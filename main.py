import string
import random


def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password


def main():
    print("Bem-vindo ao gerador de senhas!")

    while True:
        try:
            length = int(input("Digite o comprimento da senha: "))
            if length <= 0:
                raise ValueError("O comprimento deve ser um número positivo.")
            use_letters = input("Incluir letras? (s/n): ").lower() == 's'
            use_numbers = input("Incluir números? (s/n): ").lower() == 's'
            use_symbols = input("Incluir símbolos? (s/n): ").lower() == 's'

            password = generate_password(length, use_letters, use_numbers, use_symbols)
            print(f"Sua senha gerada é: {password}")
        except ValueError as e:
            print(e)

        play_again = input("Você quer gerar outra senha? (s/n): ").lower()
        if play_again != 's':
            print("Obrigado por usar o gerador de senhas! Até a próxima!")
            break


if __name__ == "__main__":
    main()
