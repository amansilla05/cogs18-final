class Character:
    """ The Character class stores information about the player and has functions to return that information to Game. """
    
    proficient = {"barbarian" : ["strength", "constitution"], "bard": ["charisma", "intelligence"], 
                  "druid" : ["intelligence", "wisdom"], "fighter" : ["strength", "dexterity"], "monk" : ["wisdom", "dexterity"], 
                  "paladin" : ["strength", "charisma"], "ranger" : ["dexterity", "wisdom"], 
                  "rogue" : ["dexterity", "intelligence"], "sorcerer" : ["constitution", "charisma"], 
                  "warlock" : ["intelligence", "charisma"], "wizard" : ["intelligence", "wisdom"]}
    

    def __init__(self, name, dnd_race, dnd_class, modifier):
        """
        This function create the variables for the character information
        """
        self.name = name
        self.dnd_race = dnd_race
        self.dnd_class = dnd_class
        self.modifier = modifier
        
    def get_name(self):
        """
        The get_name function returns the player's name.
        output: name (string)
        """
        return self.name

    
    def get_modifier(self, roll_type):
        """
        The get_modifier function determines if the player has a modifier for a specific type of roll and returns the modifier.
        output: modifier (int)
        """
        #checks if the player has a modifier for the specific type of roll
        if roll_type in Character.proficient[self.dnd_class]:
            return self.modifier
        #returns 0 if the player does not have a modifier for that roll
        return 0