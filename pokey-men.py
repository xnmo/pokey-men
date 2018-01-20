import curses
import random
import traceback

#simple character information
poke_a_label = 'YOU'
poke_a_name = 'POKEY-MAN'
poke_a_hp_max = 10
poke_a_mp_max = 8
poke_a_hp = 10
poke_a_mp = 8

poke_b_label = 'ENEMY'
poke_b_name = 'BADDY-MAN'
poke_b_hp_max = 10
poke_b_mp_max = 8
poke_b_hp = 10
poke_b_mp = 8

poke_a_moveset = ['HIT','BITE','STAB','POKE']


def DrawStats(y,x, label, name, hp, hp_max, mp, mp_max):
    stdscr.addstr(y+0,x, label + ': ' + name)
    stdscr.addstr(y+1,x,'HP: ' + str(hp) + '/' + str(hp_max))
    stdscr.addstr(y+2,x,'MP: ' + str(mp) + '/' + str(mp_max))

def DrawEndBattle(y,x,name):
    stdscr.addstr(y,x, 'You have defeated ' + name)
    
def ConvertNum(c_ch):
    if c_ch == 49:
        return 1
    elif c_ch == 50:
        return 2
    elif c_ch == 51:
        return 3
    elif c_ch == 52:
        return 4

def DrawMenuOne(y,x):
    stdscr.addstr(y,x,  '(1)FIGHT     (2)MEN')
    stdscr.addstr(y+1,x,'(3)RUN       (4)INVENTORY')

def DrawFightMenu(y,x,poke_moveset):
    stdscr.addstr(y,x, '(1)' + poke_moveset[0])
    stdscr.addstr(y,x+13, '(2)' + poke_moveset[1])
    stdscr.addstr(y+1,x, '(3)' + poke_moveset[2])
    stdscr.addstr(y+1,x+13, '(4)' + poke_moveset[3])
try:
    #makes a big screen the size of the terminal
    stdscr = curses.initscr()
    #doesn't let you type on the screen
    curses.noecho()
    #allows the terminal to parse each key without a CR
    curses.cbreak()
    #allows the use of special keys
    stdscr.keypad(1)

    while poke_b_hp > 0:
        #prints character info
        DrawStats(0,0, poke_a_label, poke_a_name, poke_a_hp, poke_a_hp_max, poke_a_mp, poke_a_mp_max)
        DrawStats(4,0, poke_b_label, poke_b_name, poke_b_hp, poke_b_hp_max, poke_b_mp, poke_b_mp_max)
        DrawMenuOne(8,0)

        #prints screen and gets input
        stdscr.refresh()

        
        menu_choice_1 = ConvertNum(stdscr.getch())
        if menu_choice_1 == 1:
            stdscr.move(8,0)
            stdscr.clrtobot()
            DrawFightMenu(8,0,poke_a_moveset)
            stdscr.refresh()

        
        #waits for user input before clearing the screen
        stdscr.getch()
        stdscr.clear()

    stdscr.clear()
    DrawEndBattle(0,0,poke_b_name)
    stdscr.refresh()
    stdscr.getch()
    curses.endwin()
except:
    curses.endwin()
    print(traceback.format_exc())



