from player import Player


class Controller:
    def __init__(self):
        pass

    def start_game(self):
        """This is game between human and machine"""
        print("You are playing against the machine")
        player_name = input("Input your name: ")
        player_secret_num = int(
            input("What is your secret num? (The info will be used only to autocomplete the answers) ")
        )
        print("------------------------------------------")

        player = Player(player_name, player_secret_num)
        computer = Player("Computer")

        while True:
            # Player is first
            print(f"{player.name}, take this hint - choose one from the list: ")
            print(player.possible_opponent_nums)
            num = int(input(f"{player.name}, please make a guess: "))
            player.make_guess(num)
            b, c = Player.check_b_and_c(computer.secret_num, player.my_guesses[-1])
            print(f"{computer.name}: You have {b} bulls and {c} cows")
            player.receive_feedback((b, c))

            if b == 4:
                    print(f"{player.name} wins!!!")
                    break
                # the player must receive the feedback and make notes, used for next guesses

                # computer turn
            computer.make_guess()
            print(f"{computer.name}: I guess {computer.my_guesses[-1]}")
            b, c = Player.check_b_and_c(player.secret_num, computer.my_guesses[-1])
            print(f"{player.name}: You have {b} bulls and {c} cows")
            computer.receive_feedback((b, c))
            if b == 4:
                print(f"{computer.name} wins!!!")
                break
            print(f"{computer.name}: I know your num is this list: ")
            print(computer.possible_opponent_nums)
        print("END OF GAME")
