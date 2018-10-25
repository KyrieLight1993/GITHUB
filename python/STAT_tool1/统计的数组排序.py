import re
print ("Just use the 'file.txt to input any array then save, and press any key in python")
print ("then this baby will arrange your input values from samll to big!")
print ("It can help you do your Stat homework! you dont have to count by yourself!")
print ("you can have any spaces or enters in your input")
print ("After use please clear the input on the .txt")
print ("Enjoy!")
i = -1 #tell users the number of turn
while True  :#after run one time the last "input()" will restart the loop
    i += 1
    a1 = open('file.txt','r')#import a txtfile named(file.txt)
    a1 = a1.read()#read and covert the txt into strings
    a2 = a1.replace( '\n',' ')#replace '\n' into space
    a3 = re.sub('[^\d\+]', ' ', a2)#filt numbers only
    print ("input " , i , " is " ,a1)
    print ("adjusted input " ,i, " is", a2)
    
    b = a3.split()#convert string with spaces into array
    print ("array ",i, " is", b)
    c = sorted( b , key = float)# arrange array from small to big as integeres

    print ("after arrange " ,i, " is", c)
    input ()#just type any thing to run the culculation again! enjoy! EL PSY CONGROO! 



