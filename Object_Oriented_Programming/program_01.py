
# Take the word and its meaning as input from the user.
# -> Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
# -> Now use the __str__() function to return a string that contains the word and meaning.
# -> Store the returned strings in a list named flash.
# -> Use a while loop to print all the stored flashcards.
# -> Add proper error handling
# 		-> Result image is attached in thread

flash = []
class flashcard:
    def __init__(self,value,meaning,user_inp):
        self.value = value
        self.meaning = meaning
        self.user_inp = user_inp
        
    def __str__(self):
        return value +" (" + meaning + " )"

a = 0
while user_inp == 0:
    value = input("Enter the value : ")
    meaning = input("Enter the meaning : ")
    user_inp= input("Enter 0 if you want to add another flash card : ")
    raw = flashcard(value,meaning, user_inp)
    flash.append(raw.__str__())
    try :
        a = int(input("enter : "))
    except:
        print("please enter valid number")
        a = 0
print("\nYour flashcards : ")
for i in range(len(flash)):
    print(flash[i])

    


































# flash = []
#         a = 0
#         while a==0:
#             flash.append(self.value + " (" + self.meaning + " )")
#             a = input()
#             b = flashcard(value,meaning, user_input)
#             print(b)