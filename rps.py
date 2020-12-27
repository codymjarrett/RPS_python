import random

options = ('rock', 'paper', 'scissors')


def get_player_one_option():
    return input("Make a play ('q' to quit): ").lower()


def get_player_two_option():
    option = random.randint(0, 2)
    return options[option]


def get_winner(player_one, player_two):
    print(f">>Player One has chosen {player_one}")
    print(f">>Player Two has chosen {player_two}")

    if player_one == player_two:
        return 'both'

    # if rock
    if player_one == options[0]:
        # if paper
        if player_two == options[1]:
            return 'player_two'
        # if scissors
        elif player_two == options[2]:
            return 'player_one'
    # if paper
    elif player_one == options[1]:
        # if rock
        if player_two == options[0]:
            return 'player_one'
        # if scissors
        elif player_two == options[2]:
            return 'player_two'
    # if scissors
    elif player_one == options[2]:
        # if rock
        if player_two == options[0]:
            return 'player_two'
        # if paper
        elif player_two == options[1]:
            return 'player_one'


def announce_winner(winner):
    if winner == 'both':
        print(">>>It's a draw folks!")
    elif winner == 'player_one':
        print(">>>Player One Wins")
    else:
        print(">>>Player Two Wins")


def ask_to_play_again():
    answer = input('Would you like to play again? (y/n): ').strip().lower()
    if answer == 'y':
        play_game()
    elif answer == 'n':
        print('>>Thanks for playing, goodbye!')
    else:
        ask_to_play_again()


def play_game():
    player_one = get_player_one_option()
    if player_one == 'q':
        print('>>Thanks for playing, goodbye!')
        return
    elif (player_one == options[0]) or (player_one == options[1]) or (player_one == options[2]):
        player_two = get_player_two_option()
        winner = get_winner(player_one, player_two)
        announce_winner(winner)
        ask_to_play_again()
    else:
        print("Must type either 'rock', 'paper' or 'scissors'")
        play_game()


play_game()
