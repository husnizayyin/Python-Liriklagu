from time import sleep
import time
import sys

def Aamiin():
    line = [
        ("Tuk petualangan ini",0.15),
        ("Mari kita ketuk pintu yang sama",0.10),
        ("Membawa Aamiin ........",0.10),
        ("Paling serius .... Seluruh dunia......",0.10),
        ##("Seluruh dunia......",0.10),
        ("Bayangkan betapa...... ",0.10),
        ("Cantik dan lucunya ....",0.10),
        ("Gemuruh petir ini ...",0.10),
        ("Disanding rintik-rintik ... yang ... gemas",0.15),
        ("Dan merayakan .....",0.15),
        ("Aamiin paling serius .... seluruh dunia",0.10),
        ("Aamiin paling serius .... seluruh dunia",0.10),
        
    ]
    delays=[1, 2.5, 1.3, 1, 1.2, 1.2, 1, 1.3, 1, 8.5, 1.4]

    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
Aamiin()



