
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
        assert bowling.current_frame == 2
    
    def test_throw_error(self, bowling):
        bowling.roll(9)
        with pytest.raises(Exception) as e:
            assert bowling.roll(4)
        assert 'You can only pin 10 bolls in a roll' in str(e.value)

    
    
