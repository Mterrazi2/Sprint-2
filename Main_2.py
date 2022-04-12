#Michael Terrazi
#This program is a calculator that calculates KDA ratio for Call Of Duty

#Math Program:
print(2**8)
#turns 8 into an exponet, 2 to the power of 8
print(2*8)
#multiply 2 by 8
print('*')
#Exponet
print(2/8)
#2 divided by 8
print(2%8)
#Remainder
print(2//8)
#floor division: rounds down
print(2+8)
#sum
print("+")
#Addition
print(2-8)
#Subtract

if 2<4:
    print("True")
else:
    print("false")
#If Else Statements
    
print(8==8)
#if equal to, then true
print(8!=8)
#if not equal to, then true
print(2<=8)
print(not(2<5 and 5<8))
print(2<5 and 5<8)
print(2<5 or 5<8)
#operators

x = 2
while x < 8:
  print(x)
  x += 1
my_list = ["A", "B", "C"]
for x in my_list:
    print(x)
for x in range(2, 8):
    print(x)
for x in [0, 1, 2]:
  pass
#Empty loop


def calculate(radius):
    area = path.py * radius ** 9
    print("Area of a circle with a radius of", radius, "is",
          format(area, ".2f"))
    return area
#Function with return parameters


#Project Program
print("\nHello", " greetings!", sep=' &')
#Sep function

print ("Welcome To KDA Calculator!\n", end ="\n")

print("Choose Gamemode: \n1. TDM \n2. S&D \n3. Hardpoint \n4. Domination")
#Menu

x = int(input("Enter Gamemode: "))

if (x == 1):
    print("\nYou have selected TDM!")
elif (x == 2):
    print("\nYou have selected S&D!")
elif (x == 3):
    print("\nYou have selected Hardpoint!")
elif (x == 4):
    print("\nYou have selected Domination!")
else:
    print("\nThat is not a gamemode. Try again!")
#Menu Ountcomes
    
kills = print("\nEnter Kills: ")
firstNum = int(input().strip())
#number of kills

assists = print("Enter Assists: ")
secondNum = int(input().strip())
#number of assists


Death = print("Enter Deaths: ")
thirdNum = int(input().strip())
#number of deaths

KA = (int(firstNum+secondNum))
#sum of kills and assists

KDA = (int(KA/thirdNum))
#divide the sum of kills and assists by the number of deaths

if (KDA>2.00):
    print ("KDA Ratio: ", "{:.2f}".format(KDA))
    print ("Good Job! Your KDA is positive!")

else:
    print ("KDA Ratio: ", "{:.2f}".format(KDA))
    print ("Your KDA is negative!")
