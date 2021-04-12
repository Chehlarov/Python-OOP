from player import Player


class Controller:
    def __init__(self):
        pass

    def start_game(self):
        """This is game between human and machine"""
        print("You are playing against the machine")
        player_name = input("Input your name")
        player_secret_num = int(
            input("What is your secret num? (The info will be used only to autocomplete the answers) ")
        )
        print("------------------------------------------")

        player = Player(player_name, player_secret_num)
        computer = Player("Computer")

        while True:
            # Player is first
            player.player_guess()
            feedback = computer.reply_to_suggestion(player.my_guesses[-1])
            if feedback == (4, 0):
                print(f"{player.name} wins!!!")
                break
            # print(player.possible_opponent_nums) #TODO debug only
            # the player must receive the feedback and make notes, used for next guesses

            # computer turn
            computer.make_guess()
            feedback = player.reply_to_suggestion(computer.my_guesses[-1])
            computer.receive_feedback(feedback)
            if feedback == (4, 0):
                print(f"{computer.name} wins!!!")
                break
            print(computer.possible_opponent_nums) #TODO debug only
        print("END OF GAME")
