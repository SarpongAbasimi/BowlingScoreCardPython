class Bowling:
    def __init__(self):
        self.frame = []
        self.all_rolls = []
        self.current_frame = 1

    def roll(self, pins):
        self.error(pins)
        self.check_frame_length()

        self.frame.append(pins)
        self.all_rolls.append(pins)

    def score(self):
        score = 0
        for pin_down in range(len(self.all_rolls)):
            score += self.all_rolls[pin_down]
        return score

    def error(self, pins):
        if len(self.frame) == 1 and self.frame[0] + pins > 10:
            raise Exception('You can only pin 10 bolls in a roll' )

    def check_frame_length(self):
        if len(self.frame) >= 2:
            self.frame =[]
            self.current_frame += 1

b = Bowling()
b.roll(5)
b.roll(5)
b.roll(1)
b.roll(5)
b.roll(5)
b.roll(1)
print(b.score())
