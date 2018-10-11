
import math

#find the nth digit of PI

userInput = int(input("what digit of PI would you like?: "))
if userInput <= 0:
    print("You must input a value larger than 0!")


#get the nth value to one's place, convert to int
digit = userInput - 1

power = 10 ** digit

digit = math.pi * power

integer = int(digit)


#calculates preceeding digits of PI excluding one's place
preceeding = digit/10

preInt = int(preceeding)

preIntTen = (preInt * 10)


#gives the final value
finalValue = integer - preIntTen


#print(digit)
#print(integer)
#print(preIntTen)
print(finalValue)
