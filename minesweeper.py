import random
from termcolor import colored

class MineSweeper:
    def __init__(self):
        self.field = [[0 for _ in range(9)] for _ in range(9)]
        self.display = [[" " for _ in range(9)] for _ in range(9)]
        self.total_mines = 10
        self.cells_with_mines = 0 
        self.open_cells = 0
                 
    #Printing the field
    def print_field(self, x):
        print("  ", "-" * 21)
        for i in range(9):
            print(f"{i + 1} ","|", x[i][0], x[i][1], x[i][2], x[i][3], x[i][4], x[i][5], x[i][6], x[i][7], x[i][8], "|")
        print("  ", "-" * 21)
        print("    ", "1", "2", "3", "4", "5", "6", "7", "8", "9",)
     
    #Randomly placing the mines on the field
    def mines(self):
        i = 0
        while i < self.total_mines:
            row = random.randrange(9)
            column = random.randrange(9)
            if self.field[row][column] != 0:
                continue
            i += 1     
            self.field[row][column] = "*"
            self.cells_with_mines += 1
    
    #We need to calculate the number of mines around each cell     
    def numbers(self):
        self.mines()
        for row in range(9):
            for column in range(9):        
                for j in range(-1, 2):
                        for k in range(-1, 2):
                            if self.field[row][column] == "*":
                                if (row + j > -1 and row + j < 9) and (column + k > -1 and column + k < 9):
                                    if self.field[row + j][column + k] != "*":
                                        self.field[row + j][column + k] += 1
    
    #Giving colors to numbers                                  
    def colors(self):
        for row in range(9):
            for column in range(9):
                if self.field[row][column] == "*":
                    self.field[row][column] = colored("*", "black")
                if self.field[row][column] == 1:
                    self.field[row][column] = colored("1", "blue")
                if self.field[row][column] == 2:
                    self.field[row][column] = colored("2", "green")
                if self.field[row][column] == 3:
                    self.field[row][column] = colored("3", "light_red")
                if self.field[row][column] == 4:
                    self.field[row][column] = colored("4", "light_blue")
                if self.field[row][column] == 5:
                    self.field[row][column] = colored("5", "red")
                if self.field[row][column] == 6:
                    self.field[row][column] = colored("6", "cyan")
                if self.field[row][column] == 7:
                    self.field[row][column] = colored("7", "magenta")
                if self.field[row][column] == 8:
                    self.field[row][column] = colored("8", "dark_grey")
                
    #If the user selected cell equals to zero, this function opens other numbers that are connected to it
    def zero(self, row, column):
        if row < 0 or row > 8 or column < 0 or column > 8:
            return
        if self.display[row][column] == " ":
            self.display[row][column] = self.field[row][column]
            self.open_cells += 1
            if self.field[row][column] == 0:
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        self.zero(row + j, column + k)

    #Main game loop                              
    def play(self) :
        self.numbers()
        self.colors()
        while True:
            try:
                self.print_field(self.display)
                row = int(input("Enter a row to open: ")) - 1
                column = int(input("Enter a column to open: ")) - 1
                
                #Returning to the loop if user selects out of bounds
                if row < 0 or row > 8 or column < 0 or column > 8:
                    print("Invalid row/column.")
                    continue
                
                #Game ends in a loss if the user selects a mine
                if self.field[row][column] == colored("*", "black"):
                    self.print_field(self.field)
                    return print("Game over, you selected a mine!")
                
                #Returning to the loop if user tries to open a cell that's already opened
                if self.display[row][column] == self.field[row][column]:
                    print("You already opened that cell.")
                    continue

                #Opens the cell user types
                if self.field[row][column] == 0:    
                    self.zero(row, column)
                else:
                    self.display[row][column] = self.field[row][column]
                    self.open_cells += 1

                #Win condition
                if self.open_cells + self.cells_with_mines == 9 * 9:
                    self.print_field(self.field)
                    return print("Congratulations, you won!")
                
            except ValueError:
                print("Please enter integers only.")             

   
game = MineSweeper()
game.play()                                        