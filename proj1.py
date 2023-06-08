#File: proj1.py
#Author: Hamza Ilyas
#Date: 10/18/2018
#Section: 21
#E-mail: hamza3@umbc.edu
#Description:
#    This text-based adventure game will allow this user to make multiple
#    decisions while in a simulated forest, where a hiking trip goes bad.
#    The user is in the vicinity of a monster that they must escape, so,
#    the objective of the game is to escape by travelling 150 miles toward
#    the closest town, or survive for 7 days. If they can do this, they win.




from random import randint, seed
seed(100)




#-----INITIALIZATION OF ALL CONSTANTS-----#


MAX_PLAYER_HEALTH = 100
BASE_DEMOGORGON_ATTACK = 20
BASE_DEMOGORGON_HEALTH = 300

SURVIVE_DAYS = 7
SURVIVE_DIST = 150


FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]
FOOD_VALS = [-30, -5, 15, 25, 30]
WAFFLE_VAL = 10

ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys",
         "Walkman", "Laser Cannon", "Rubber Band"]

WEAPONS = ["Flashlight", "Walkie Talkie", "Rubber band", "Sword", "Laser cannon"]
WEAPON_DMG = [5, 10, 25, 50, 100]

DAY_MENU = ["View your inventory", "View your stats",
             "Eat an eggo waffle", "Nothing else"]

AFTER_DAY_MENU = ["Pack up camp and leave to find civilization",
                   "Stay put for the day"]

EQUIP_MENU = ["Equip", "Unequip", "I changed my mind"]

TRAVEL_MENU = ["Pack up camp and go", "Stay where you are"]

FIGHT_MENU = ["Fight", "Flail", "Flee"]

EAT_MENU = ["Eat it",
            "Put it back"]

WALKMAN_DEBUFF = 0.75

NO_EQUIPPED_ITEM = "N/A"









#distanceTraveled(playerHealth, inventory, trenchActivation)
#calculates how much the user has traveled in a day by checking for certain
#items in their inventory, and whether they fell in a trench, and their current
#health.
#
#
#Input:         playerHealth; the current health of the player.
#               inventory; items in their inventory.
#               trenchActivation; whether or not they fell in a trench.
#
#Output:        calcaultedDist; the end result of the player's ealth calculation,
#               which is the new player health.
def distanceTraveled(playerHealth, inventory):

   if ITEMS[1] in inventory:
      calculatedDist = ((playerHealth / 4) + 5)
      #-----CHECK TO SEE IF BIKE IN INVENTORY-----#
      calculatedDist *= 1.5
      print("The bicycle you found improved your distance traveled.")
      return calculatedDist

   #-----USE ELIF TO GIVE BIKE PRESCENDENCE-----#
   elif ITEMS[3] in inventory:
      calculatedDist = ((playerHealth / 4) + 5)
      #-----CHECK TO SEE IF HEELY'S IN INVENTORY-----#
      calculatedDist *= 1.25
      print("The heelys you found improved your distance traveled.")
      return calculatedDist

      
   if ITEMS[3] and ITEMS[1] not in inventory:
      calculatedDist = (playerHealth / 4) + 5
      return calculatedDist






   


#printIntro()
#prints the beginning text of the game instead of having lots of strings in main.
#
#
#Input:         none; it's a print function.
#Output:        strings; the intro of the game.
def printIntro():

   print("\nAfter miles and miles of hiking in the woods, you finally setup "\
         "your  camp. \nYou decided to go camping on the wrong weekend.\n"\
         "Your phone buzzes:"\
	 "\n\t\tTHE DEMOGORGON HAS ESCAPED.		RUN.")







   

   
#displayMenu(choices)
#prints a menu with a corresponding number at the beginning to the index + 1.
#
#
#Input:         choices; the menu list that wants to be printed out.
#Output:        none; it only displays the menu.
def displayMenu(choices):


    print("\nYour options are: \n")
    
    i = 0
    while i < len(choices):
        #-----USE i+1 BECAUSE INDEX STARTS AT 0-----#
        #-----WHEREAS MENU OPTIONS START AT 1------#
        print(i + 1, "-", choices[i])
        i += 1

    print()




    

#getUserChoices(choices)
#Gets the choice that the user wants to select from the
#aforementioned menu that was displayed.
#
#
#Input:         choices; the list we're deriving the choice of the user from.
#Output:        userChoice; the choice the user selected from the menu.   
def getUserChoices(choices):


    userChoice = int(input("Enter a choice: "))

    #-----VALIDATE AN OPTION IN THE MENU-----#
    while userChoice < 1 or userChoice > len(choices):
        print("Invalid choice!\n")
        userChoice = int(input("\nEnter a choice: "))

    return userChoice








 
 
