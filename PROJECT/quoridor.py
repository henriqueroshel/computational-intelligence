"""
https://dbdmg.polito.it/dbdmg_web/wp-content/uploads/2022/10/2-Python-Programming.pdf
https://dbdmg.polito.it/dbdmg_web/wp-content/uploads/2021/10/3-Python-Projects.pdf
"""

import numpy as np
import matplotlib.pyplot as plt

TABLE_SIZE = 9
START_WALLS = 10

class quoridor:
    
    def __init__(self, player0, player1, table):
        self.player0 = player(0)
        self.player1 = player(1)
        self.table = table()


class player:
    
    def __init__(self, player_num):
        self.player_num = player_num
        self.position = (int(TABLE_SIZE/2+.5), 1+player_num*(TABLE_SIZE-1))
        

class table:
    
    def __init__(self):
        # Arrays of boolean values to represent the wall between cells
        self.vwalls = np.zeros((9,8), '?')
        self.hwalls = np.zeros((8,9), '?')

    def __str__(self):
        s=''
        

    def show(self):
        for i,walls in enumerate(self.vwalls):
            for j,wall in enumerate(walls):
                if wall:
                    plt.plot([j+1,j+1],[i,i+1])
        for i,walls in enumerate(self.hwalls):
            for j,wall in enumerate(walls):
                if wall:
                    plt.plot([j+1,j],[i+1,i+1])
        plt.grid()
        plt.show()

if __name__ == "__main__":
    table().show()