#!/usr/bin/python
from enum import Enum
from random import randint


class Player(Enum):
    PlayerOne = 1
    PlayerTwo = 2

class Game:
    'Common base class for all game'
    grid = []
    player = Player.PlayerOne
    ScorePlayerOne = 0
    ScorePlayerTwo = 0

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def init_grid(self):
        for row in range(self.row):
            # Appen a blank list to each row cell
            self.grid.append([])
            # print('> Row ', row, " grid content ", self.grid)
            for column in range(self.column):
                # Assign x to each row
                self.grid[row].append('*')
                # print('> Column ', column, " grid content ", self.grid)

    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))

    def start(self):
        self.init_grid()
        self.print_grid()
        print("> Game of square : Human vs AI")
        while not self.is_grid_full():
            self.human(Player.PlayerOne)
            # self.robot(Player.PlayerTwo)

        print("> You played in row ", row, " and column ", column)
        self.update_grid(row, column)

    def is_position_correct(self, x, y):
        print("Typing point status")
        grid_len = self.grid.__len__()
        if x > grid_len or x < 1 or y > grid_len or y < 1:
            return False
        if self.grid[x][y] == "*":
            return True
        return False

    def is_grid_full(self):
        for item in self.grid:
            for value in item:
                if value == "*":
                    return  False
        return True

    def player_scored(self, player, x, y):
        grid_len = self.grid.__len__() - 1

        if (x == 0 and y == 0) or (x == 0 and y == grid_len) or (x == grid_len and y == 0)  or (x == grid_len and y == grid_len):
            self.on_coner_treatment(player, x, y, grid_len)

        elif x == 0 or y == 0 or x == grid_len or y == grid_len:
            self.on_edge_treatment(player, x, y, grid_len)

        else :
            print("Is not on edge")
            self.in_grid_treatment(player, x, y)

    def on_edge_tretament(self, player, x, y, grid_len):
        scored = False;
        if x == 0 :
            print("Is on top edge")
            if self.grid[x + 1][y] == "x" and self.grid[x + 1][y + 1] == "x" and self.grid[x][y + 1] == "x":
                scored = self.point_to(player)
            if self.grid[x + 1][y - 1] == "x" and self.grid[x + 1][y] == "x" and self.grid[x][y - 1] == "x":
                scored = self.point_to(player)

        elif y == 0 :
            print("Is on left edge")
            if self.grid[x + 1][y] == "x" and self.grid[x + 1][y + 1] == "x" and self.grid[x][y + 1] == "x":
                scored = self.point_to(player)
            if self.grid[x - 1][y] == "x" and self.grid[x - 1][y + 1] == "x" and self.grid[x][y + 1] == "x":
                scored = self.point_to(player)

        elif x == grid_len :
            print("Is on bottom edge")
            if self.grid[x - 1][y] == "x" and self.grid[x - 1][y + 1] == "x" and self.grid[x][y + 1] == "x":
                scored = self.point_to(player)
            if self.grid[x - 1][y] == "x" and self.grid[x - 1][y - 1] == "x" and self.grid[x][y - 1] == "x":
                scored = self.point_to(player)

        #elif y == grid_len :
        else:
            print("Is right edge")
            if self.grid[x - 1][y] == "x" and self.grid[x - 1][y - 1] == "x" and self.grid[x][y - 1] == "x":
                scored = self.point_to(player)
            if self.grid[x + 1][y - 1] == "x" and self.grid[x + 1][y] == "x" and self.grid[x][y - 1] == "x":
                scored = self.point_to(player)
        return scored

    def in_grid_treatment(self, player, x, y):
        scored = False
        if self.grid[x+1][y] == "x" and self.grid[x+1][y+1] == "x" and self.grid[x][y+1] == "x":
            scored = self.point_to(player)
        if self.grid[x-1][y] != "*" and self.grid[x-1][y+1] != "*" and self.grid[x][y+1] != "*":
            scored = self.point_to(player)
        if self.grid[x-1][y] != "*" and self.grid[x-1][y-1] != "*" and self.grid[x][y-1] != "*":
            scored = self.point_to(player)
        if self.grid[x+1][y-1] != "*" and self.grid[x+1][y] != "*" and self.grid[x][y-1] != "*":
            scored = self.point_to(player)
        return scored

    def on_coner_treatment(self,player, x, y, grid_len):
        print("> Is on the corner fired")
        scored = False
        if x == 0 and y == 0:
            print("Is on top left corner")
            if self.grid[x + 1][y] == "x" and self.grid[x + 1][y + 1] == "x" and self.grid[x][y + 1] == "x":
                scored = self.point_to(player)

        if x == 0 and y == grid_len:
            print("Is on top right corner")
            if self.grid[x][y-1] == "x" and self.grid[x + 1][y] == "x" and self.grid[ x+1 ][y - 1] == "x":
                scored = self.point_to(player)

        if x == grid_len and y == 0:
            print("Is on bottom left corner")
            if self.grid[x][y+1] == "x" and self.grid[x - 1][y] == "x" and self.grid[ x-1 ][y + 1] == "x":
                scored = self.point_to(player)

        if x == grid_len and y == grid_len:
            print("Is on bottom right corner")
            if self.grid[x-1][y] == "x" and self.grid[x - 1][y - 1] == "x" and self.grid[x][y - 1] == "x":
                scored = self.point_to(player)
        return scored

    def point_to(self, player):
        if player == Player.PlayerOne:
            self.ScorePlayerOne += 1
        else:
            self.ScorePlayerTwo += 1
        return True;

    def human(self, player):
        print('> It''s Human turn to play')
        row = int(input("> Chose a row to play : "))
        column = int(input("> Chose a column to play: "))
        if not self.is_position_correct(row, column):
            self.human(player)
        else:
            self.update_grid(row, column)
            self.player_scored(player, row, column)

    def robot(self):
        print("robot function")

    def update_grid(self, row, column):
        print("> Log : update grid function", row, " ", column)
        for r in range(0, self.grid.__len__()):
            print("row ", r)
            for c in range(0, self.grid[r].__len__()):
                print("c and r value : ", c, " ", r)
                if r == row and c == column:
                    self.grid[row-1][column-1] = "x"
                    print("> case updated : ", self.grid[row][column])
        self.print_grid()

    # Max min algorithm
    def max_min(self, array, n, k):
        array = sorted(array)
        return min(array[a + k - 1] - array[a] for a in range(n - k + 1))

"This would create first object of Game class"
print("> Choose your grid size by typing row and column number.")
row = int(input("> Row : "))
column = int(input("> Column : "))
game = Game(row, column)
"This would start game"
game.start()
