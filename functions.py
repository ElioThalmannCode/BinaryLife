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
    life = player_classes.yourself_class(random.choice(possible_stats.possible_male_first_names) if gender == 1 else random.choice(possible_stats.possible_female_first_names), random.choice(possible_stats.possible_last_names), gender, random.randrange(70,100), random.randrange(1,100), random.randrange(1,100), random.randrange(50,100))
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

Deine Glücklichkeit:
|{(yourself.happy // 5) * "█"}|{yourself.happy}/100

Dein Name ist {yourself.first_name} {yourself.last_name}. Du hast {len(family[0])} Schwester/n und {len(family[1])} Bruder/Brüder.
Deine Mutter heisst {family[2].first_name} {family[2].last_name} und dein Vater heisst {family[3].first_name} {family[3].last_name}.
Deine Familie lebt in einer {'sehr armen' if hood.save == 1 else ('normal wohlhabenden' if hood.save == 2 else 'sehr armen')} Gegend mit einem {'sehr gutem' if hood.education == 1 else ('mittelmässigen' if hood.education == 2 else 'sehr schlechtem')} Schulsystem.
    """)

def update():
    """
    Shows your Stats
    """
    return(f"""
    Deine Gesundheit:
|{(yourself.health // 5) * "█"}|{yourself.health}/100

Deine Inteligenz:
|{(yourself.iq // 5) * "█"}|{yourself.iq}/100

Dein Aussehen:
|{(yourself.looks // 5) * "█"}|{yourself.looks}/100

Deine Glücklichkeit:
|{(yourself.happy // 5) * "█"}|{yourself.happy}/100
""")


def say_hello():
    """
    Welcomes you to the programm and give you the option to create life or exit the game.
    """
    return ("Hallo und willkommen zu Binarylife.")

def preschool():
    '''
    Starts the events for the Preschool
    '''
    randomint = random.randrange(1,5)
    if randomint == 1:
        return("Dein geliebtes Haustier mit dem Namen Knuffel ist gestorben. Du bist sehr traurig.\nWillst du deine Eltern auffordern ein neues zu kaufen?", ["Deine Eltern wollen dir kein neues Haustier kaufen.\nDu bist Traurig deswegen.\n-10 Glücklichkeit", -10, 0,0], ["Du bist für einen Moment Traurig.\n -5 Glücklichkeit", -5,0,0])
    elif randomint == 2:
        return("Das Nachbarskind will mit dir Spielen, machst du mit?", ["Das Nachbarskind ist sehr Grob zu dir aber es hat Spass gemacht.\n-10 Gesundheit\n+20 Glücklichkeit", 20,-10,0], ["Du sagst dem Nachbarskind nein und es geht. Nichts passiert",0,0,0])
    elif randomint == 3:
        return("Deine Mutter gibt dir Essen das dir nicht schmeckt.\nIsst du es deiner Mutter zuliebe?",["Du hast es gegessen.",0,0,0],["Du hast es nicht gegessen. Das hat deine Mutter nicht gerne gesehen.",0,0,0])
    elif randomint == 4:
        return("Du hast starken Husten.Fragst du deine Mutter ob du zum Arzt darfst?",["Du hattest etwas Schlimmes. Zum Glück konnte der Arzt dur Helfen.\n+20Gesundheit",0,20,0],["Du hattest etwas Schlimmes, bist aber nicht zum Arzt.\n-20 Gesundheit",0,-20,0])
    
    
def school():
    '''
    Starts the events for the School
    '''
    randomint = random.randrange(1,4)
    if randomint == 1:
        return("Du hast eine schlechte Note erhalten zeigst du sie deiner Mutter?",["Deine Mutter meldet dich für Nachhilfe an.\n+10 Inteligenz",0,0,10],["Du musst das Jahr wiederholen. Weil du nichts gegen deine Matheschwäche gemacht hast musst du ein Jahr wiederholen.\n120 Inteligenz",0,0,-20])
    elif randomint == 2:
        return("Ein paar Kolegen wollen ins Kino, gehst du mit?",["Du gehst mit und Langweilst dich.\n-10 Glücklichkeit",-10,0,0],["Du bleibst Zuhause."],0,0,0)
    elif randomint == 3:
        return("Du hast Stress mit einem Kolegen.\nEndschuldigst du dich?",["Du hast dich Versöhnt.\n+10 Glücklichkeit",10,0,0],["Du hast einen Freund verloren.\n-10 Glücklichkeit",-10,0,0])


def job():
    '''
    Starts the events for the Job
    '''
    randomint == random.randrange(1,4)
    if randomint == 1:
        return("Du wurdest bei der Arbeit gefeuert. Willst du Rache am Chef nehmen?\n",["Du verhälst dich erwachsen und nimmst keine Rache am Chef.",0,0,0],["Du wirst von deinem chef beim zerstechen von seinen Reifen erwischt. Du kriegst eine Anzeige.",0,0,0])
    elif randomint == 2:
        return("Du triffst eine hübsche Frau in der Stadt.\nWillst du sie ansprechen?",["Du sprichst die Frau an. Doch sie antwortet nicht stattessen kommt ihr Freund und gibt dir einen Schlag ins Gesicht.\n-10 Gesundheit.",0,-10,0],["Du läufst nur an ihr vorbei.",0,0,0])
    elif randomint == 3:
        return("Du triffst eine hübsche Frau in der Stadt.\nWillst du sie ansprechen?",["Du hast die Frau angesprochen und die Nummer bekommen\n+10 Glücklichkeit.",10,0,0],["Du läufst nur an ihr vorbei.",0,0,0])

def dead():
    '''
    you die
    '''
    return("Du bist Gestorben. Hat dir den Leben gefallen?",["Du hast 81 Jahre überlebt.",0,-1000,0],["Du hast 81 Jahre überlebt.",0,-1000,0])
def next_year():
    if year < 6 and year > -1:
        event,yes,no = preschool()
    elif year < 17 and year > 5:
        even,yes,no = school()
    elif year < 61 and year > 15:
        event,yes,no = job()
    elif year == 81:
        event = dead()
    else:
        print("error")
    return event,yes,no


yourself = init_life()
family = create_family(yourself)
hood = hood_init()
year = 0