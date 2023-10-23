import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

  
def test_plot():
    size = 9
    starting_walls = 10

    v=np.random.randint(0,2,(size,size-1),'?')  
    h=np.random.randint(0,2,(size-1,size),'?')
    remaining_topwalls = starting_walls - np.random.randint(0,starting_walls)
    remaining_bottomwalls = starting_walls - np.random.randint(0,starting_walls)
    print(remaining_topwalls, remaining_bottomwalls)

    fig, (topwalls_ax, table_ax, bottomwalls_ax) = plt.subplots(3, 1, height_ratios=[2,size,2])
    #fig, table_ax = plt.subplots(1, 1)
    table_ax.set_xlim(.5,size+.5)
    table_ax.set_ylim(.5,size+.5)
    table_ax.set_xticks([_ for _ in range(1,size+1)], minor=False)
    table_ax.set_yticks([_ for _ in range(1,size+1)], minor=False)
    table_ax.set_xticks([_+.5 for _ in range(size)], minor=True)
    table_ax.set_yticks([_+.5 for _ in range(size)], minor=True)
    table_ax.set_xticklabels([ chr(ord('A')+_) for _ in range(size) ])
    table_ax.tick_params(axis='both', which='both', length=0)
    
    table_ax.spines[['left','bottom','right', 'top']].set_visible(False)
    topwalls_ax.spines[['left','bottom','right', 'top']].set_visible(False)
    bottomwalls_ax.spines[['left','bottom','right', 'top']].set_visible(False)
    topwalls_ax.tick_params(axis='both', which='both', length=0)
    bottomwalls_ax.tick_params(axis='both', which='both', length=0)

    for i,walls in enumerate(v):
        for j,wall in enumerate(walls):
            if wall:
                table_ax.plot([j+1.5,j+1.5],[i+.5,i+1.5],c='k',linewidth=2)
    for i,walls in enumerate(h):
        for j,wall in enumerate(walls):
            if wall:
                table_ax.plot([j+1.5,j+.5],[i+1.5,i+1.5],c='k',linewidth=2)

    table_ax.plot(int(size/2+.5),1,'b.',markersize=25)
    table_ax.plot(int(size/2+.5),size,'r.',markersize=25)
    table_ax.grid(linestyle=':', which='minor')  
    
    topwalls_ax.set_xticks([])
    topwalls_ax.set_yticks([])
    bottomwalls_ax.set_xticks([])
    bottomwalls_ax.set_yticks([])
    topwalls_ax.set_xlim(.5,starting_walls+.5)
    topwalls_ax.set_ylim(0,2)
    bottomwalls_ax.set_xlim(.5,starting_walls+.5)
    bottomwalls_ax.set_ylim(0,2)
    
    for i in range(remaining_topwalls):
        topwalls_ax.plot([starting_walls-i,starting_walls-i-.25],[0,2], c='#a80000', linewidth=2)
    for i in range(remaining_bottomwalls):
        bottomwalls_ax.plot([i+1,i+1.25],[0,2], c='#000070', linewidth=2)
    
    
    plt.show()
    return

def test_print():
    size=3
    v=np.random.randint(0,2,(size,size-1),'?')
    h=np.random.randint(0,2,(size-1,size),'?')
    print(v,v.shape,h,h.shape,sep='\n')

    # print inline table
    s='\n '+ size*'-'
    for i in range(size):
        for j in range(size-1,0,-1):
            new = '-' if v[i,j-1] else ' '
            s='\n'+new+s
    print(s)

if __name__ == "__main__":
    test_plot()