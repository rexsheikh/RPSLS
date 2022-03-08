from player import Player
from human import Human
from ai import AI   
import random

class Game():
    def __init__(self):
        self.win_loss_table = [['draw','p1','p2','p2','p1'],['p2','draw','p1','p1','p2'],['p1','p2','draw','p2','p1'],['p1','p2','p1','draw','p2'],['p2','p1','p2','p1','draw']]


    def run_game(self):
        self.display_welcome()
        self.display_rules()
        game_type = self.choose_player_options()
        self.player1_score = 0
        self.player2_score = 0
        if game_type == 1:
            self.player1_choice = self.display_gesture_options()
            self.player2_choice = self.display_gesture_options()
            self.winner = self.win_loss_table[self.player1_choice][self.player2_choice]
            if self.winner == 'p1':
                self.player1_score += 1
                print(f'player 1 score: {self.player1_score}')
                print(f'player 2 score: {self.player2_score}')
            elif self.winner == 'p2':
                self.player2_score += 1
            else:
                pass
        else: 
            #human v ai 
            pass
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
        return self.user_input

    def display_gesture_options(self):
        for i in range(0, len(self.player1.gestures)):
            print(f"{i} : {self.player1.gestures[i]}")
        self.gesture_choice = int(input(f'Choose the number corresponding to the gesture choice: '))
        return self.gesture_choice


    def ai_player_input(self):
        self.ai_gesture = random.randint(0,4)
        print(f'the AI has chosen {self.player2.gestures[self.ai_gesture]}')

    def display_winner(self):
        #prints the name of the winner
        #ask the user if they want to play again
        pass
