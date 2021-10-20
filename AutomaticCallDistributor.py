#Name: David Rogers
#Date: May 18, 2021

from Queue import Queue
from Call import Call
from datetime import date
import time
import random

print("Name: David Rogers\nDate: {0}".format(str(date.today())))

call_data = []
file = 'ClientData.csv'

with open(file) as infile:
    for line in infile:
        s = line.split(',')
        client_id = int(s[0])
        client_name = s[1]
        phone = s[2]
        

        c = Call(client_id, client_name, phone)

        call_data.append(c)

calls_waiting = Queue()
call_number = 0

print()
seconds = int(input("How many seconds should the simulation run? "))
print()

x = 0

for i in range(seconds):
    x += 1
    print('-'*40)
    print(x,". ")
    time.sleep(1)
    random_num = random.randint(1,3)

    if random_num == 1:
        random_caller = random.randint(0, len(call_data))
        
        calls_waiting.enqueue(call_data[random_caller])
        print("Call recieved. Caller added to queue.")
        call_number += 1

        print("\tCalls waiting: ", calls_waiting.get_length())
        print()
        
    elif random_num == 2:
        print("Call being routed to a service representative: ")
        if calls_waiting.get_length() > 0:
            call = calls_waiting.dequeue()
            call_number -= 1
            print("\n", call, "\n")
            print()
        else:
            print("Call could not be routed, no calls in the queue.")

        print("\tCalls waiting: ", calls_waiting.get_length())
        print()
        
    else:
        print("Nothing happened during this second.")
        print("\tCalls waiting: ", calls_waiting.get_length())
        print()

print("\nThe simulation has completed.")
