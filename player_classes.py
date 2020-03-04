class yourself_class():
    """
    This is the class of the player you represent in the game.
    This is very important because this will lead you trew the game.
    """
    def __init__(self, first_name, last_name, gender, health, iq, looks, fame, age):
        self.first_name =   first_name
        self.last_name  =   last_name
        self.gender =   gender
        self.health =   health
        self.iq     =   iq
        self.looks  =   looks
        self.fame   =   fame
        self.age    =   age

class hood():
    """
    This is the hood the caracter lives in.
    good hood = good education
    bad hood = bad education
    good hood = save
    bad hood = unsave
    """
    def __init__(self, save, education):
        self.save   =   save
        self.education  =   education

class npc():
    """
    This are all caracters who have contact with you in the game
    """
    def __init__(self, first_name, last_name, gender, age, contact, love, money, family, alive, looks, iq):
        self.first_name =   first_name
        self.last_name  =   last_name
        self.gender     =   gender
        self.age        =   age
        self.contact    =   contact
        self.love       =   love
        self.money      =   money
        self.family     =   family
        self.alive      =   alive
        self.looks      =   looks
        self.iq         =   iq