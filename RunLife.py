#!/usr/bin/env python3

# ---------------------------
# projects/collatz/RunLife.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# -------
# imports
# -------

import sys
from trialife import *

# ---------------------
# Life ConwayCell 21x13
# ---------------------

print("*** Life ConwayCell 21x13 ***")
"""
Simulate 12 evolutions.
Print every grid (i.e. 0, 1, 2, 3, ... 12)
"""

game = Life("RunLife.in.txt")
game.read_board()
game.run(1,1)

# ---------------------
# Life ConwayCell 20x29
# ---------------------

print("*** Life ConwayCell 20x29 ***")
"""
Simulate 28 evolutions.
Print every 4th grid (i.e. 0, 4, 8, ... 28)
"""
#game = Life()
# game.read_board()
# game.run(4,4)

# ----------------------
# Life ConwayCell 109x69
# ----------------------

print("*** Life ConwayCell 109x69 ***")
"""
Simulate 283 evolutions.
Print the first 10 grids (i.e. 0, 1, 2...9).
Print the 283rd grid.
Simulate 40 evolutions.
Print the 323rd grid.
Simulate 2177 evolutions.
Print the 2500th grid.
"""
# game.read_board()
# game.run(10,1)
# game.run(283,283)
# game.run(323,323)
# game.run(2500,2500)
# game.run(283,283)
# ----------------------
# Life FredkinCell 20x20
# ----------------------

print("*** Life FredkinCell 20x20 ****")
"""
Simulate 5 evolutions.
Print every grid (i.e. 0, 1, 2, ..., 5)
"""
# game.read_board()
# game.runF(5,1)
