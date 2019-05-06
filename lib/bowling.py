class Bowling:
    def __init__(self):
        self._frame = []
        self._all_rolls = []
        self._current_frame = 1

    def roll(self, pins):
        if len(self._frame) >= 2:
            self._frame =[]
            self._current_frame += 1
        self._frame.append(pins)
        self._all_rolls.append(pins)

    def score(self):
        result = sum(self._all_rolls)
        return result
    