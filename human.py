from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.score = 0

    def choose_gesture(self):
        for i in range(0, len(self.player1.gestures)):
            print(f"{i} : {self.player1.gestures[i]}")
        self.gesture_choice = int(input(f'Choose the number corresponding to the gesture choice: '))
        return self.gesture_choice
        
    # def choose_gesture(self):
    #     gesture_index = 0
    #     for gesture in self.gestures:
    #         print(f"Choose {gesture_index} for {gesture}: ")
    #         gesture_index += 1
    #     human_input = int(input("Choose your gesture! "))
    #     if human_input in ("0", "1", "2", "3", "4"):
    #         self.chosen_gesture = human_input
    #         print(f"Player one chose {self.gestures[int(self.chosen_gesture)]}")
    #     else:
    #         print("Please enter number value 0-4 to choose gesture")
    #         self.choose_gesture()
