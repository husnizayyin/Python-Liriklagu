from time import sleep
import time
import sys

def bunga():
    line = [
        ("Ohhhh.....",0.15),
        ("Ku menembus ruang dan waktu",  0.10),
        ("Terjalin gelak tawa, sedih dan merayu", 0.10),
        ("Bersanding bersama dirinya", 0.10),
        ("-------------------------------------", 0.10),
        ("Ohhhh .....",0.10),
        ("Hanya satu yang kan ku pinta",0.10),
        ("Menjaga bunga abadi yang tlah kuberi", 0.10),
        ("Satu dan selamanya.", 0.10),
        ("Di dalam perjalanan hidupnya", 0.15),
        ("Ku persembahkan bunga abadi yang kupetik untuknya", 0.20),
    ]
    delays=[1, 2.5, 1.8, 2.7, 1.4, 2.3, 2.3, 1.5, 1, 8.7, 1.8]

    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
bunga()