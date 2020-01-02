
#Objective: Create a set of virtual dice to be used in board games / tabletop games


#import random module for use in program
import random



##Get dice count
#ask user to specify how many virutal dice are needed for the game
DiceNeedQuestion="How many dice needed for the game?"

# Implement try and except to ensure whole number of dice is entered...
try:
    total_dice_count=int(input(DiceNeedQuestion))

except:
    print("total dice must be integer")
    total_dice_count=int(input(DiceNeedQuestion))    

#...and implement while so that the number of dice is positive

while total_dice_count <=0:
    print("total dice must be greater than zero")
    total_dice_count=int(input(DiceNeedQuestion))



##ask user to specify the number of sides of each dice and store as list
#setup an empty list to hold dice results
dice_set_used=[]

#iterate on understanding the number of sides for each individual dice
for i in range(total_dice_count):
    DiceSideQuetion = "how many sides for dice"
    
    print(DiceSideQuetion,i+1,"?")
    
    #try and except in case whole number greater than zero not provided for number of sides (dice of side 1 is allowed even though is nonsensical)
    try:
        die_generic_NumSides = int(input())

    except:
        print("sides of dice must be integer")
        print(DiceSideQuetion,i+1,"?")
        die_generic_NumSides = int(input())

    while die_generic_NumSides <4:
        print("Number of sides must be at least 4")  #odd-number of dice and no limit on number of sides allowed for simplicity
        print(DiceSideQuetion,i+1,"?")
        die_generic_NumSides = int(input())

    dice_set_used.append(die_generic_NumSides)

print("\n"
      "The ",total_dice_count,"-dice set is: ", dice_set_used,"\n",sep="")



#Ask if want to do first roll
DiceAgain=input("""Roll dice? ("y"=yes): """)

while DiceAgain.lower() in ["yes","y"]:             
   
   #set list to start out as empty for a new roll
    dice_set_results=[]                             
   
    for i in dice_set_used:                         
        die_random_roll=random.randrange(1,i+1,1)
        dice_set_results.append(die_random_roll)

    print("\nThe roll outcome is:", dice_set_results)

    print("The sum of roll is: ", sum(dice_set_results))
    
    #ask if want to do an additional roll
    DiceAgain=input("\n"
                    """Roll dice again? ("y"=yes): """)



#Notify program is ending
print("Done. Restart program to initiate new set of dice")