#calcDamage(item)
#Calculates the damage the user does to the monster per hit.
#
#
#Input:         item; the item that we'll correlate the damage to,
#               which is a string.
#Output:        an index in the corresponding list of damages; this is the
#               number they hit according to the item.
def calcDamage(item):

    i = 0
    passedItem = item
    while i < len(WEAPONS):
        if passedItem == WEAPONS[i]:
            #-----SIMPLY RETURN THE CORRESPONDING DAMAGE-----#
            #-----TRAVERSE ALL POSSIBLE WEAPONS UNTIL-------#
            #-----A MATCHING WEAPON IS FOUND.--------------#
           return WEAPON_DMG[i]
        else:
            i += 1





            



#eat(food, playerHealth)
#calculates how much a player heals after eating a certain food.
#
#
#Input:         food; a string so we know how much points to give
#               playerHealth; so we can return the new health and make sure it
#               doesn't exceed 100.
#Output:        the max health which is 100 if the new food would exceed.
#               Otherwise, return the food health value plus the current health.
def eat(food, playerHealth):


    #-----THIS IF WILL BE ENABLED IF EATING A WAFFLE-----#
    if food == "Waffle":

        remainingWaffleHP = MAX_PLAYER_HEALTH - playerHealth

        #-----IF PLAYER IS BELOW 100 HEALTH, ADD VALUE-----#
        if playerHealth + WAFFLE_VAL < MAX_PLAYER_HEALTH:
            print("You eat the waffle. So bad yet so good.")
            return playerHealth + WAFFLE_VAL
         
        #-----IF THEIR HEALTH WOULD EXCEED 100, RETURN 100-----#
        else:
            print("\nSince 100 health is the maximum: ")
            print("You were healed for", remainingWaffleHP, "HP, ", end = "")
            print("instead of the", WAFFLE_VAL, "that a waffle would provide.")
            print("Your health has been restored to full.\n")

            return MAX_PLAYER_HEALTH
            
    #-----FOR ALL FOODS EXCEPT WAFFLE-----#
    if food in FOODS:
            
        i = 0
        chosenFoodVal = 0
    
        while i < len(FOODS):
            if food == FOODS[i]:
                chosenFoodVal = FOOD_VALS[i]
            i += 1
        if chosenFoodVal + playerHealth < MAX_PLAYER_HEALTH:
            print("\nYou eat the", food, "for a total of", chosenFoodVal, "HP.")
            print("Your new HP is:", chosenFoodVal + playerHealth, "\n")

            return chosenFoodVal

        else:
            remainingHeal = MAX_PLAYER_HEALTH - playerHealth
            print("\nSince 100 health is the maximum: ")
            print("You were healed for", remainingHeal, "HP, ", end = "")
            print("instead of the", chosenFoodVal, "that", food, "would provide.")
            print("Your health has been restored to full.\n")
        
            return MAX_PLAYER_HEALTH





         


#fight(playerHealth, item, inventory)
#executes an entire fight until either the player or monster reaches 0 health.
#
#
#Input:         playerHealth; the current player health to start the fight at.
#               item; a string, the current item the player has equipped
#               inventory; a list, so we can see if the monster will be given
#               any debuffs to start out with.
#Output:        fightingHealth; the health after finishing the fight
def fight(playerHealth, item, inventory):


    #-----INITIALIZE DAMAGES AND HEALTHS-----#
    enemyHealth = BASE_DEMOGORGON_HEALTH
    enemyDmg = BASE_DEMOGORGON_ATTACK
    fightingHealth = playerHealth


    #-----REDUCE DAMAGE IF DEBUFF ITEMS IN THE INVENTORY-----#
    if ITEMS[2] in inventory:
        enemyHealth = int(enemyHealth / 2)
    if ITEMS[4] in inventory:
        enemyDmg = int(enemyDmg / WALKMAN_DEBUFF)

        
    #-----FIGHTING CONTINUES UNTIL ONE PERSON DIES.-----#
    while enemyHealth > 0 and fightingHealth > 0:

        print("\n\nYour health is:", fightingHealth)
        print("The demogorgon's health is:", enemyHealth)


        displayMenu(FIGHT_MENU)
        fightChoice = getUserChoices(FIGHT_MENU)
        dmgFromItem = calcDamage(item)
        #FIGHT#
        if fightChoice == 1:

            enemyHealth -= dmgFromItem
            fightingHealth -= enemyDmg

        #FLAIL#
        if fightChoice == 2:

            fightingHealth = 0
            print("You lose the game!")

        #FLEE#
        if fightChoice == 3:
           fleeChance = randint(1, 10)
           if fleeChance <= 3:
                print("You've successfully fled!")
                enemyHealth = 0
           else:
                #HALF DAMAGE RETURNED IF FLEEING FAILS#
                fightingHealth -= int(enemyDmg / 2)
            
    return fightingHealth





 
        
