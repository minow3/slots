import random
import curses
from curses import wrapper

def main (stdscr):
  stdscr.clear()
  stdscr.addstr(1, 0,"------------------------------------------------------------")
  stdscr.addstr(2,20,"WELLCOME TO")
  stdscr.addstr(3, 0,"------------------------------------------------------------")
  stdscr.addstr(4,20, "SLOT MACHINE")
  stdscr.addstr(5, 0,"------------------------------------------------------------")
  stdscr.refresh()
  stdscr.getch()
  
wrapper(main)