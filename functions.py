import player_classes
import possible_stats
import random
import time
from tkinter import *
from tkinter import ttk
import random

def init_life():
    """
    creates the player you play with
    """
    gender = random.randrange(1, 3)
    life = player_classes.yourself_class(random.choice(possible_stats.possible_male_first_names) if gender == 1 else random.choice(possible_stats.possible_female_first_names), random.choice(possible_stats.possible_last_names), gender, random.randrange(70,100), random.randrange(1,100), random.randrange(1,100), 0)
    return life

def hood_init():
    """
    your socializion you will have this your entire life
    """
    return player_classes.hood(random.randrange(1, 4), random.randrange(1, 4))

def create_family(yourself):
    """
    creates you family,
    """
    #list with all members
    #mom
    mom = player_classes.npc(random.choice(possible_stats.possible_female_first_names),yourself.last_name, 2, random.randrange(20,30), random.randrange(70,100),0,random.randrange(1,5), True, True, random.randrange(1,100), random.randrange(1,100))
    #dad
    dad = player_classes.npc(random.choice(possible_stats.possible_male_first_names),yourself.last_name, 1, random.randrange(20,30), random.randrange(70,100),0,random.randrange(1,5), True, True, random.randrange(1,100), random.randrange(1,100))
    #sister/brother
    sisters = []
    brothers = []
    for x in range(random.randrange(0,3)):
        sister = player_classes.npc(random.choice(possible_stats.possible_female_first_names),yourself.last_name, 2, random.randrange(2,4), random.randrange(70,100),0,random.randrange(1,5), True, True, random.randrange(1,100), random.randrange(1,100))
        sisters.append(sister)
    for x in range(random.randrange(0,3)):
        brother = player_classes.npc(random.choice(possible_stats.possible_male_first_names),yourself.last_name, 1, random.randrange(2,4), random.randrange(70,100),0,random.randrange(1,5), True, True, random.randrange(1,100), random.randrange(1,100))
        brothers.append(brother)
    family = [sisters, brothers, mom, dad]
    return [sisters, brothers, mom, dad]

def start():
    """
    The message with your stats at the Start of the game
    """
    return(f"""
Hallo und willkommen zu Bitlife.

Deine Stats:


Deine Gesundheit:
|{(yourself.health // 5) * "█"}|{yourself.health}/100

Deine Inteligenz:
|{(yourself.iq // 5) * "█"}|{yourself.iq}/100

Dein Aussehen:
|{(yourself.looks // 5) * "█"}|{yourself.looks}/100

Dein Name ist {yourself.first_name} {yourself.last_name}. Du hast {len(family[0])} Schwester/n und {len(family[1])} Bruder/Brüder.
Deine Mutter heisst {family[2].first_name} {family[2].last_name} und dein Vater heisst {family[3].first_name} {family[3].last_name}.
Deine Familie lebt in einer {'sehr armen' if hood.save == 1 else ('normal wohlhabenden' if hood.save == 2 else 'sehr armen')} Gegend mit einem {'sehr gutem' if hood.education == 1 else ('mittelmässigen' if hood.education == 2 else 'sehr schlechtem')} Schulsystem.
    """)
    input("Enter drücken zum starten")


def say_hello():
    """
    Welcomes you to the programm and give you the option to create life or exit the game.
    """
    return ("Hallo und willkommen zu Binarylife.")

def preschool():
    '''
    Starts the events for the Preschool
    '''
    randomint = 1 #random.randrange(1,5)
    if randomint == 1:
        return("""
Dein geliebtes Haustier mit dem Namen Knuffel ist gestorben. Du bist sehr traurig.
Willst du deine Eltern auffordern ein neues zu kaufen?
""", ["Deine Eltern wollen dir kein neues Haustier kaufen.\nDu bist Traurig deswegen.\n-10 Glücklichkeit", -2, 0], ["haram"])
    elif randomint == 2:
        return("2. event")
    elif randomint == 3:
        return("3.event")
    elif randomint == 4:
        return("4.event")
    elif randomint == 5:
        return("5.event")
    
    
    
def school():
    '''
    Starts the events for the School
    '''
    randomint = random.randrange(1,5)
    if randomint == 1:
        return("erstes event")
    elif randomint == 2:
        return("2. event")
    elif randomint == 3:
        return("3.event")
    elif randomint == 4:
        return("4.event")
    elif randomint == 5:
        return("5.event")
def job():
    '''
    Starts the events for the Job
    '''
    randomint == random.randrange(1,5)
    if randomint == 1:
        return("erstes event")
    elif randomint == 2:
        return("2. event")
    elif randomint == 3:
        return("3.event")
    elif randomint == 4:
        return("4.event")
    elif randomint == 5:
        return("5.event")
def senior():
    '''
    Starts the events for the endgame(;
    '''
    randomint == random.randrange(1,5)
    if randomint == 1:
        return("erstes event")
    elif randomint == 2:
        return("2. event")
    elif randomint == 3:
        return("3.event")
    elif randomint == 4:
        return("4.event")
    elif randomint == 5:
        return("5.event")
def dead():
    '''
    you die
    '''
    pass
def next_year():
    year ++ 1
    print(year)
    if year < 6 and year > -1:
        event,yes,no = preschool()
    elif year < 17 and year > 5:
        even,yes,no = school()
    elif year < 61 and year > 15:
        event,yes,no = job()
    elif year < 81 and year > 99:
        event,yes,no = senior()
    elif year == 100:
        event = dead()
    else:
        print("error")
    return event,yes,no


yourself = init_life()
family = create_family(yourself)
hood = hood_init()
year = 0