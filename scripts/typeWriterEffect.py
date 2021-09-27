from time import sleep
import sys

def typeWriter(my_str):
    if '\n' in my_str:
        my_str = my_str.strip('\n')
    for char in my_str:
        sleep(0.07)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')
