import sys
import termios

import tty


def get_single_input(question):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    print question
    try:
        tty.setraw(sys.stdin.fileno())

        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


tt="Qui es tu ?"
caract = get_single_input(tt)

print "Resultat %s" %caract
