# -*- coding: utf-8 -*-
# Bomberman in python

from os import system

import curses
import time
import sys

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print ""
     if a == 0:
          print "Command executed correctly"
     else:
          print "Command terminated with error"
     raw_input("Press enter")
     print ""

x = 0

while x != ord('4') and x != ord('q'):
     screen = curses.initscr()

     screen.clear()
     screen.border(0)
     #screen.box(0,0)
     screen.addstr(2, 2, "Ncurse-Python-Networked Bomberman 0.1")
     screen.addstr(4, 2, "Please enter a number...")
     screen.addstr(6, 4, "1 - Enter a server address")
     screen.addstr(7, 4, "2 - Launch a bomberman game ")
     screen.addstr(8, 4, "4 - Exit")
     screen.refresh()


     screen = curses.newwin(10,30,4,2)
     screen.box()

     x = screen.getch()

     if x == ord('1'):
          server_address = get_param("Enter a server name or ip address")
          curses.endwin()
     if x == ord('2'):
          # launch_game()
          curses.endwin()
     if x == ord('3'):
          curses.endwin()
          execute_cmd("df -h")

curses.endwin()

