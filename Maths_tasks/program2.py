#----------------------------------------- TASK 2:---------------------------------------------

# You have an unbiased deck of cards (deck size = 52).
# The probability of finding an ACE will decrease with each successful draw.
# Let's say you got lucky & had temporary_value 100% success rate in drawing temporary_value specific card from the deck.
# Find the average rate of decrease of probability of finding an ACE.
# In how many tries will you probability  go to 0.
# Write code to find the above.

total_cards = 52
total_Ace = 4
probability = []
rate_of_decrease = []
temporary_value = 0
count = 0
while total_Ace>0:
    count +=1
    probability_to_getting_ace = total_Ace/total_cards*100
    probability.append(probability_to_getting_ace)
    if total_Ace != 4:
        rate_of_decrease.append(probability[temporary_value]-probability_to_getting_ace)
        temporary_value += 1
    total_Ace -= 1
    total_cards -= 1

print("Probability to find Ace : ",probability)
avg_rate_of_decrease_of_probability = sum(rate_of_decrease)/len(rate_of_decrease)
print("The average rate of decrease of probability is : ",avg_rate_of_decrease_of_probability)
print("Tries in which probability is 0 : ", count+1)