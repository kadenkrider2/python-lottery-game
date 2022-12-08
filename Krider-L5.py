'''

NAME: KADEN KRIDER

ASN: L5

DESC: This python module reads at 3 digit number from the user and compares the numbers to computer generated number

DATE: November 25, 2022

'''


import random
from random import randint
# generate 3 random numbers for lottery 
computer_generate1 = random.randint(1,9)
computer_generate2 = random.randint(1,9)
computer_generate3 = random.randint(1,9)
#create a variable 
realNumber = str(computer_generate1) + str(computer_generate2) + str(computer_generate3)
# open numbers in read mode using with/as
 with open("numbers.txt") as f:
   number = f.readline()
print(number)
print(realNumber)
   

#If the user's number (pick) is an EXACT MATCH (same 3 numbers in the same order), then print a statement of a $10000 award   
if number == realNumber:
    print("You won $10,000")
#create an if elif statement for printing the different  computer generate options     
count = 0
for i in number:
  if i == str(computer_generate1):
      count += 1
  elif i == str(computer_generate2):
      count += 1
  elif i == str(computer_generate3):
      count += 1
   
#If the user's number (pick) contains 1 number from the computer generated pick, then print a statement of a $1 award
#If the user's number (pick) contains 2 numbers from the computer generated pick, then print a statement of a $100 award
#If the user's number (pick) contains 3 numbers from the computer generated pick, then print a statement of a $1000 award
if count == 1:
    print("You won $1")
elif count == 2:
    print("You won $100")
elif count == 3:
    print("You won $1000")
elif count == 0:
    print("Sorry you lose")

 




