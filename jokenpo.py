import random

def usuario_choice():
    choice = input("Escolha pedra (1), papel (2) ou tesoura (3): ")
    if choice.lower() == '1':
        return 'pedra'
    elif choice.lower() == '2':
        return 'papel'
    elif choice.lower() == '3':
        return 'tesoura'
    else:
        print("Escolha inválida. Por favor, tente novamente.")
        return usuario_choice()

def computador_choice():
    choices = ['pedra', 'papel', 'tesoura']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (
        (user_choice == 'pedra' and computer_choice == 'tesoura') or
        (user_choice == 'papel' and computer_choice == 'pedra') or
        (user_choice == 'tesoura' and computer_choice == 'papel')
    ):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def play_game():
    print("Bem-vindo ao Pedra, Papel e Tesoura!")
    while True:
        user_choice = usuario_choice()
        computer_choice = computador_choice()
        print(f"\nVocê escolheu: {user_choice}")
        print(f"O computador escolheu: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("\nDeseja jogar novamente? (s/n): ")
        if play_again.lower() != 's':
            break
play_game()