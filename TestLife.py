# TestLife.py
# Ibrahim Nagib
# In 2422

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Life import *

# -----------
# Test Life
# -----------

class TestLife (TestCase):

    # -------
    # Abstract_Cell
    # -------

    # def test_Abstract_Cell_1(self):
    #     cell = Abstract_Cell("*")
    #     self.assertEqual(cell.symbol, "*")
    #     self.assertEqual(cell.live_neighbors, 0)

    # def test_Abstract_Cell_2(self):
    #     cell = Abstract_Cell("*")
    #     self.assertEqual(cell.symbol, "*")
    #     self.assertEqual(cell.live_neighbors, 0)

    # def test_Abstract_Cell_3(self):
    #     cell = Abstract_Cell("*")
    #     self.assertEqual(cell.symbol, "*")
    #     self.assertEqual(cell.live_neighbors, 0)

    # -------
    # Conway_Cell
    # -------

    def test_Conway_Cell_1(self):
        cell = Conway_Cell("*")
        self.assertEqual(cell.symbol, "*")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,1)

    def test_Conway_Cell_2(self):
        cell = Conway_Cell(".")
        self.assertEqual(cell.symbol, ".")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,0)

    def test_Conway_Cell_3(self):
        cell = Conway_Cell("*")
        self.assertEqual(cell.symbol, "*")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,1)

    def test_Conway_Cell_4(self):
        cell = Conway_Cell(".")
        self.assertEqual(cell.symbol, ".")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,0)

    def test_Conway_Cell_5(self):
        cell = Conway_Cell("*")
        self.assertEqual(cell.symbol, "*")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,1)

    def test_Conway_Cell_6(self):
        cell = Conway_Cell(".")
        self.assertEqual(cell.symbol, ".")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,0)

    # -------
    # Fredkin_Cell
    # -------

    def test_Fredkin_Cell_1(self):
        cell = Fredkin_Cell("0")
        self.assertEqual(cell.symbol, "0")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,1)

    def test_Fredkin_Cell_2(self):
        cell = Fredkin_Cell("-")
        self.assertEqual(cell.symbol, "-")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,0)

    def test_Fredkin_Cell_3(self):
        cell = Fredkin_Cell("1")
        self.assertEqual(cell.symbol, "1")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,1)

    def test_Fredkin_Cell_4(self):
        cell = Fredkin_Cell("0")
        self.assertEqual(cell.symbol, "0")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.age, 0)

    def test_Fredkin_Cell_5(self):
        cell = Fredkin_Cell("2")
        self.assertEqual(cell.symbol, "2")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,1)
        self.assertEqual(cell.age,2)

    # -------
    # Wall_Cell
    # -------

    def test_Wall_Cell_1(self):
        cell = Wall_Cell("#")
        self.assertEqual(cell.symbol, "#")
        self.assertEqual(cell.live_neighbors, 0)
        self.assertEqual(cell.status,0)

    # def test_Wall_Cell_1(self):
    #     cell = Wall_Cell("#")
    #     self.assertEqual(cell.symbol, "#")
    #     self.assertEqual(cell.live_neighbors, 0)
    #     self.assertEqual(cell.status,0)

    # def test_Wall_Cell_1(self):
    #     cell = Wall_Cell("#")
    #     self.assertEqual(cell.symbol, "#")
    #     self.assertEqual(cell.live_neighbors, 0)
    #     self.assertEqual(cell.status,0)


    # -------
    # Life
    # -------

    def test_Life_1(self):
        assert hasattr(Life, "read_board")
        assert hasattr(Life, "play_round_Conway_Cell")
        assert hasattr(Life, "run_fredkin")
        assert hasattr(Life, "run_conway")
        assert hasattr(Life, "update_board")
        assert hasattr(Life, "play_round_Fredkin_Cell")
        assert hasattr(Life, "show_board")

    def test_Life_2 (self):
        v = StringIO("3\n3\n...\n***\n...")
        game = Life(v)
        game.read_board()
        self.assertEqual(len(game.board[0]),5) # added 2 to account for the wall
        game.run_conway(1,1)
        self.assertEqual(game.board[1][2].symbol,"*")

    def test_Life_3 (self):
        v = StringIO("4\n4\n....\n....\n....\n....")
        game = Life(v)
        game.read_board()
        self.assertEqual(len(game.board[0]),6) # added 2 to account for the wall
        #game.run_conway(1,1)






main()

