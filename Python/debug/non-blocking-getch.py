#!/usr/bin/python

import curses
import select
import sys

timeout = 100

stdscr = curses.initscr()
curses.cbreak()
keyboard_fd = sys.stdin.fileno()
select_input_list = [keyboard_fd]
k = 15
try:
    stdscr.addch(10,5,"X")
    stdscr.refresh()
     
    while True:
        (i,o,x) = select.select(select_input_list, [], [], .5)        
        if not i:
            stdscr.addstr(15, k, "pas d'appui sur le clavier")
            k = k+1
            stdscr.refresh()
        if keyboard_fd in i:
            key = stdscr.getch()
#        if key == -1:
#            (i, o, s) = select.select([], [], [], timeout)

        
            if key == ord("q"):
                break

            if key == curses.KEY_UP:
                stdscr.addstr(11,5,"KEY_UP")
                screen.refresh()
            if key == curses.KEY_DOWN:
                stdscr.addstr(11,5,"KEY_DOWN")
            if key == curses.KEY_RIGHT:
                stdscr.addstr(11,5,"KEY_RIGHT")
            if key == curses.KEY_LEFT:
                stdscr.addstr(11,5,"KEY_LEFT")
            
            stdscr.addch(20,25,key)
            stdscr.refresh()
    
    

finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
  
