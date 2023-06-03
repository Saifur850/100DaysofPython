from turtle import Turtle


class ScoreBroad(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())

        # self.high_score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {round(self.score,0)} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
            self.high_score = self.score
        self.score = 0
        self.update_score()




    def increase_score(self, point):
        self.score += point
        self.clear()
        self.update_score()
