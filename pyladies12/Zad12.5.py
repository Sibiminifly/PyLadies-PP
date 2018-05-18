#import datetime
#print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#template = 'His name is {0} {1}. {0} is happy!'
#name = 'John'
#last_name = 'Smith'
#print(template.format(name, last_name))

import datetime
import time
import random

random.seed()

fp = open('warunki-pogodowe.txt', 'a+', encoding='UTF-8')

template = "{}, Temperatura: {}, Ciśnienie {}, Wilgotność = {}, Prędkość wiatru = {}\n"

for _ in range(30): #podkreślnik nie jest ważny, kwestia stylistyczna
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temp = random.randint(-35, -20)
    pressure = random.randint (978, 1080)
    humidity = random.randint(50, 70)
    wind = random.randint(20, 68)
#    print(current_time, temp, pressure, humidity,wind)

    info = template.format(current_time, temp, pressure, humidity, wind)
    print(info)
    fp.write(info)
    time.sleep(1)

fp.close()


