#Project: A Python Game - DARKNESS
#Name: Aaron Wang/ Benison Doo
#Period: 5
#Description: You wake up in the middle of nowhere, your only choice is to explore and hope to find the end, but you are encountered with monsters as you explore.
#Consitsting of three monsters:
#                           -Goblin
#                           -Skeleton
#                           -Giant Skeleton Goblin
#Code's Function: When you explore, using a a random number generater, you are encountered with an enemy, or with nothing. When a set number has been reached you are faced with the boss, it uses a list and a random number generater to have a move.
import random
import time
import sys

sys.setrecursionlimit(10000)

def Introduction():
    #Before the Game
    raw_input("PRESS ENTER TO WAKE UP\n") #HIGHLIGHT
    Name = raw_input("What is your name?\n")
    time.sleep(1)
    print ("")
    print Name,':', "Huh?"
    time.sleep(1)
    #The Beginning of the Game
    print ("NARRATOR : You wake up in complete darkness") #HIGHLIGHT
    time.sleep(1)
    print Name, ':', "Where am I?"
    time.sleep(1)
    print ("...")
    time.sleep(1)
    print "I need to get out of here"
    time.sleep(1)
    Controls() 
#main
Introduction()

def Controls():
    print 
    command = raw_input ("Enter 'help' to see the list of controls\n")
    if command == 'help':
        Help()
        Controls()
    elif command == 'EXP':
        EXP()
        Controls()
    elif command == 'explore':
        explore()
    elif command == 'quit':
        Quit()
    elif command == 'HP':
        HP()
        Controls()
    else:
        print "You didn't enter a valid control"
        Controls()
			
#Character that is created upon running the program. Limited RNG is involved in the creation of a character to ensure a fair chance for any player.
def Help(): 
	MenuControls = {
'EXP',
'HP',
'explore',
'quit',
'help',
   }
	print MenuControls
	
def HP():
    low_health = 10
    max_health = 10
    print "Health:", low_health,"/", max_health
       	
def EXP():
	#variables
    level = 1
    levelup = 5
    experience = 0
        
    print "Level:", level
    print "Experience:", experience/levelup*100,"%"
    print "Experience needed until next level:", levelup
		
def explore():
    print "You can't see through the seemingly endless darkness so you stumble forward."
    Encounter()
        
def Quit():
    print "You concede to the enemy's wrath and fall into a deep sleep"   	
    sys.exit()

def ExperienceCounter():
    while True:
        if experience >= levelup:
            print ("Congratulations, you leveled up!")
            level += 1
            experience = experience - levelup
            levelup = round(levelup * 1.5)
            max_health += 5
            low_health = max_health

#Function that dictates what happens when the user encounters an enemy
def Encounter():
    global counter
    bosscounter = 0
    bosschance = random.randint(4,6)
    chance = random.randint(1,3)

    if bosscounter == bosschance:
        print ("After the weary battles, you gaze upward to a giant skeleton goblin")
        Boss()
		
    if chance == 1:
        print ("As you explore the darkness, you encounter what seems to be a goblin.")	
	bosscounter = bosscounter + 1
	Goblin()

    elif chance == 2:
        print ("As you explore the darkness, you encounter what seems to be a skeleton.")
	bosscounter = bosscounter + 1
	Skeleton()

    elif chance == 3:
	print ("You continue along but seemn to be going in circles.")
	Controls()
	
def Goblin():
    GoblinHP = 40
    combatcommands = {
    'A) Heavy kick',
    'B) Quick jab',
    'C) Rest',
    'D) Concede',
    'E) Flee'
    }
    print combatcommands    
    
    combatcontrol = raw_input("You're in combat! What would you like to do:")
    
    while GoblinHP > 0:
    	
    	if GoblinHP <= 0:
            print "You slay the goblin and gain 3 experience"
            experience += 3
            Controls()
            
        if  low_health <=0:
            print "You concede to the enemy's wrath and fall into a deep sleep"
            sys.exit
            
        if combatcontrol == 'A':
            chance = random.randint(1,4)
            if chance == 1:
                print "You land a critical blow, dealing 8 damage"
                GoblinHP -= 8
                GoblinAttack()
            elif 2 <= chance <= 3:
                print "You land a blow, dealing 5 damage"
                GoblinHP -= 5
                GoblinAttack()
            elif chance == 4:
                print "You completely miss"
                GoblinAttack()
            
        elif combatcontrol == 'B':
            chance = random.randint(1,3)
            if chance == 1:
                print "You land a critical blow, dealing 6 damage"
                GoblinHP -= 6
                GoblinAttack()
            elif chance == 2:
                print "You land a blow, dealing 3 damage"
                GoblinHP -= 3
                GoblinAttack()
            elif chance == 3:
                print "You completely miss"
                GoblinAttack()
                
        elif combatcontrol == 'C':
            chance = random.randint(1,2)
            if chance == 1:
                print "You try to rest, but fail as the enemy disrupts your rest. You don't regain any health"
                GoblinAttack()
            elif chance == 2:
                print "You rest successfully and gain 10 health."
                low_health += 10
                GoblinAttack()
        elif combatcontrol == 'D':
            print "You concede to the enemy's wrath and fall into a deep sleep"
            sys.exit
            
        elif combatcontrol == 'E':
            chance = random.randint(1,2)
            if chance == 1:
                print "You try to flee but fail, losing 5 HP in the process"
                low_health -= 5
                GoblinAttack()
            elif chance == 2:
                print "You successfully flee"
                Controls()
        else:
            print "Please enter a correct combat function"
            Goblin()
            
