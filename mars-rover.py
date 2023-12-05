import unittest

DIRECTIONS = {"N": 1, "E": 2, "S": 3, "W": 4}


class Plateau:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def can_move(self, position):
        # check inbounds
        return 0 <= position.x <= self.width and 0 <= position.y <= self.height


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rover:
    def __init__(self, x, y, heading, plateau):
        self.position = Position(x, y)
        self.heading = DIRECTIONS[heading]  # int
        self.plateau = plateau

    def turn_left(self):
        self.heading = DIRECTIONS["W"] if (self.heading - 1) < 1 else self.heading - 1

    def turn_right(self):
        self.heading = DIRECTIONS["N"] if (self.heading + 1) > 4 else self.heading + 1

    def move(self):
        if not self.plateau.can_move(self.position):
            return False

        if self.heading == DIRECTIONS["N"]:
            self.position.y += 1
        elif self.heading == DIRECTIONS["E"]:
            self.position.x += 1
        elif self.heading == DIRECTIONS["S"]:
            self.position.y -= 1
        else:
            self.heading.x -= 1

        return True

    def process_command(self, command):
        # command L, R, M
        if command == "L":
            self.turn_left()
        elif command == "R":
            self.turn_right()
        else:
            self.move()


class TestRover(unittest.TestCase):
    def test_turn_left(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, "N", plateau)
        rover.turn_left()
        self.assertEqual(rover.heading, DIRECTIONS["W"])

        rover.turn_left()
        self.assertEqual(rover.heading, DIRECTIONS["S"])

    def test_turn_right(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, "N", plateau)
        rover.turn_right()
        self.assertEqual(rover.heading, DIRECTIONS["E"])

        rover.turn_right()
        rover.turn_right()
        rover.turn_right()  # N

        self.assertEqual(rover.heading, DIRECTIONS["N"])

    def test_move(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, "N", plateau)
        self.assertEqual(rover.position.x, 1)
        self.assertEqual(rover.position.y, 2)

        rover.move()

        self.assertEqual(rover.position.y, 3)

    def test_can_not_move(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 6, "N", plateau)
        self.assertEqual(rover.move(), False)

    def test_process_L_command(self):
        command = "L"
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, "N", plateau)
        rover.process_command(command)
        self.assertEqual(rover.heading, DIRECTIONS["W"])

    def test_process_R_command(self):
        command = "R"
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, "N", plateau)
        rover.process_command(command)
        self.assertEqual(rover.heading, DIRECTIONS["E"])

    def test_process_M_command(self):
        command = "M"
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, "N", plateau)

        self.assertEqual(rover.position.x, 1)
        self.assertEqual(rover.position.y, 2)

        rover.process_command(command)

        self.assertEqual(rover.position.y, 3)


class PlateauTest(unittest.TestCase):
    def test_can_move(self):
        plateau = Plateau(5, 5)
        position = Position(1, 5)
        self.assertTrue(plateau.can_move(position))

    def test_can_not_move(self):
        plateau = Plateau(5, 5)
        position = Position(1, 6)
        self.assertFalse(plateau.can_move(position))


if __name__ == "__main__":
    unittest.main()

# # # # # #
# # R # # #
# # # # # #
# # # # # #

# N -> y + 1
# E -> x + 1
# S -> y - 1
# W -> x - 1


# Turn left and right
#
