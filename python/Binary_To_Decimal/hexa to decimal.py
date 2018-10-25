##Python 3.7.0 
import math;

userInput = str (input ( "put a hexadecimal number here: " ));

length =  len (  userInput  );

base = [ pow ( 16 , length -  i - 1 ) for i in range ( 0, length ) ];

print ( base );

baseList = list (userInput)
print (baseList )
A=10
B=11
C=12
D=13
E=14
F=15
for n,i in enumerate(baseList):
    if i== 'A' or i == 'a':
     baseList[n]=10
    if i== 'B' or i == 'b':
     baseList[n]=11
    if i== 'C' or i == 'c':
     baseList[n]=12
    if i== 'D' or i == 'd':
     baseList[n]=13
    if i== 'E' or i == 'e':
     baseList[n]=14
    if i== 'F' or i == 'f':
     baseList[n]=15
numlist = list (map(int, baseList))
print (numlist )
result  =  0
for j in range ( 0, length ): 
    result = result + base[ j ] * numlist [j] ;
print (result);
input ();
