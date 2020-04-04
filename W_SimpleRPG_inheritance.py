#Objective: Demonstrate a simple role-playing-game (RPG) battle that uses classes to create a character for each instance
#Classes with inheritance are also used to create the enemy

#Notes on some of the variables
#Attack Points (AP) are the base amount of damage a character produces from a basic (non-magic) attack
#Magic Points (MP) are the base amount of damage a character produces from a magic (non-basic) attack
#Health Points (HP) are the starting value a character has.  Attacks by enemies decrease the value.  If the value falls to zero, the character can take no further action

#import numpy module for random integer generation
import numpy as np
import random
import time
import sys

#create class that can create character with basic attack points (AP), magic points (MP), and health points (HP)
class RPGCharacterCreate:
    def __init__(self,name,CharType):
        self.name=name
        self.CharType = CharType
        if CharType.lower() in ["warrior","w"]:
            self.AP = 100
            self.MP = 10
            self.HP = 1000
            self.ClassDescribe = "Warrior"
            
        
        elif CharType.lower() in ["mage","m"]:
            self.AP = 40
            self.MP = 80
            self.HP = 400
            self.ClassDescribe = "Mage"
    

        #create a "balanced" generic character if the user does not specify a warrior / mage or mistypes warrior / mage
        else: 
            self.AP = 70
            self.MP = 40
            self.HP = 800
            self.ClassDescribe = "Balance"
            

    ##define methods for class
    #method: state the character details
    def CharDetails(self):
        print(f"I am a {self.ClassDescribe} class with {self.AP}AP and {self.MP}MP.  You may call me, {self.name}")
        
    ##method: same function as above but using return instead of print to show different implementation approach
    #def CharDetailsRtn(self):
    #    return f"I am a {self.CharType} class with {self.AP}AP and {self.MP}MP.  You may call me {self.name}"
      

    #method: attack damage from basic attack
    def CharAttack_ap(self):
        dmg_ap=self.AP + np.random.randint(0,21,1)  #each damage roll for attack is character's AP + a random bonus of 0 to 20
        return dmg_ap

    #method: attack damage from magic attack
    def CharAttack_mp(self):
        dmg_mp=self.MP + np.random.randint(20,81,1)  #each damage roll for attack is character's MP + a random bonus of 20 to 80
        return dmg_mp

    #method: damage taken from enemy
    def CharDamageTaken(self,DamageReceived):
        self.DamageReceived = DamageReceived
        #print("You strike the enemy and deliver the damage")
        self.HP = max(0,self.HP - self.DamageReceived)


#Define details to create an enemy character
#Create dictionary of possible enemy encounters.  For key-value pairs: Key is name; values are Hit Points (HP) and Attack Points (AP)
enemy_dict = {"Deceptive Bunny":[600,60,30,60],"Sneaky Marauder":[800,20,20,150]}  #values are HP, base damage, additional damage low, additional damage high


#Define an enemy class with methods for attack and defend
class EnemyCreate:
    def __init__(self,EnemyName,EnemyHP,EnemyBaseDamage,EnemyExtraDamageLow,EnemyExtraDamageHigh):
        self.EnemyName = EnemyName
        self.EnemyHP = EnemyHP   
        self.EnemyBaseDamage = EnemyBaseDamage
        self.EnemyExtraDamageLow = EnemyExtraDamageLow
        self.EnemyExtraDamageHigh = EnemyExtraDamageHigh

    #Define enemy attack as a method
    def EnemyAttack(self,base,modifier_low, modifier_high):
        self.base = base
        self.modifier_low = modifier_low
        self.modifier_high = modifier_high
        return self.base + np.random.randint(self.modifier_low,self.modifier_high,1)

    #Define enemy defend as a method
    def EnemyDamageTaken(self,AttackReceived):
        
        self.DamageApplied = AttackReceived

        if self.DamageApplied == 0:  # allows for passing in no dmaage situations such as damage from shield, dodging, etc
            print("No damage dealt!")
        
        else:
            print("You strike the enemy and deliver the damage")
            self.DamageApplied = AttackReceived
            self.EnemyHP = max(0,self.EnemyHP - self.DamageApplied)
        
        return self.DamageApplied


#Define an enemy class with inheritance that adds a shield
class EnemyCreateWithShield(EnemyCreate):
    def __init__(self,EnemyName,EnemyHP,EnemyBaseDamage,EnemyExtraDamageLow,EnemyExtraDamageHigh,ShieldBlockPct):
        super().__init__(EnemyName,EnemyHP,EnemyBaseDamage,EnemyExtraDamageLow,EnemyExtraDamageHigh)
        self.ShieldBlockPct = ShieldBlockPct


    #Define enemy defend with shield as a method and then call the base class method of same name
    def EnemyDamageTaken(self,AttackReceived):   #consider adding magic attack always passes through shield
        #there is a chance the attack is blocked
        if random.random() <= self.ShieldBlockPct:
            #attack is blocked by shield
            print("Attack is blocked by enemy shield!")
            AttackReceived = 0
        
        return super().EnemyDamageTaken(AttackReceived)



