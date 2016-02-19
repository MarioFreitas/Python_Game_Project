import os
from time import sleep


# Clean Interpreter Function
def clc():
    # os.system('cls')
    print '\n'*100


# Pause code
pause_option = False


def pause(seconds):
    if pause_option:
        sleep(seconds)
    else:
        raw_input("")


# Custom Input
def c_input(text, str_list):
    while True:
        inp = raw_input(text)
        if inp in str_list:
            return inp
