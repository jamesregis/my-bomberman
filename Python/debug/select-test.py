#!/usr/bin/python

import sys
import termios
import curses
import select

import common

def get_single_input():
    tab = []
    ch = sys.stdin.read(1)
    if ord(ch) == 27:
        tab.append(ord(ch))            
        ch = sys.stdin.read(1)
        if ch == '[':
            tab.append(ord(ch))
            ch = sys.stdin.read(1)
            tab.append(ord(ch))
            #print "TABLEAU : ", tab
            return tab
        #elif  ord(ch) == 32 :
    return ch

def initialize_termios():
    common.fd = sys.stdin.fileno()
    common.old_settings = termios.tcgetattr(common.fd)
    common.new_settings = termios.tcgetattr(common.fd)
    common.new_settings[3] = common.new_settings[3] & ~termios.ECHO #~termios.ICANON
    termios.tcsetattr(common.fd, termios.TCSADRAIN, common.new_settings)
    #tty.setraw(sys.stdin.fileno())


def deinitialize_termios():
    termios.tcsetattr(common.fd, termios.TCSADRAIN, common.old_settings)

keyboard_fd = sys.stdin.fileno()
select_input_list = [keyboard_fd]

initialize_termios()
while True:
    
    (i,o,x) = select.select(select_input_list, [], [], .5)

    if not i:
        print "Dans la boucle"

    if keyboard_fd in i:
        ch = get_single_input()

        if type(ch) == str:
            if ord(ch) == ord("q"):
                print ord(ch)
                break
            if ord(ch) == ord(" "):
                print "Touche ESPACE"


        if type(ch) == list:
            if ch == common.KEY_UP:
                print "You pressed KEY_UP"
            if ch == common.KEY_LEFT:
                print "You pressed KEY_LEFT"
            if ch == common.KEY_DOWN:
                print "You pressed KEY_DOWN"
            if ch == common.KEY_RIGHT:
                print "You pressed KEY_RIGHT"
    
    #termios.tcsetattr(common.fd, termios.TCSAFLUSH, common.old_settings)
deinitialize_termios()