#Define function that delays the time to show the result of an action (such as waiting to see how much attack damage is caused)
#Suspense is "built" by displaying the characters of the message one at a time
def suspense_build(suspense_message):
    for x in suspense_message:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.5)
    print()



##Gather details from user to create character to then invoke class creation
#collect character name with a character limit
char_limit=20  #set character limit (here, 20)
RPGInput_Name=input(f"Provide a character name ({char_limit} char limit):")
while len(RPGInput_Name) > char_limit:
    RPGInput_Name=input(f"That was too long.  Provide a character name ({char_limit} char limit):")

#collect character class selection
RPGInput_Type=input("Choose character type: (Warrior (W), Mage (M) or press ENTER for Balanced):")

#use user inputs to to create new character from class
RPGOutput_Character01 = RPGCharacterCreate(RPGInput_Name,RPGInput_Type)
print("\nCongratulations!  You have created a character!")
print("The character, greets you:")
RPGOutput_Character01.CharDetails()



##Have user decide if want to send the character to battle
#Request yes or no for value of battle initiation variable
initiate_battle=input(f"Send {RPGOutput_Character01.name} to battle?  (y = yes)")

#Define logic that occurs if user chooses to go to battle (with "y" or "yes" response) or chooses to skip battle
if initiate_battle.lower() in ["yes","y"]:

    #Create an enemy by selecting randomly from the enemy dictionary  (This could be done outside of if but enemy not generated if no battle)
    EnemySelect = random.choice(list(enemy_dict.keys()))
    
    #Grab starting HP of enemy and its attack range
    EnemyBattleHP = enemy_dict[EnemySelect][0]
    EnemyBaseDamage = enemy_dict[EnemySelect][1]
    EnemyLowModify = enemy_dict[EnemySelect][2]
    EnemyHighModify = enemy_dict[EnemySelect][3]

    #Create the enemy using classes.  Introduce chance that the enemy has a shield
    EnemyHasShield = False  #Set default to no shield
    ShieldChanceToBlock = 0.30 #Probability of shield successfully blocking attack if have shield

    if random.random() <= 0.40:   #Determine if enemy will have a shield.  If so, use "sub" class with inheritance that supports shield with a block percentage
        EnemyHasShield=True
        EnemyOpponent = EnemyCreateWithShield(EnemySelect,EnemyBattleHP,EnemyBaseDamage, EnemyLowModify, EnemyHighModify,ShieldChanceToBlock)

    else:  #use "base" class that has no concept of enemy shield
        EnemyOpponent = EnemyCreate(EnemySelect,EnemyBattleHP,EnemyBaseDamage, EnemyLowModify, EnemyHighModify)


    #####Set starting HP of player
    ####PlayerBattleHP=RPGOutput_Character01.HP
    
    #The battle begins!!
    print("\nAn enemy appears!")
    print(f"It is a {EnemyOpponent.EnemyName}")
    if EnemyHasShield:
        print("...and it has a shield!")
    print("The enemy's HP and AP is unknown")
    print(f"\nYour starting HP total is {RPGOutput_Character01.HP}")

    #check current hit points
    while  RPGOutput_Character01.HP > 0 and EnemyOpponent.EnemyHP > 0:

        #choose attack
        print("You prepare to attack")
        attack_type=input("Choose basic attack or magic attack (basic = b, magic = m):")

        print("\nattacking now")
        suspense_build("...") #delaying until the attack damage is displayed to give appearance of attack being in progress

        if attack_type.lower() in ["basic","b"]: 
            AttackAmt = RPGOutput_Character01.CharAttack_ap()
            print(f"Attempted basic damage to deal to enemy: {AttackAmt}")

        else:  #always do magic attack if basic attack is not selected
            AttackAmt = RPGOutput_Character01.CharAttack_mp()
            print(f"Attempted magic damage deal to enemy: {AttackAmt}")
        
        #calculate if enemy takes damage and its remaining HP
        EnemyOpponent.EnemyDamageTaken(AttackAmt)

        #Determine if enemy is defeated (HP at zero) or enemy survives and responds with an attack
        if EnemyOpponent.EnemyHP <= 0:
            print(f"The {EnemyOpponent.EnemyName} is defeated")
            break
        else:
            print(f"The {EnemyOpponent.EnemyName} remains alive")
            print(f"\nThe {EnemyOpponent.EnemyName} attacks!")
            EnemyAttackAmt = EnemyOpponent.EnemyAttack(EnemyBaseDamage,EnemyLowModify,EnemyHighModify)
            suspense_build("...") #delaying until the attack damage is displayed to give appearance of attack being in progress
            print(f"The {EnemyOpponent.EnemyName} deals total damage of {EnemyAttackAmt}")
            

            #Apply Enemy Attack to modify Hero's HP...
            RPGOutput_Character01.CharDamageTaken(EnemyAttackAmt)

            #...and dtermine if Hero is still alive
            if RPGOutput_Character01.HP <= 0:
                print("Your HP has fallen to zero.  You are defeated")
                break

        print(f"Your current HP total is {RPGOutput_Character01.HP}")


        print("\n")

#acknowledge that user chooses not to go to battle
else:    
    print(f"Instead of goign to battle, {RPGOutput_Character01.name} takes a nap")


