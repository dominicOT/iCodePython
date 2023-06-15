# Python Loops
Python loops are programming constructs that allow coders to repeatedly execute a block of code until a certain condition is met. <br>
There are two main types of loops in Python.


## for loop:
The ` for loop ` is used to iterate over a sequence such as a list, tuple, string, or range. 

### Syntax
`
for item in sequence:\
    # block to be executed
`  

#### In each iteration, the loop variable (item in the example) takes the value of the next element in the sequence. The loop continues until all elements in the sequence are exhausted.

Here's an example that prints each item in a list:
`
planets = ["jupiter", "venus", "mars"]
for d in planets:
    print(planets)
`
Output:

apple
banana
cherry

while loop:
The while loop repeatedly executes a block of code as long as a specified condition is true. It has the following syntax:

python
Copy code
while condition:
    # Code block to be executed
The loop continues until the condition becomes false. It's important to ensure that the condition eventually becomes false; otherwise, the loop will run indefinitely.

Here's an example that counts from 1 to 5 using a while loop:

python
Copy code
count = 1
while count <= 5:
    print(count)
    count += 1
Output:

Copy code
1
2
3
4
5
Both types of loops can be controlled using statements like break (to exit the loop prematurely), continue (to skip the rest of the current iteration and move to the next one), and else (to execute a block of code when the loop finishes normally without encountering a break statement).

Loops are powerful tools for iterating over data structures, performing repetitive tasks, and implementing algorithms that require repetitive operations.
