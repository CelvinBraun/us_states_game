from turtle import Turtle
import pandas

csv_data = pandas.read_csv("50_states.csv")

class States_Game(Turtle):

    def __init__(self):
        super().__init__()
        # turtle settings
        self.hideturtle()
        self.penup()

        # general variables
        self.answer = ""
        self.state_list = []
        self.answer_list = []
        self.named_states = 0

        #call of init function
        self.create_list()

    # creates list for simple loop possibility
    def create_list(self):
        for index, row in csv_data.iterrows():
            self.state_list.append(row["state"])

    # checks when answer is correct and send the x,y value to the mark function
    def check_answer(self):
        for state in self.state_list:
            if state == self.answer:
                # search in answer_list for already named states
                mark = True
                for answer_state in self.answer_list:
                    if answer_state == self.answer:
                        mark = False
                # when not named -> get x/y cor
                if mark == True:
                    temp_data = csv_data[csv_data["state"] == state]
                    x = temp_data["x"].item()
                    y = temp_data["y"].item()
                    self.mark_on_map(x, y)

    def mark_on_map(self, x, y):
        self.goto(x, y)
        self.write(self.answer)
        self.answer_list.append(self.answer)
        self.named_states += 1

    def game_over(self):
        if len(self.answer_list)==50:
            print("Congratulations, you know all U.S. States!")
            return False
        else:
            return True