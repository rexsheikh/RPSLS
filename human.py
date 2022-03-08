from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.score = 0

    def choose_gesture(self):
        for i in range(0, len(self.gestures)):
            print(f"{i} : {self.gestures[i]}")
        self.gesture_choice = int(input(f'Choose the number corresponding to the gesture choice: '))
        if self.gesture_choice not in list(range(0,5)):
            print('Please enter a number between 0 and 4')
            self.choose_gesture()
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
