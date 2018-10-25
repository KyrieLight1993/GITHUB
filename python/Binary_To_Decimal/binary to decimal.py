##Python 3.7.0 
import math;

userInput = int (input ( "put a binary number here: " ));

length =  len ( str ( userInput ) );

base = [ pow ( 2 , length -  i - 1 ) for i in range ( 0, length ) ];

print ( base );
result  =  0
for j in range ( 0, length ): 
    result = result + base[ j ] * ( userInput // ( 10**( length - j - 1 ) ) % 10 );
print (result);
input ();