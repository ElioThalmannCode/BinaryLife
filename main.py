import player_classes
import possible_stats
import random


def init_life():
    """
    creates the player you play with
    """
    gender = random.randrange(1, 3)
    life = player_classes.yourself_class(random.choice(possible_stats.possible_male_first_names) if gender == 1 else random.choice(possible_stats.possible_female_first_names), random.choice(possible_stats.possible_last_names), gender, random.randrange(70,100), random.randrange(1,100), random.randrange(1,100), 0, 0)
    return life

def socialization_birth():
    """
    your socializion you will have this your entire life
    """
    hood = player_classes.hood(random.randrange(1, 5), random.randrange(1, 5))
    friends

def create_family(yourself):
    """
    creates you family,
    """
    #list with all members
    family = []
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
    return sisters, brothers


def start():
    yourself = init_life()
    print(yourself)
    sisters, brothers = create_family(yourself)
    print(sisters, brothers)
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

def main():
    """
    Welcomes you to the programm and give you the option to create life or exit the game.
    """
    print("Hallo und willkommen zu Binarylife.")
    start()

if __name__ == "__main__":
    main()

