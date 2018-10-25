##Python 3.7.0 
import math;

userInput = int (input ( "input a decimal number here: " ));
p=0
i=0
def function10To2 (n):
    global p
    global i
    if n == 0:
        return (p)
    else:
        p = p + (n % 2) * (10**i) 
        i = i + 1
        return function10To2(n//2) 

print (function10To2 (userInput))

input ()
      