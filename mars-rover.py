import unittest

DIRECTIONS = {"N": 1, "E": 2, "S": 3, "W": 4}


class Rover:
    def __init__(self, x, y, heading="N"):
        self.x = x
        self.y = y
        self.heading = DIRECTIONS[heading]  # int

    def turn_left(self):
        self.heading = DIRECTIONS["W"] if (self.heading - 1) < 1 else self.heading - 1

    def turn_right(self):
        self.heading = DIRECTIONS["N"] if (self.heading + 1) > 4 else self.heading + 1


class TestRover(unittest.TestCase):
    def test_turn_left(self):
        rover = Rover(1, 2, "N")
        rover.turn_left()
        self.assertEqual(rover.heading, DIRECTIONS["W"])

        rover.turn_left()
        self.assertEqual(rover.heading, DIRECTIONS["S"])

    def test_turn_right(self):
        rover = Rover(1, 2, "N")
        rover.turn_right()
        self.assertEqual(rover.heading, DIRECTIONS["E"])

        rover.turn_right()
        rover.turn_right()
        rover.turn_right()  # N

        self.assertEqual(rover.heading, DIRECTIONS["N"])


if __name__ == "__main__":
    unittest.main()


# # # #
# # X #
# # # #
# # # #
