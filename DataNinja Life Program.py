#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import Counter

def next_generation(world):
    "The set of live cells in the next generation."
    possible_cells = counts = neighbor_counts(world)
    return {cell for cell in possible_cells
            if (counts[cell] == 3) 
            or (counts[cell] == 2 and cell in world)}

def neighbor_counts(world):
    "A {cell: int} counter of the number of live neighbors for each cell that has neighbors."
    return Counter(nb for cell in world 
                      for nb in neighbors(cell))

def neighbors(cell):
    "All 8 adjacent neighbors of cell."
    (x, y) = cell
    return [(x-1, y-1), (x, y-1), (x+1, y-1), 
            (x-1, y),             (x+1, y), 
            (x-1, y+1), (x, y+1), (x+1, y+1)]


# In[3]:


#Creating world
world = {(3, 1), (1, 2), (1, 3), (2, 3)}
next_generation(world)


# In[4]:


next_generation(next_generation(world))


# In[5]:


neighbors((2, 4))


# In[6]:


neighbor_counts(world)


# In[7]:


#Creating world
def run(world, n):
    "Run the world for n generations. No display; just return the nth generation."
    for g in range(n):
        world = next_generation(world)
    return world


# In[8]:


run(world, 100)


# In[9]:


#Displaying each generation
import time
from IPython.display import clear_output, display_html

LIVE  = '@'
EMPTY = '.'
PAD   = ' '

def display_run(world, n=10, Xs=range(10), Ys=range(10), pause=0.1):
    "Step and display the world for the given number of generations."
    for g in range(n + 1):
        clear_output()
        display_html('Generation {}, Population {}\n{}'
                     .format(g, len(world), pre(picture(world, Xs, Ys))), 
                     raw=True)
        time.sleep(pause)
        world = next_generation(world)
        
def pre(text): return '<pre>' + text + '</pre>'
        
def picture(world, Xs, Ys):
    "Return a picture: a grid of characters representing the cells in this window."
    def row(y): return PAD.join(LIVE if (x, y) in world else EMPTY for x in Xs)
    return '\n'.join(row(y) for y in Ys)


# In[10]:


print(picture(world, range(5), range(5)))


# In[11]:


display_run(world, 10, range(5), range(5))


# In[12]:


#Interesting worlds exploration
def shape(picture, offset=(3, 3)):
    "Convert a graphical picture (e.g. '@ @ .\n. @@') into a world (set of cells)."
    cells = {(x, y) 
             for (y, row) in enumerate(picture.splitlines())
             for (x, c) in enumerate(row.replace(PAD, ''))
             if c == LIVE}
    return move(cells, offset)

def move(cells, offset):
    "Move/Translate/slide a set of cells by a (dx, dy) displacement/offset."
    (dx, dy) = offset
    return {(x+dx, y+dy) for (x, y) in cells}

blinker     = shape("@@@")
block       = shape("@@\n@@")
beacon      = block | move(block, (2, 2))
toad        = shape(".@@@\n@@@.")
glider      = shape(".@.\n..@\n@@@")
rpentomino  = shape(".@@\n@@.\n.@.", (36, 20))
line        = shape(".@@@@@@@@.@@@@@...@@@......@@@@@@@.@@@@@", (10, 10))
growth      = shape("@@@.@\n@\n...@@\n.@@.@\n@.@.@", (10, 10))


# In[13]:


shape("""@ @ .
         . @ @""")


# In[14]:


block


# In[15]:


move(block, (100, 200))


# In[16]:


display_run(blinker)


# In[17]:


display_run(beacon)


# In[18]:


display_run(toad)


# In[19]:


display_run(glider, 15)


# In[20]:


display_run(rpentomino, 130, range(55), range(40))


# In[21]:


zoo = (move(blinker, (5, 25)) | move(glider, (8, 13)) | move(blinker, (20, 25))  |
       move(beacon, (24, 25)) | move(toad, (30, 25))  | move(block, (13, 25)) | move(block, (17, 33)))

display_run(zoo, 160, range(50), range(40))


# In[22]:


display_run(growth, 100, range(40), range(40))


# In[ ]:




