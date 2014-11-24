# Life.py
# Ibrahim Nagib
# In 2422


class Abstract_Cell:
    """
    class Abstract_Cell creates Abstract_Cell objects that 
    can become either a Fredkin_Cell or a Conway_Cell,
    both are derived from this Parent class
    """
    def __init__(self, symbol):
        self.symbol = symbol
        self.live_neighbors = 0

class Conway_Cell(Abstract_Cell):
   """
   class Conway_Cell is derived from the class Abstract_Cell,
   it defines a Conway_Cell, its symbol is '*' if alive, 
   and '.' if dead. It's status is 1 if alive, and 0 if dead.
   Int 1 and 0 were used in order to reduce the if statements 
   needed to increment the live neighbors. This way, we will 
   simply add status (1 or 0) to all neighbors regardless.
   """

   def __init__(self, symbol):
       Abstract_Cell.__init__(self, symbol)
       self.name = "conway"
       if symbol == "*":
          self.status = 1
       elif symbol == ".":
          self.status = 0

class Fredkin_Cell(Abstract_Cell):
   """
   class Fredkin_Cell is derived from the class Abstract_Cell,
   it defines a Fredkin_Cell, its symbol is its age if alive, 
   and '-' if dead. It's status is 1 if alive, and 0 if dead, 
   similar to Conway_Cell. A Fredkin_Cell becomes a Conway_Cell if 
   it ages past age 2.
   """
   def __init__(self, symbol):
       Abstract_Cell.__init__(self,symbol)
       self.name = "fredkin"
       if symbol == "-":
          self.status = 0
          self.age = 0
       else:
          self.status = 1
          self.age = int(symbol)

class Wall_Cell(Abstract_Cell):
   """
   class Wall_Cell is derived from the class Abstract_Cell,
   it defines a Wall_Cell, its symbol is '#' and is always "dead". 
   It's status is always 0 , and therefore will not interupt any of 
   characters on the board, but creates a buffer and eliminates the need
   for if statements at sides and corners.
   """
   def __init__(self, symbol):
       Abstract_Cell.__init__(self, symbol)
       self.name = "wall"
       self.live_neighbors = 0
       self.status = 0


class Life:
    """
    Class Life owns the game of life and creates game objects.
    It has a board, which is read in using Life's read_board method.
    It plays each round and prints the boards that are called to be shown.
    """
    def __init__(self,infile):
        self.board = []
        self.rows = 0
        self.cols = 0
        self.population = 0
        #self.infile = open(textfile,"r")
        self.infile = infile

    def read_board(self):
        """
        read_board method reads the starting positions of the board,
        and depending on the symbols it finds, assigns them accordingly
        to either a Conway_Cell, Fredkin_Cell, or Wall_Cell.
        """
        self.population = 0
        self.cols = int(self.infile.readline())+2
        self.rows = int(self.infile.readline())+2
        self.board = [[Wall_Cell("#") for i in range(self.rows)] for j in range(self.cols)]
        for i in range(self.cols-2):
            x = self.infile.readline()
            for j in range (self.rows-2):
                if x[j] == "." :
                    cell = Conway_Cell(x[j])
                elif x[j] == "*":
                    cell = Conway_Cell(x[j])
                    self.population += 1
                elif x[j] == "-":
                    cell = Fredkin_Cell(x[j])
                elif x[j] == "0":
                    cell = Fredkin_Cell(x[j])
                    self.population += 1

                self.board[i+1][j+1] = cell
        self.infile.readline()   
        """
        After read board is called, it prints the board it has read, 
        this board is Generation 0, it also prints the inital population
        on the board.
        """    
        print("Generation = 0 ", "Population = ",self.population)
        self.show_board()
        print()


    def play_round_Fredkin_Cell(self):
      """
      play_round_Fredkin_Cell iterates through the entire board, 
      adding each cell's status (1 or 0) to all of it's neighbors,
      which for fredkin, are 4.
      """
      for x in self.board:
        for f in x:
          f.live_neighbors = 0

      for i in range(1, self.cols - 1):
           for j in range(1, self.rows - 1):
               status = self.board[i][j].status
               for m in range(i-1 , i +2):
                   self.board[m][j].live_neighbors += status
               for n in range(j-1 , j +2):
                   self.board[i][n].live_neighbors += status

      self.board[i][j].live_neighbors -= status

    def play_round_Conway_Cell(self):
       """
       play_round_Conway_Cell iterates through the entire board, 
       adding each cell's status (1 or 0) to all of it's neighbors,
       which for conway, are 8 total.
       """
       for x in self.board:
           for f in x:
               f.live_neighbors = 0

       for i in range(1, self.cols - 1):
           for j in range(1, self.rows - 1):
               status = self.board[i][j].status

               for m in range(i - 1, i + 2):
                   for n in range(j - 1, j + 2):
                       self.board[m][n].live_neighbors += status
               self.board[i][j].live_neighbors -= status

    def run_conway(self, rounds, shown):
        gen = 1
        while rounds > 0:
            self.population = 0
            self.play_round_Conway_Cell()
            self.update_board()

            if gen % shown == 0:
              print("Generation = ",gen , "Population = ", self.population)
              self.show_board()
              print()
            rounds -=1
            gen += 1

    def run_fredkin(self, rounds, shown):
        gen = 1
        while rounds > 0:
            self.population = 0
            self.play_round_Fredkin_Cell()
            self.update_board()

            if gen % shown == 0:
              print("Generation = ",gen , "Population = ", self.population)
              self.show_board()
              print()
            rounds -=1
            gen += 1

    def update_board(self):
        """
        update_board iterates through the board, according to the 
        cell it is on, it checks, its status, and whether its Fredkin_Cell 
        or Conway_Cell. According the their respective rules, it changes the cells
        from dead to alive, or vise versa. also ages the Fredkin_Cells accordingly.
        update_board also increments the population of the board accordinly for the 
        next board.
        """
        for x in self.board:
            for f in x:
                if f.status == 0:
                    if f.name == "conway":
                        if f.live_neighbors == 3:
                            f.symbol ="*"
                            f.status = 1
                            self.population += 1
                    elif f.name == "fredkin":
                        if f.live_neighbors == 1 or f.live_neighbors == 3 :
                            f.status = 1
                            f.symbol = str(f.age)
                            self.population += 1
                    else:
                        f.status = 0

                elif f.status == 1:
                    if f.name == "conway":
                        if not((f.live_neighbors == 2 or f.live_neighbors == 3)):
                            f.symbol = "."
                            f.status = 0
                        else:
                          self.population += 1
                    elif f.name == "fredkin":
                        if f.live_neighbors == 1 or f.live_neighbors == 3:
                            f.status = 1
                            f.age += 1
                            if f.age <= 2:
                              f.symbol = str(f.age)
                              self.population += 1
                            else:
                              self.board.replace(f, Conway_Cell("*"))
                        else:
                          f.status = 0
                          f.symbol = "-"



        

    def show_board(self):
        """
        shows board by printing each array in the 2d array
        on a new line. Only prints [1:-1] in both the outer
        and inner arrays. Those indexes are the Wall.
        """

        for s in self.board[1:-1]:
            print(''.join(x.symbol for x in s[1:-1]))




