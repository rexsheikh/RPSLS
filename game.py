from player import Player
from human import Human
from ai import AI   


class Game():

    def __init__(self) -> None:
        pass

    def run_game(self):
        #comparison of choices
        #increment scoreboard
        #check if winner exists (first to two)
        #display winner 
        pass

    def display_welcome(self):
        print("welcome to rock/paper/scissor/spock/lizard!")
        pass

    def display_rules(self):
        print("Rock crushes Scissors\n \
             Scissors cuts Paper\n \
                  Paper covers Rock\n \
                       Rock crushes Lizard\n \
                            Lizard poisons Spock\n \
                                Spock smashes Scissors\n \
                                     Scissors decapitates Lizard\n \
                                          Lizard eats Paper\n \
                                               Paper disproves Spock\n \
                                                    Spock vaporizes Rock")
        pass

    def choose_player_options(self):
        self.user_input = int(input("press 1 for PvP or 2 to play the AI: "))

        if self.user_input == 1:
            self.player1 = Human()
            self.player2 = Human()
        elif self.user_input == 2:
            self.player1 = Human()
            self.player2 = AI()
        else:
            print('error. enter 1 or 2.')
            self.choose_player_options()




    def display_gesture_options(self):
        pass

    def human_player_input(self):
        #display gestures and receive an input 
        pass

    def ai_player_input(self):
        #randomly choose an input
        pass

    def display_winner(self):
        #prints the name of the winner
        #ask the user if they want to play again
        pass
