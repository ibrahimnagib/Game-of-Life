# Life

class AbstractCell:
    def __init__(self, symbol):
        #self.name 
        self.symbol = symbol
        self.live_neighbors = 0

class ConwayCell(AbstractCell):
   def __init__(self, symbol):
       AbstractCell.__init__(self, symbol)
       self.name = "conway"
       if symbol == "*":
          self.status = 1
       elif symbol == ".":
          self.status = 0

class FredkinCell(AbstractCell):
   def __init__(self, symbol):
       AbstractCell.__init__(self,symbol)
       self.name = "fredkin"
       # self.status = 1
       if symbol == "-":
          self.status = 0
          self.age = 0
       elif symbol == "+":
          self.age = 11
          self.status = 1
       else:
          self.status = 1
          self.age = int(symbol)

       self.live_neighbors = 0


class WallCell(AbstractCell):
   def __init__(self, symbol):
       AbstractCell.__init__(self, symbol)
       self.name = "wall"
       #self.name = "wall"
       self.live_neighbors = 0
       self.status = 0


class Life:
    def __init__(self,textfile):
        self.board = []
        self.rows = 0
        self.cols = 0
        self.population = 0
        self.infile = open(textfile,"r")

    def read_board(self):
        # infile = open(file,"r")
        self.population = 0
        self.cols = int(self.infile.readline())+2
        self.rows = int(self.infile.readline())+2
        self.board = [[WallCell("#") for i in range(self.rows)] for j in range(self.cols)]
        for i in range(self.cols-2):
            x = self.infile.readline()
            for j in range (self.rows-2):
                if x[j] == "." :
                    cell = ConwayCell(x[j])
                elif x[j] == "*":
                    cell = ConwayCell(x[j])
                    self.population += 1
                else:
                    cell = FredkinCell(x[j])
                self.board[i+1][j+1] = cell
        self.infile.readline()       
        print("Generation = 0 ", "Population = ",self.population)
        self.show_board()


    def play_round_FredkinCell(self):
      """
      Play...
      """
      # i = 0
      # j = 0

      # for x in self.boards:
      #     for f in x:
      #         j += 1
      #         if f.status == 1:
      #             for m in range(i-1,i+1):
      #                 for n in range(j-1,j+1):
      #                     self.board[m][n].live_neighbors += 1
      #     i += 1
      for x in self.board:
        for f in x:
          f.live_neighbors = 0
      self.population = 0
      for i in range(1, self.cols - 1):
           for j in range(1, self.rows - 1):
               status = self.board[i][j].status
               self.population += status

      self.board[i][j].live_neighbors -= status

    def play_round_ConwayCell(self):
       """
       Play...
       """
       #self.population = 0
       for x in self.board:
           for f in x:
               f.live_neighbors = 0
       #self.population = 0
       for i in range(1, self.cols - 1):
           for j in range(1, self.rows - 1):
               status = self.board[i][j].status
               #self.population += status
               for m in range(i - 1, i + 2):
                   for n in range(j - 1, j + 2):
                       self.board[m][n].live_neighbors += status
               self.board[i][j].live_neighbors -= status

    def run(self, rounds, shown):
        # gen = 0
        # print("Generation = ", gen, "Population = ",self.population)
        # self.show_board()
        gen = 1
        while rounds > 0:
            self.population = 0
            self.play_round_ConwayCell()
            self.update_board()
            # if gen == 1:
            #   self.update_board()
            #print
            if gen % shown == 0:
              print("Generation = ",gen , "Population = ", self.population)
              self.show_board()
              print
            rounds -=1
            gen += 1

    def runF(self, rounds, shown):
        gen = 0
        print("Generation = ", gen, "Population = ",self.population)
        self.show_board()
        gen += 1
        while rounds > 0:
            self.play_round_FredkinCell()
            self.update_board()
            print
            if gen % shown == 0:
              print("Generation = ",gen , "Population = ", self.population)
              self.show_board()
            rounds -=1
            gen += 1



    def update_board(self):
        #self.population = 0
        for x in self.board:
            for f in x:
                if f.status == 0:
                    if f.name == "conway":
                        if f.live_neighbors == 3:
                            #f.name = "alive"
                            f.symbol ="*"
                            f.status = 1
                            self.population += 1
                    elif f.name == "fredkin":
                        if f.live_neighbors == 0 or f.live_neighbors == 2 or f.live_neighbors == 4:
                            f.status =1
                            f.age += 1
                            self.population += 1
                    else:
                        f.status = 0


                elif f.status == 1:
                    #self.population += 1
                    if f.name == "conway":
                        if not((f.live_neighbors == 2 or f.live_neighbors == 3)):
                        # f.symbol = "*"
                        # f.name = "alive"
                        # else:
                            f.symbol = "."
                            #f.name = "dead"
                            f.status = 0
                            #self.population += 1
                        else:
                          self.population += 1

                    elif f.name == "fredkin":
                        if f.live_neighbors == 1 or f.live_neighbors == 3:
                            f.age += 1
                            f.status = 1
                            self.population += 1



        

    def show_board(self):
        """
        shows board by printing each array in the 2d array
        on a new line, seperated by spaces
        """

        # for s in self.board:
        #     print(' '.join(str(x.live_neighbors) for x in s))
            
        for s in self.board[1:-1]:
            print(' '.join(x.symbol for x in s[1:-1]))




