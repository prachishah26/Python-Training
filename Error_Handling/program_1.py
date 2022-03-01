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
    inp =  input("enter your expression : ").split()
    try:
        if "quit" in inp and len(inp)==1:
            break
            
        if len(inp) == 3 and (inp[1] == "+" or inp[1] == "-" ):
            a = float(inp[0])
            b = float(inp[2])
            if inp[1] == "+":
                print("result is ", a+b)
            elif inp[1] == "-":
                print("result is ", a-b)
        else:
            raise FormulaError
    except : 
        print("Enter a valid formula !!!")
       