def GoblinAttack():
	chance = random.randint(1,2)
	
	if chance == 1:
		print ("The goblin dealt 5 damage")
		low_health -= 5
	if chance == 2:
		print ("The enemy missed")
	Goblin()
	
def Skeleton():
    SkeletonHP = 50
    chance = random.randint(1,3)
    print "You're in combat! What would you like to do:"
    combatcommands = {
    'A) Heavy kick',
    'B) Quick jab',
    'C) Rest',
    'D) Concede',
    'E) Flee'
    }
    print combatcommands
    
    combatcontrol = raw_input("You're in combat! What would you like to do:") 
    
    while SkeletonHP > 0:
        if combatcontrol == 'A':
            chance = random.randint(1,4)
            if chance == 1:
                print "You land a critical blow, dealing 8 damage"
                SkeletonHP -= 8
            elif 2 <= chance <= 3:
                print "You land a blow, dealing 5 damage"
                SkeletonHP -= 5
            elif chance == 4:
                print "You completely miss"
        if SkeletonHP <= 0:
            print "You slay the skeleton and gain 5 experience"
            experience += 5
	    Controls()
        if  low_health <=0:
            print "You concede to the enemy's wrath and fall into a deep sleep"
            sys.exit
            
        elif combatcontrol == 'B':
            chance = random.randint(1,3)
            if chance == 1:
                print "You land a critical blow, dealing 6 damage"
                SkeletonHP -= 6
            elif chance == 2:
                print "You land a blow, dealing 3 damage"
                SkeletonHP -= 3
            elif chance == 3:
                print "You completely miss"
                
        elif combatcontrol == 'C':
            chance = random.randint(1,2)
            if chance == 1:
                print "You try to rest, but fail as the enemy disrupts your rest. You don't regain any health"
            elif chance == 2:
                print "You rest successfully and gain 10 health."

        elif combatcontrol == 'D':
            print "You concede to the enemy's wrath and fall into a deep sleep"
            sys.exit
            
        elif combatcontrol == 'E':
            chance = random.randint(1,2)
            if chance == 1:
                print "You try to flee but fail, losing 5 HP in the process"
            elif chance == 2:
                print "You successfully flee"
        else:
            print "Please enter a correct combat function"
            Skeleton()
            
        
def Boss():
    BossHP = 150
    chance = random.randint(1,3)
    bosscombatcommands = {
    'Heavy kick',
    'Quick jab',
    'Rest',
    'Concede'
    }
    print bosscombatcommands
    
    combatcontrol = raw_input("You're in combat! What would you like to do:")
    
    while BossHP > 0:
        if combatcontrol == 'A':
            chance = random.randint(1,4)
            if chance == 1:
                print "You land a critical blow, dealing 8 damage"
                BossHP -= 8
            elif 2 <= chance <= 3:
                print "You land a blow, dealing 5 damage"
                BossHP -= 5
            elif chance == 4:
                print "You completely miss"
        if BossHP <= 0:
            print "You slay the boss and win the game."
            sys.exit
        if  low_health <=0:
            print "You concede to the enemy's wrath and fall into a deep sleep"
            sys.exit
            
        elif combatcontrol == 'B':
            chance = random.randint(1,3)
            if chance == 1:
                print "You land a critical blow, dealing 6 damage"
                BossHP -= 6
            elif chance == 2:
                print "You land a blow, dealing 3 damage"
                BossHP -= 3
            elif chance == 3:
                print "You completely miss"
                
        elif combatcontrol == 'C':
            chance = random.randint(1,2)
            if chance == 1:
                print "You try to rest, but fail as the enemy disrupts your rest. You don't regain any health"
            elif chance == 2:
                print "You rest successfully and gain 10 health."

        elif combatcontrol == 'D':
            print "You concede to the enemy's wrath and fall into a deep sleep"
            sys.exit
            
        else:
            print "Please enter a correct combat function"
            Boss()
