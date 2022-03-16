#  calculator

# You're going to write an interactive calculator!
# User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space
# (e.g. 1 + --> Split user input and check whether the resulting list is valid:
# -> If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# -> Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
# -> If the second input is not '+' or '-', again raise a FormulaError
# -> If the input is valid, perform the calculation and print out the result.
# -> The user is then prompted to provide new input, and so on until the user enters quit.
# -> Example image in attached in thread

class FormulaError(Exception):
    pass

while True:
    user_input =  input("enter your expression : ").split()
    try:
        if "quit" in user_input and len(user_input)==1:
            break
            
        if len(user_input) == 3 and (user_input[1] == "+" or user_input[1] == "-" ):
            user_input1 = float(user_input[0])
            user_input2 = float(user_input[2])
            if user_input[1] == "+":
                print("result is ", user_input1+user_input2)
            elif user_input[1] == "-":
                print("result is ", user_input1-user_input2)
        else:
            raise FormulaError
    except : 
        print("Enter  valid formula !!!")