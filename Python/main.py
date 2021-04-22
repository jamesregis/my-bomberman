# -*- coding: utf-8 -*-
# Bomberman in python

import curses
import time
import select
import sys
import termios

import common 


# class Map


#class Bomb(x, y):
#    def __init__(self):
#        self.x = x
#        self.y = y
#        
#    timeout = 5
#    b_range = 2
#    def explode():
#        if self.timeout == 0:
#            pass


def load_map():
    x = 0
    common.g_map = [[0 for col in range(common.MAP_YSIZE)] for row in range(common.MAP_XSIZE)]
    f = open('map.txt','r')
    for line in f:
        for y in range(0, common.MAP_YSIZE):
            if line[y] == ':':
                common.g_map[x][y] = common.MAP_WALL
            elif line[y] == '#':
                common.g_map[x][y] = common.MAP_STONE
            elif line[y] == 'Z':
                common.g_map[x][y] = common.MAP_PLAYER_1
            elif line[y] == ' ':
                common.g_map[x][y] = common.MAP_EMPTY
        x = x + 1



def draw_map(screen): 
    for x in range(0, common.MAP_XSIZE):
        for y in range(0, common.MAP_YSIZE):
            if common.g_map[x][y] == common.MAP_WALL :
                if curses.has_colors():
                    screen.attrset(curses.color_pair(1))
                    screen.addstr(x, y, common.CHR_WALL)
            if common.g_map[x][y] == common.MAP_STONE:
                if curses.has_colors():
                    screen.attrset(curses.color_pair(2))
                    screen.addstr(x, y, common.CHR_STONE)
            if common.g_map[x][y] == common.MAP_PLAYER_1:
                screen.attrset(curses.color_pair(1))
                screen.addstr(x, y, common.CHR_PLAYER_1)
            if common.g_map[x][y] == common.MAP_EMPTY:
                screen.addstr(x, y, common.CHR_EMPTY)

#                screen.move(x+1, y+1)
#                screen.addstr(x, y, common.CHR_WALL, curses.COLOR_BLUE)

#    screen.addstr(10, 5,"::", curses.COLOR_BLUE)
#    screen.addstr(11, 6,"@@@@@@", curses.COLOR_RED)
#    screen.addstr(5, 5, "--", curses.COLOR_BLUE)
#    screen.addstr(0, 0, "#", curses.COLOR_BLUE)

#def get_single_input():
#    ch = sys.stdin.read(1)
#    return ch


#def initialize_termios():
#    common.fd = sys.stdin.fileno()
#    common.old_settings = termios.tcgetattr(common.fd)
#    common.new_settings = termios.tcgetattr(common.fd)
#    common.new_settings[3] = common.new_settings[3] & ~termios.ICANON
#    termios.tcsetattr(common.fd, termios.TCSADRAIN, common.new_settings)
#    #tty.setraw(sys.stdin.fileno())
#
#def deinitialize_termios():
#    termios.tcsetattr(common.fd, termios.TCSADRAIN, common.old_settings) 


def update_map(screen):
    for x in range(0, common.MAP_XSIZE):
        for y in range(0, common.MAP_YSIZE):
            if common.g_map[x][y] == common.MAP_WALL :
                if curses.has_colors():
                    screen.attrset(curses.color_pair(1))
                    screen.addstr(x, y, common.CHR_WALL)
            
            if common.g_map[x][y] == common.MAP_STONE:
                if curses.has_colors():
                    screen.attrset(curses.color_pair(2))
                    screen.addstr(x, y, common.CHR_STONE)
            
            if common.g_map[x][y] == common.MAP_PLAYER_1:
               screen.attrset(curses.color_pair(1))
               screen.addstr(x, y, common.CHR_PLAYER_1)
            
            if common.g_map[x][y] == common.MAP_EMPTY:
                screen.addstr(x, y, common.CHR_EMPTY)

            if common.g_map[x][y] == common.MAP_BOMB:
                if curses.has_colors():
                    screen.attrset(curses.color_pair(3))
                    screen.addstr(x, y, common.CHR_BOMB)

