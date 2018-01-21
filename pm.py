import curses
import random
import traceback

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(1)

def IsWalkable(y,x):
    return map_list[y][x]['walkable']

tile_types = [{'tile':'.', 'walkable':True}, {'tile':'#', 'walkable':False}]
map_list = []
map_file = open('pmap.txt','rb')
# loop through each line of the file
for line in map_file:
    row = []
    #loop through each character in the line
    for char in line:
        #loop through list of tiles
        for tile in tile_types:
            if tile['tile'] == char:
                row.append(tile)
                break
    map_list.append(row)

y = 0
x = 0
player_y = 1
player_x = 2
try:
    while True:
        stdscr.move(y,x)
        for row in map_list:
            for tile in row:
                stdscr.addstr(tile['tile'])
            y+=1
            stdscr.move(y,x)
        stdscr.addstr(player_y,player_x, '@')
        player_input = stdscr.getch()
        y = 0
        x = 0
        #104-108
        row = map_list[player_y]
        tile = row[player_x]
        if player_input == 104 and IsWalkable(player_y,player_x-1):
            player_x -= 1
        elif player_input == 106 and IsWalkable(player_y+1,player_x):
            player_y += 1
        elif player_input == 107 and IsWalkable(player_y-1,player_x):
            player_y -= 1
        elif player_input == 108 and IsWalkable(player_y,player_x+1):
            player_x += 1

        
except:
    curses.endwin()
    print(traceback.format_exc())
finally:
    curses.endwin()

