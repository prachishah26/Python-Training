#  Create class Cards with two list suits (Hearts, Diamonds, Clubs, Spades) and  values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
# -> Create a class deck. That contains a method to get a card set containing 52 elements.
# -> Create class shuffle. That contains two methods to shuffle given cards and remove/pick a single card.
# -> Create two objects of the above class as players. Each player pick/remove 5 cards from the shuffle cards. Total points of both players and display name of winner player.

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
all_cards = []
import random
class cards:
    def __init__(self,suits,values):
        self.suits = suits
        self.values = values

a = cards(suits,values)

class deck:
    def group_cards():
        for i in range(len(a.suits)):
            for j in range(len(a.values)):
                all_cards.append(f'{a.suits[i]}-{a.values[j]}')
        return all_cards


unique_cards = deck.group_cards()
arr = []
class shuffle:
    def shuffling(a):
        for i in range(len(unique_cards)):
            j = random.randint(0,51)
            c = unique_cards[j]
            unique_cards[j] = unique_cards[i]
            unique_cards[i] = c
        print("shuffling done")
        return unique_cards
    def pick(self):
        picked_card = random.randint(0,len(unique_cards)-1)
        player_card = unique_cards[picked_card]
        # print("picked card is ",player_card)
        arr.append(player_card)
        unique_cards.remove(unique_cards[picked_card])


# print(shuffle.shuffling(unique_cards))
p1 = []
p2 = []
players = shuffle()
# player2 = shuffle()
for i in range(10):
    players.pick()
    if i<5:
        number = arr[i][-1]
        print("player-1 has ",arr[i])
        if type(number) == str:
            norm_number = abs(ord(number)-100)
            p1.append(norm_number)
        # elif type(number) == int:
        #     norm_number = number
        #     p1.append(norm_number)
    else:
        number = arr[i][-1]
        print("player-2 has ",arr[i])
        if type(number) == str:
            norm_number = abs(ord(number)-100)
            p2.append(norm_number)
        # elif type(number) == int:
        #     norm_number = number
        #     p2.append(norm_number)

points_of_p1 = sum(p1)
points_of_p2 = sum(p2)

# print(p1)
# print(p2)
if points_of_p1>points_of_p2:
    print("Winner is player-1 !!!!!")
else:
    print("Winner is player-2 !!!!!")

# print(arr)