def explode_bomb(screen, x0, y0, blowout_range):
    for r in range(0, blowout_range):
        if curses.has_colors():
            screen.attrset(curses.color_pair(4))
            if ((x0 + r) < common.MAP_XSIZE):
                if (common.g_map[x0 + r][y0] != common.MAP_WALL):
                    common.g_map[x0 + r][y0] = common.MAP_EXPLOSION
                    screen.addstr(x0 + r, y0, common.CHR_EXPLOSION)

            if common.g_map[x0 - r][y0] != common.MAP_WALL:
                common.g_map[x0 - r][y0] = common.MAP_EXPLOSION
                screen.addstr(x0 - r, y0, common.CHR_EXPLOSION)
               
            if common.g_map[x0][y0 + r] != common.MAP_WALL:
                screen.addstr(x0, y0 + r, common.CHR_EXPLOSION)
                common.g_map[x0][y0 + r] = common.MAP_EXPLOSION
           
            if common.g_map[x0][y0 - r] != common.MAP_WALL:
                common.g_map[x0][y0 - r] = common.MAP_EXPLOSION
                screen.addstr(x0, y0 - r, common.CHR_EXPLOSION)

            # TODO : update common.g_map
            # Update explosion if there is a wall because now the explosion cross the wall and explode in the other side
            screen.refresh()

def clean_bomb(screen, x0, y0, blowout_range):
    for r in range(0, blowout_range):
        if common.g_map[x0 + r][y0] != common.MAP_WALL:
            common.g_map[x0 + r][y0] = common.MAP_EMPTY
            screen.addstr(x0 + r, y0, common.CHR_EMPTY) 

        if common.g_map[x0 - r][y0] != common.MAP_WALL:
            common.g_map[x0 - r][y0] = common.MAP_EMPTY
            screen.addstr(x0 - r, y0, common.CHR_EMPTY)
        
        if common.g_map[x0][y0 + r] != common.MAP_WALL:
            common.g_map[x0][y0 + r] = common.MAP_EMPTY
            screen.addstr(x0, y0 + r, common.CHR_EMPTY)
        
        if common.g_map[x0][y0 - r] != common.MAP_WALL:
            common.g_map[x0][y0 - r] = common.MAP_EMPTY
            screen.addstr(x0, y0 - r, common.CHR_EMPTY)
        # TODO Update common.g_map
        screen.refresh()
          
def bomb_processing(screen, blowout_range, countdown, blow_duration):
    for bomb in common.g_bombs:
        if (time.time() - bomb[3] >= countdown) & (bomb[2] == "armed"): # the bomb is armed and the countdown is reached
            explode_bomb(screen, bomb[0], bomb[1], blowout_range)
            bomb[2] = "explosed"
            bomb[3] = time.time()
        if (time.time() - bomb[3] >= blow_duration) & (bomb[2] == "explosed"): # call clean_bomb when the bomb explosed
            clean_bomb(screen, bomb[0], bomb[1], blowout_range)
            #bomb[2] = "cleaned" # hack to test removing bomb
            common.g_bombs.remove(bomb)
            # remove bomb from bomb the bomb list
        #if bomb[2] == "cleaned":
        #    common.g_bombs.pop(int(bomb))

def msgbox(screen, message):
    pass

def user_processing(screen, usertab):
#    if 
    
    pass


def main(screen):
#    screen = curses.initscr()
#    curses.curs_set(0)
#    curses.start_color()

    if curses.has_colors():
        bg = curses.COLOR_BLACK
        curses.init_pair(1, curses.COLOR_CYAN, bg)
        curses.init_pair(2, curses.COLOR_YELLOW, bg)
        curses.init_pair(3, curses.COLOR_RED, bg)
        curses.init_pair(4, curses.COLOR_WHITE, bg)
        curses.init_pair(5, curses.COLOR_GREEN, bg)


    load_map()
    draw_map(screen)
    screen.refresh()

    # size of one step
    step = 1
    g_bomb = []

    # Initialisaion pour le player 1
    p_x = 1
    p_y = 2
    
    screen.move(p_x, p_y)
    screen.addstr(p_x, p_y, common.CHR_PLAYER_1)

    # screen.nodelay(1)

