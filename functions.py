import player_classes
import possible_stats
import random
import time
from tkinter import *
from tkinter import ttk
def menü(yourself):
    print("""
Was willst du tun?
1   |   Karriere
2   |   Aktivitäten
3   |   Personen
4   |   Besitztümer/Tiere

Nur Enter = nächstes Jahr
""")
    selection = input("--->")
    if selection == "":
        next_year()
    elif selection == "1":
        career(yourself)
    elif selection == "2":
        activities(yourself)
    elif selection == "3":
        people(yourself)
    elif selection == "4":
        prop(yourself)
    else:
        print("Du hast etwas falsches eingegeben!")
        menü()

def init_life():
    """
    creates the player you play with
    """
    gender = random.randrange(1, 3)
    life = player_classes.yourself_class(random.choice(possible_stats.possible_male_first_names) if gender == 1 else random.choice(possible_stats.possible_female_first_names), random.choice(possible_stats.possible_last_names), gender, random.randrange(70,100), random.randrange(1,100), random.randrange(1,100), 0, 0, None, None)
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
    print(family)
    return [sisters, brothers, mom, dad]
def next_year(yourself):
    pass
def people(yourself): 
    pass
def activities(yourself):
    pass
def career(yourself):
    print(yourself.school)
    if yourself.school == None:
        pass
    else:
        pass
    if yourself.work == None:
        pass
    else:
        pass

def start():
    yourself = init_life()
    print(yourself)
    family = create_family(yourself)
    hood = hood_init()
    print(f"""
Hallo und willkommen zu Bitlife.

Deine Stats:


Deine Gesundheit:
|{(yourself.health // 5) * "█"}|{yourself.health}/100

Deine Inteligenz:
|{(yourself.iq // 5) * "█"}|{yourself.iq}/100

Dein Aussehen:
|{(yourself.looks // 5) * "█"}|{yourself.looks}/100
  """)
    time.sleep(3)
    print(f"""
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

if __name__ == "__main__":
    say_hello()
