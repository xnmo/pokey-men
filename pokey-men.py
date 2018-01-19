import curses
import random

#simple character information
poke_a_name = 'Character'
poke_a_hp_max = 10
poke_a_mp_max = 8
poke_a_hp_current = 10
poke_a_mp_current = 8

poke_b_name = 'Enemy'
poke_b_hp_max = 10
poke_b_mp_max = 8
poke_b_hp_current = 10
poke_b_mp_current = 8


try:
    #makes a big screen the size of the terminal
    stdscr = curses.initscr()
    #doesn't let you type on the screen
    curses.noecho()
    #allows the terminal to parse each key without a CR
    curses.cbreak()
    #allows the use of special keys
    stdscr.keypad(1)

    while True:
        #prints character info
        stdscr.addstr(0,0,'  YOU: ' + poke_a_name)
        stdscr.addstr(1,0,'   HP: ' + str(poke_a_hp_current) + '/' + str(poke_a_hp_max))
        stdscr.addstr(2,0,'   MP: ' + str(poke_a_mp_current) + '/' + str(poke_a_mp_max))
        stdscr.addstr(4,0,'ENEMY: '+ poke_b_name)
        stdscr.addstr(5,0,'   HP: ' + str(poke_b_hp_current) + '/' + str(poke_b_hp_max))
        stdscr.addstr(7,0,'ROCK(1), PAPER,(2), SCISSORS(3), MAGIC(4)')

        #prints screen and gets input
        stdscr.refresh()
        rps_a_ch = stdscr.getch()
        if rps_a_ch == 49:
            rps_a = 1
        elif rps_a_ch == 50:
            rps_a = 2
        elif rps_a_ch == 51:
            rps_a = 3
        elif rps_a_ch == 52:
            rps_a = 4
        #enemy rps
        rps_b = random.randint(1,3)
        stdscr.addstr(8,0,str(rps_a) + ',' + str(rps_b))
        
        #rps logic
        if rps_a == 1 and rps_b == 3:
            poke_b_hp_current -= 2
        elif rps_a == 1 and rps_b == 2:
            poke_a_hp_current -= 1
        elif rps_a == 2 and rps_b == 1:
            poke_b_hp_current -= 2
        elif rps_a == 2 and rps_b == 3:
            poke_a_hp_current -= 1
        elif rps_a == 3 and rps_b == 2:
            poke_b_hp_current -= 2
        elif rps_a == 3 and rps_b == 1:
            poke_a_hp_current -= 1
        elif rps_a == 4 and poke_a_mp_current >= 4:
            poke_b_hp_current -= 4
            poke_a_mp_current -= 4
        #waits for user input before clearing the screen
        stdscr.getch()
        stdscr.clear()
except:
    curses.endwin()