#    initialize_termios()
    blowout_range = 3
    bomb_countdown = 2
    blow_duration = 1
    keyboard_fd = sys.stdin.fileno()
    player_id = 1

    select_input_list = [keyboard_fd]
    k = 0
    timeout = 0.01
    while True:

        (inputready,outputready,exceptready) = select.select(select_input_list, [], [], timeout)

        if not inputready:
            screen.addstr(common.MAP_XSIZE + 2, 3, str(k)) # add debug information
            bomb_processing(screen, blowout_range, bomb_countdown, blow_duration)
            #update_map
            user_processing(screen, common.g_users)
            screen.refresh()
            k = k+1

        if keyboard_fd in inputready:
            #char = get_single_input()       
            ch = screen.getch()

            old_p_x = p_x
            old_p_y = p_y
           
            if common.g_map[p_x][p_y] != common.MAP_BOMB:
                common.g_map[p_x][p_y] = common.MAP_EMPTY

            if ch == ord('q'):
                break
        
            if ch == curses.KEY_RIGHT:
                p_y = p_y + step
            if ch == curses.KEY_LEFT:
                p_y = p_y - step
            if ch == curses.KEY_UP:
                p_x = p_x - step
            if ch == curses.KEY_DOWN:
                p_x = p_x + step

            if common.g_map[p_x][p_y] == common.MAP_WALL:
                p_x = old_p_x
                p_y = old_p_y

            if common.g_map[p_x][p_y] == common.MAP_STONE:
                p_x = old_p_x
                p_y = old_p_y

            if common.g_map[p_x][p_y] == common.MAP_BOMB:
                #common.g_map = common.MAP_BOMB
                p_x = old_p_x
                p_y = old_p_y

            if ch == ord(' '): # espace is pressed to drop a bomb
                common.g_map[p_x][p_y] = common.MAP_BOMB
                common.g_bombs.append([p_x, p_y, "armed", time.time()])


            if common.g_map[p_x][p_y] == common.MAP_EMPTY:
                common.g_map[p_x][p_y] = common.MAP_PLAYER_1

            update_map(screen)
            

#            if common.g_map[p_x][p_y] == common.MAP_EMPTY:
#                common.map
#                screen.attrset(curses.color_pair(5))
#                screen.move(p_x, p_y + step)
#                p_y = y + step
#                screen.addstr(p_x, p_y, common.CHR_PLAYER_1)
#                screen.refresh()
##            common.g_map[p_x][p_y] = common.MAP_PLAYER
#            if ch == curses.KEY_UP:
#                screen.move(p_x - step, p_y)
#                p_x = x - step
##            common.g_map[p_x][p_y] = common.MAP_PLAYER
#                screen.attrset(curses.color_pair(5))
#                screen.addstr(p_x, p_y, common.CHR_PLAYER_1)
#            if ch == curses.KEY_DOWN:
#                screen.move(p_x + step, p_y)
#                p_x = x + step
##            common.g_map[p_x][p_y] = common.MAP_PLAYER
#                screen.attrset(curses.color_pair(5))
#                screen.addstr(p_x, p_y, common.CHR_PLAYER_1)
#    #screen.refresh()
#            if ch == curses.KEY_LEFT:
#                common.g_map[p_x][p_y] = common.MAP_EMPTY
#                screen.move(p_x, p_y - step)
#                p_y = p_y - step
#                common.g_map[p_x][p_y] = common.MAP_PLAYER_1
#                screen.attrset(curses.color_pair(5))
#                screen.addstr(p_x, p_y + step, common.CHR_PLAYER_1)
#                update_map(screen)
#
#    deinitialize_termios()
    
    screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

if __name__ == "__main__":
#    curses.wrapper(main)

    screen = curses.initscr()
    curses.start_color()

#    if curses.has_colors():
#        bg = curses.COLOR_BLACK
#        curses.init_pair(1, curses.COLOR_BLUE, bg)
#        curses.init_pair(2, curses.COLOR_CYAN, bg)

    curses.noecho()
    curses.cbreak()
    screen.keypad(1)
    
    main(screen)
#    main()
    screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
