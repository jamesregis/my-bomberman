import select
import sys
import curses


def test(timeout):
    screen = curses.initscr()
    curses.start_color()
    
    curses.noecho()
    curses.cbreak()
    screen.keypad(1)

    keyboard_fd = sys.stdin.fileno()
    select_input_list = [keyboard_fd]
    k = 0
    while 1:
        i,o,e = select.select(select_input_list, [], [], 0.1)
        screen.addstr(0, 0, "Dans la boucle")

        if not i:
            screen.addstr(0, 2, "Dans la boucle")
            k = k+1
            screen.refresh()

        if keyboard_fd in i:
            ch = screen.getch()
          
            if ch == ord("q"):
                screen.addstr(10, 0, "Quit request")
                break
            if ch == curses.KEY_UP:
                screen.addstr(11, 14, "KEY_UP pressed")
            if ch == curses.KEY_DOWN:
                screen.addstr(11, 14, "KEY_DOWN pressed")
            if ch == curses.KEY_RIGHT:
                screen.addstr(11, 14, "KEY_RIGHT pressed")
            if ch == curses.KEY_LEFT:
                screen.addstr(11, 14, "KEY_LEFT pressed")
            if ch == ord(" "):
                screen.addstr(11, 14, "SPACE pressed")





    screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

if __name__ == "__main__":
    test(10)
