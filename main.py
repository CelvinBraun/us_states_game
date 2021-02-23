from turtle import Screen
from states import States_Game

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

game_is_on = True
game = States_Game()

# game start
game.answer = screen.textinput(title="Guess the state", prompt="Name a state: ").capitalize()
game.check_answer()
while game_is_on:
    game.answer = screen.textinput(title=f"Guess the state {game.named_states}/50", prompt="Name another state: ").capitalize()

    game.check_answer()
    game_is_on = game.game_over()

    # game exit
    if game.answer == "Exit":
        game_is_on = False

screen.exitonclick()