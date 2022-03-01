### Program_1 - calculator

User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space<br>
(e.g. 1 + --> Split user input and check whether the resulting list is valid:<br>
-> If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.<br>
-> Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError<br>
-> If the second input is not '+' or '-', again raise a FormulaError<br>
-> If the input is valid, perform the calculation and print out the result.<br>
-> The user is then prompted to provide new input, and so on until the user enters quit.<br>
-> Example image in attached in thread<br>

Input : space seperated values and operator<br>
Output : result of the formula
<br>

#### Testcases:

| Input | Output |
| ----- | ------ |
| 1 + 2 | 3.0 |
| 2 - 1 | 1.0 |
| 1 * 2 | enter a valid formula !!|

<br>
<br>

### Program_2 - Create while loop which increase counter by one every second. Start count from 0, Stop while loop when counter is grater than 500, Program must not stop on any keyboard press. (Not even ctrl + c or ctrl + x)



Input : number of time we want to print numbers<br>
Output : print all numbers without keyboard Interruption.
<br>


#### Testcases:

| Input | Output |
| ----- | ------ |
| 500 | start from 1 and prints all numbers till 500 without any interruption of keyboard |
