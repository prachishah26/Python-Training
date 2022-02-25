
import time
import random

users = ["prachi", "Aksh", "Praveen", "Kshitij", "Komal", "Vishruti"]
n = len(users)
time_delay = 0

while n>1:
    t = 0
    round_stops_at_sec = random.uniform(5,21)
    # timeout = time.time() + round_stops_at_sec
    while time_delay <= round_stops_at_sec:        
        print(users[t] + " has hot potato")
        delay_in_passing = float("{:.2f}".format(random.uniform(0.1,3.1)))
        time.sleep(delay_in_passing)
        time_delay += delay_in_passing
        last = users[t]
        t += 1
        # print(t,t %n-1 == 0,n-1,t%n-1)
        if t == n:
            t = 0

    print("---------------------{0} is out !!!--------------------------".format(last))
    print("\nNext round")
    print("------------------------------------------------------------------------\n")
    users.remove(last)
    
    time_delay = 0
    n = n-1
    
print("----------------------{0} is winner !!!!-------------------------".format(users[0])) 