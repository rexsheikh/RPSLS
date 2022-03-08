from player import Player
from human import Human
from ai import AI   
import random
import time

class Game():
    def __init__(self):
        self.win_loss_table = [['draw','p1','p2','p2','p1'],['p2','draw','p1','p1','p2'],['p1','p2','draw','p2','p1'],['p1','p2','p1','draw','p2'],['p2','p1','p2','p1','draw']]

    def run_game(self):
        self.display_welcome()
        time.sleep(1)
        self.display_rules()
        time.sleep(1)
        game_type = self.choose_player_options()
        if game_type == 1:
            while(self.player1.score < 2 and self.player2.score < 2):
                print(f'player 1 score: {self.player1.score}')
                print(f'player 2 score: {self.player2.score}')
                self.player1_choice = self.display_gesture_options()
                self.player2_choice = self.display_gesture_options()
                print(f"Player one chose {self.player1.gestures[self.player1_choice]} and Player 2 chose {self.player2.gestures[self.player2_choice]} \n")
                self.winner = self.win_loss_table[self.player2_choice][self.player1_choice]
                if self.winner == 'p1':
                    self.player1.increment_score()
                    print('Player 1 scores!')
                elif self.winner == 'p2':
                    self.player2.increment_score()
                    print('Player 2 scores!')
                else:
                    print('draw!')
        elif game_type == 2:
            while(self.player1.score < 2 and self.player2.score < 2):
                print(f'player 1 score: {self.player1.score}')
                print(f'AI score: {self.player2.score}')
                self.player1_choice = self.display_gesture_options()
                self.player2_choice = self.ai_player_input()
                print(f"Player one chose {self.player1.gestures[self.player1_choice]} and the AI chose {self.player2.gestures[self.player2_choice]}\n")
                self.winner = self.win_loss_table[self.player2_choice][self.player1_choice]
                if self.winner == 'p1':
                    self.player1.increment_score()
                    print('Player 1 scores!')
                elif self.winner == 'p2':
                    self.player2.increment_score()
                    print('AI scores!')
                else:
                    print('draw!')
        self.display_winner()
        self.another_game()

    def display_welcome(self):
        print("welcome to rock/paper/scissor/spock/lizard!")
        pass

    def display_rules(self):
        print("Here are the rules:\n \
             Rock crushes Scissors\n \
             Scissors cuts Paper\n \
             Paper covers Rock\n \
             Rock crushes Lizard\n \
             Lizard poisons Spock\n \
             Spock smashes Scissors\n \
             Scissors decapitates Lizard\n \
             Lizard eats Paper\n \
             Paper disproves Spock\n \
             Spock vaporizes Rock")

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
        return self.ai_gesture

    def display_winner(self):
        #prints the name of the winner
        #ask the user if they want to play again
        pass


#steph
    # def play_game(self):
    #     self.player1.choose_gesture()
    #     self.player2.choose_gesture()
    #     if self.player1.chosen_gesture == self.player2.chosen_gesture:
    #         print("It's a tie! Please try again!")
    #         self.display_winner()
    #     elif (self.player1.chosen_gesture, self.player2.chosen_gesture) in self.winning_conditions:
    #         print("Player one wins!")
    #         self.player1.score += 1
    #         self.display_winner()
    #     else:
    #         print("Player two wins!")
    #         self.player2.score += 1
    #         self.display_winner()
    #     print()


    def display_winner(self):
        if self.player1.score == 2:
            print("Player one is the winner!")
        elif self.player2.score == 2:
            print("Player two is the winner!")
        else:
            print()
            print("Continue playing until one player reaches two wins!")
            self.play_game()
        print()
    
    def another_game(self):
        while True:
            replay_answer = input("Would you like to play again? (y/n) ")
            if replay_answer == 'y':
                self.clear_score()
                self.run_game()
                break
            elif replay_answer == 'n':
                print('Thanks for playing!')
                break
            else:
                print('Please enter a valid answer!')
                self.another_game()
        print()

    def clear_score(self):
        self.player1.score = 0
        self.player2.score = 0
        self.run_game()
