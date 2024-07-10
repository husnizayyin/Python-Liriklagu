from time import sleep
import time
import sys

def print_lirik():
    lines = [
        ("Aku yang jatuh cinta",0.10),
        ("Haruskah kau kuberi kesempatan",0.07),
        ("Ingin aku jadi kekasih yang baik",0.07),
        ("Berikan aku kesempatan oh",0.08),
        ("Tahukah dirimu?, tahukah hatimu?",0.06),
        ("Berulang kuketuk, aku mencintamu",0.08),
        ("Tapi dirimu tak pernah sadari",0.05),
        ("Aku yang jatuh cinta",0.10),
    ]
    delays=[7.2, 3, 2.5, 7.5, 3.5, 4, 3.5, 3.5]

    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
print_lirik()

