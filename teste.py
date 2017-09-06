#Abrir o browser considerando um determinado tempo.

import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program starts on " + time.ctime())

while (break_count < total_breaks):
    time.sleep(5)
    webbrowser.open("http://serpro.gov.br")
    break_count = break_count + 1


