from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_score()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()
        self.score = 0

    @staticmethod
    def get_score():
        file = open("data.txt")
        h_scr = int(file.read())
        file.close()
        return h_scr


    def save_score(self):
        file = open("data.txt", 'w')
        file.write(f"{self.high_score}")
        file.close()


    # def game_over(self, cause):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    #     print(cause)
