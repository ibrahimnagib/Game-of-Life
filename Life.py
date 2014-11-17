# Life

class Abstract:
    def __init__(self, symbol):
        #self.name 
        self.symbol = symbol
        #self.live_neighbors = 0

class Conway(Abstract):
    def __init__(self,symbol):
        #self.name = ""
        Abstract.__init__(self, symbol)
        if symbol == "*":
            self.name = "alive"
        elif symbol == ".":
            self.name = "dead"

        self.live_neighbors = 0

class Fredkin(Abstract):
    def __init__(self,symbol):
        Abstract.__init__(symbol)
        if symbol == "-":
            self.name = "dead"
        elif type(symbol) == int: 
            self.name = "alive"
            self.age = int(symbol)
        elif symbol == "+":
            self.name = "alive"
            self.age = 11
        self.live_neighbors = 0

class Wall(Abstract):
    def __init__(self,symbol):
        Abstract.__init__(self, symbol)
        self.name = "wall"
        self.live_neighbors =  0

class Life:
    def __init__(self):
        self.board = []
        self.rows = 0
        self.cols = 0

    def read_board(self, file):
        infile = open(file,"r")
        self.cols = int(infile.readline())+2
        self.rows = int(infile.readline())+2
        self.board = [[Wall("#") for i in range(self.rows)] for j in range(self.cols)]
        for i in range(self.cols-2):
            x = infile.readline()
            for j in range (self.rows-2):
                if x[j] == "." or "*":
                    cell = Conway(x[j])
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
            
def play_round_conway(self):
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
        while rounds > 0:
            self.play_round_conway()
            self.update_board()
            rounds -=1


    def update_board(self):
        for x in self.board:
            for f in x:
                if f.name == "dead":
                    if f.live_neighbors == 3:
                        f.name = "alive"
                        f.symbol ="*"

                elif f.name == "alive":
                    if f.live_neighbors != 2 or f.live_neighbors !=3:
                        # f.symbol = "*"
                        # f.name = "alive"
                    # else:
                        f.symbol = "."
                        f.name = "dead"


        

    def show_board(self):
        """
        shows board by printing each array in the 2d array
        on a new line, seperated by spaces
        """
        for s in self.board:
            print(' '.join(x.symbol for x in s))



game = Life()
game.read_board("RunLife.in.txt")
game.show_board()
game.run(1)
game.show_board()
