from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as highscore:
            self.highscore = int(highscore.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=420)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}", align="center", font=("Arial", 15, "bold"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 15, "bold"))
