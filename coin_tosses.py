import random

def coin_tosses():
    print("Starting the program...")
    num_head = 0
    num_tail = 0
    for i in range(5000):
        random_num = round(random.random())
        print(random_num)
        if (random_num == 1):
            num_head = num_head + 1
            print("Attempt #:",i+1,": Throwing a coin...It's a head!...Got ",num_head," head(s) so far and ",num_tail," tail(s) so far")
        else:
            num_tail = num_tail + 1
            print("Attempt #:",i+1,": Throwing a coin...It's a tail!...Got ",num_head," head(s) so far and ",num_tail," tail(s) so far")
    print("Ending the program. Thank you!")

coin_tosses()
