
from lib.bowling import Bowling
import pytest


@pytest.fixture()
def bowling():
    bowling = Bowling()
    return bowling

class Test_Bowling:
    def test_score_gutters(self, bowling):
        for i in range(20):
            bowling.roll(0)
        assert bowling.score() == 0

    def test_all_one(self, bowling):
        for i in range(20):
            bowling.roll(1)
        assert bowling.score() == 20
    
    def test_move_frame(self, bowling):
        bowling.roll(3)
        bowling.roll(4)
        bowling.roll(2)
        assert bowling._current_frame == 2
    
    