def main():


    #INITIALIZE ALL INFO, SET TRENCH ACTIVATION AT 0.
    #IF PLAYER FALLS IN TRENCH, IT TURNS TO 1, MAKING THE DISTANCE
    #TRAVELLED HALF.
   
    backpack = ["Walkie Talkie", "Flashlight"]
    equippedItem = NO_EQUIPPED_ITEM
    playerHealth = MAX_PLAYER_HEALTH
    dayCount = 1
    distance = 0
    trenchActivation = 0

    #PRINT THE INTRO STATEMENTS
    printIntro()
    

    #WHILE LOOP CONTINUES UNTIL 7 DAYS OR UNTIL HEALTH IS 0.
    while dayCount < SURVIVE_DAYS and playerHealth > 0 and \
          distance <= SURVIVE_DIST:



       print("The sun rises on day", dayCount, "in the forest.\n")
       print("What would you like to do this morning?")
       
       displayMenu(DAY_MENU)
       dayAction = getUserChoices(DAY_MENU)

       #WE DON'T WANT TO UPDATE THE DAY UNTIL 4 IS SELECTED.
       while dayAction != 4:

          #VIEW INVENTORY
          if dayAction == 1:
             
              print("Here's what your inventory looks like: ")
              print(backpack)
              print("\nDo you want to equip an item?")
            
              displayMenu(EQUIP_MENU)
              equipOption = getUserChoices(EQUIP_MENU)
              if equipOption == 1:
                 displayMenu(backpack)
                 equipItem = getUserChoices(backpack)
                 equippedItem = backpack[equipItem - 1]
              elif equipOption == 2:
                 equippedItem = NO_EQUIPPED_ITEM
              elif equipOption == 3:
                 print("OK, that's fine.")

          #VIEW STATS
          if dayAction == 2:
            print("\nHealth:", playerHealth)
            print("Distance traveled:", distance)
            print("Equipped item: ", equippedItem)

          #EAT A WAFFLE
          if dayAction == 3:
             playerHealth = eat("Waffle", playerHealth)
            
          #LOOP IF THEY WANT TO DO ANYTHING ELSE
          if dayAction != 4:
            print("\nWhat else would you like to do this morning?")
            displayMenu(DAY_MENU)
            dayAction = getUserChoices(DAY_MENU)


       #DIVERGE INTO NEXT MENU IF THEY'RE DONE CHOOSING.
       if dayAction == 4:
          print("\nThe demogorgon looms in the distance. Do you leave camp, "\
                "or do you stay?")

          displayMenu(AFTER_DAY_MENU)
          travelChoice = getUserChoices(AFTER_DAY_MENU)

          #IF THEY CHOOSE TO TRAVEL
          if travelChoice == 1:
             travelEventRand = randint(1, 10)

             #RANDOM FOOD
             if travelEventRand == 1 or travelEventRand == 2:
                randFoodGen = randint(0, (len(FOODS) - 1))
                print("As you were walking, you found a backpack.")
                print("Inside the backpack, there was some: ", FOODS[randFoodGen])
                displayMenu(EAT_MENU)
                eatOption = getUserChoices(EAT_MENU)
                if eatOption == 1:
                   playerHealth += eat(FOODS[randFoodGen], playerHealth)
                   subtractedFromDist = eat(FOODS[randFoodGen], playerHealth)
                   paramToPass = playerHealth - subtractedFromDist
                else:
                   print("Your diet says no.")

             #FIND RANDOM ITEM
             if travelEventRand == 3 or travelEventRand == 4:
                randShedGen = randint(0, (len(ITEMS) - 1))
                backpack.append(ITEMS[randShedGen])
                    
                print("You pass by and old shed and decide to go inside."\
                      "Something on the shelf catches your eye.")
                print("You reach up to grab the item. It's a ",\
                      ITEMS[randShedGen])

                print("The", ITEMS[randShedGen], "has been added to your "\
                      "inventory.")


                
             #FALL INTO TRENCH
             if travelEventRand == 5 or travelEventRand == 6:
                print("You fell into a trench becuase you weren't "\
                      "paying attention to where you were stepping.")
                print("It takes you a whole extra day to climb out.")
                dayCount += 1
                trenchActivation = 1

             if travelEventRand == 1 or travelEventRand == 2:
                if trenchActivation != 1:
                   distance += distanceTraveled(paramToPass, backpack)
                else:
                   distance += (distanceTraveled(paramToPass, backpack))
             else:
                if trenchActivation != 1:
                   distance += distanceTraveled(playerHealth, backpack)
                else:
                   distance += (distanceTraveled(paramToPass, backpack) / 2)
                  
             #FIGHT
             if travelEventRand >= 7 and travelEventRand <= 9:
                playerHealth = fight(playerHealth, equippedItem, backpack)


             if travelEventRand == 10:
                print("Nothing happened.")


                
       #IF THEY CHOOSE TO STAY PUT
       if travelChoice == 2:
          fightRand = randint(1, 10)
          if fightRand <= 7:
             playerHealth = fight(playerHealth, equippedItem, backpack)
          else:
             print("You get to rest for the night.")
             


       print("\nYou have now traveled", distance)
       dayCount += 1

       
    
main()
