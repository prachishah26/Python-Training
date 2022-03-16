#  hot potato game
import time
import random

players = ["prachi", "Aksh", "Praveen", "Kshitij", "Komal", "Vishruti","Dhruvin bhai"]
no_of_players = len(players)
time_delay = 0

while no_of_players>1:
    index = 0
    round_stops_at_sec = random.uniform(5,21)
    # timeout = time.time() + round_stops_at_sec
    while time_delay <= round_stops_at_sec:        
        print(players[index] + " has hot potato")
        delay_in_passing = float("{:.2f}".format(random.uniform(0.1,3.1)))
        time.sleep(delay_in_passing)
        time_delay += delay_in_passing
        last = players[index]
        index += 1
        # print(index,index %no_of_players-1 == 0,no_of_players-1,index%no_of_players-1)
        if index == no_of_players:
            index = 0

    print("---------------------{0} is out !!!--------------------------".format(last))
    print("\nNext round")
    print("------------------------------------------------------------------------\no_of_players")
    players.remove(last)
    
    time_delay = 0
    no_of_players = no_of_players-1
    
print("----------------------{0} is winner !!!!-------------------------".format(players[0])) 