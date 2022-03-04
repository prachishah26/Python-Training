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

card = cards(suits,values)

class deck:
    def group_cards():
        for i in range(len(card.suits)):
            for j in range(len(card.values)):
                all_cards.append(f'{card.suits[i]}-{card.values[j]}')
        return all_cards


unique_cards = deck.group_cards()
list_of_players = []
class shuffle:
    def shuffling(card):
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
        list_of_players.append(player_card)
        unique_cards.remove(unique_cards[picked_card])


# print(shuffle.shuffling(unique_cards))
player1 = []
player2 = []
players = shuffle()
# player2 = shuffle()
for i in range(10):
    players.pick()
    if i<5:
        number = list_of_players[i][-1]
        print("player-1 has ",list_of_players[i])
        if type(number) == str:
            norm_number = abs(ord(number)-100)
            player1.append(norm_number)
        # elif type(number) == int:
        #     norm_number = number
        #     player1.append(norm_number)
    else:
        number = list_of_players[i][-1]
        print("player-2 has ",list_of_players[i])
        if type(number) == str:
            norm_number = abs(ord(number)-100)
            player2.append(norm_number)
        # elif type(number) == int:
        #     norm_number = number
        #     player2.append(norm_number)

points_of_player1 = sum(player1)
points_of_player2 = sum(player2)

if points_of_player1>points_of_player2:
    print("Winner is player-1 !!!!!")
else:
    print("Winner is player-2 !!!!!")

