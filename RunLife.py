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
from Life import *

# ---------------------
# Life Conway_Cell 21x13
# ---------------------

print("*** Life Conway_Cell 21x13 ***")
print()
"""
Simulate 12 evolutions.
Print every grid (i.e. 0, 1, 2, 3, ... 12)
"""

infile = open("RunLife.in", "r")

game = Life(infile)
game.read_board()

game.run_conway(12,1)

# ---------------------
# Life Conway_Cell 20x29
# ---------------------

print("*** Life Conway_Cell 20x29 ***")
print()
"""
Simulate 28 evolutions.
Print every 4th grid (i.e. 0, 4, 8, ... 28)
"""

game.read_board()

game.run_conway(28,4)

# ----------------------
# Life Conway_Cell 109x69
# ----------------------

print("*** Life Conway_Cell 109x69 ***")
print()
"""
Simulate 283 evolutions.
Print the first 10 grids (i.e. 0, 1, 2...9).
Print the 283rd grid.
Simulate 40 evolutions.
Print the 323rd grid.
Simulate 2177 evolutions.
Print the 2500th grid.
"""
game.read_board()

game.run_conway(10,1)
game.run_conway(283,283)
game.run_conway(323,323)
game.run_conway(2500,2500)

# ----------------------
# Life Fredkin_Cell 20x20
# ----------------------

print("*** Life Fredkin_Cell 20x20 ****")
print()
"""
Simulate 5 evolutions.
Print every grid (i.e. 0, 1, 2, ..., 5)
"""
game.read_board()

game.run_fredkin(5,1)