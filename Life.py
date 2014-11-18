# Life

class AbstractCell:
    def __init__(self, symbol):
        #self.name 
        self.symbol = symbol
        self.live_neighbors = 0

class ConwayCell(AbstractCell):
   def __init__(self, symbol):
       # self.name = ""
       AbstractCell.__init__(self, symbol)
       if symbol == "*":
           self.name = "alive"
           self.code = 1
       elif symbol == ".":
           self.name = "dead"
           self.code = 0

class FredkinCell(AbstractCell):
   def __init__(self, symbol):
       AbstractCell.__init__(symbol)
       if symbol == "-":
           self.name = "dead"
       elif type(symbol) == int:
           self.name = "alive"
           self.age = int(symbol)
       elif symbol == "+":
           self.name = "alive"
           self.age = 11
       self.live_neighbors = 0


class WallCell(AbstractCell):
   def __init__(self, symbol):
       AbstractCell.__init__(self, symbol)
       self.name = "wall"
       self.live_neighbors = 0
       self.code = 0


class Life:
    def __init__(self):
        self.board = []
        self.rows = 0
        self.cols = 0
        self.population = 0

    def read_board(self, file):
        infile = open(file,"r")
        self.cols = int(infile.readline())+2
        self.rows = int(infile.readline())+2
        self.board = [[WallCell("#") for i in range(self.rows)] for j in range(self.cols)]
        for i in range(self.cols-2):
            x = infile.readline()
            for j in range (self.rows-2):
                if x[j] == "." or "*":
                    cell = ConwayCell(x[j])
                else:
                    cell = Fredkin(x[j])
                self.board[i+1][j+1] = cell

    def play_round_fredkin(self):
        """
        Play...
        """
        i = 0
        j = 0

        for x in self.boards:
            for f in x:
                j += 1
                if f.symbol == "*":
                    for m in range(i-1,i+1):
                        for n in range(j-1,j+1):
                            self.board[m][n].live_neighbors += 1

            i += 1
            
    def play_round_ConwayCell(self):
       """
       Play...
       """
       for x in self.board:
           for f in x:
               f.live_neighbors = 0

       for i in range(1, self.cols - 1):
           for j in range(1, self.rows - 1):
               code = self.board[i][j].code
               for m in range(i - 1, i + 2):
                   for n in range(j - 1, j + 2):
                       self.board[m][n].live_neighbors += code
               self.board[i][j].live_neighbors -= code

    def run(self, rounds):
        gen = 0
        print("Generation = ", gen, "Population = ",self.population)
        self.show_board()
        gen += 1
        while rounds > 0:
            self.play_round_ConwayCell()
            self.update_board()
            print("Generation = ",gen, "Population = ", self.population)
            self.show_board()
            rounds -=1
            gen += 1


    def update_board(self):
        self.population = 0
        for x in self.board:
            for f in x:
                if f.name == "dead":
                    if f.live_neighbors == 3:
                        f.name = "alive"
                        f.symbol ="*"
                        f.code = 1

                elif f.name == "alive":
                    self.population += 1
                    if not((f.live_neighbors == 2 or f.live_neighbors == 3)):
                        # f.symbol = "*"
                        # f.name = "alive"
                    # else:
                        f.symbol = "."
                        f.name = "dead"
                        f.code = 0


        

    def show_board(self):
        """
        shows board by printing each array in the 2d array
        on a new line, seperated by spaces
        """

        # for s in self.board:
        #     print(' '.join(str(x.live_neighbors) for x in s))
            
        for s in self.board[1:-1]:
            print(' '.join(x.symbol for x in s[1:-1]))




game = Life()
game.read_board("RunLife.in.txt")
# game.show_board()
game.run(5)
#game.show_board()
