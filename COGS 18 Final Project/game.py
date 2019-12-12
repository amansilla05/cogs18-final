from character import Character 
import random
import string
from webbrowser import open_new
from time import sleep

class Game:
    """ 
    The game class contains all the lists and functions needed to run the main game method of play().
    """  
    
    #create fields
    def __init__(self):
        """
        This function creates lists to be used for checks or responses in the Game class.
        """
        self.greeting = ["Hello!", "Hi!", "Hey!", "Welcome!", "Greetings!"]
        self.valid_races = ["dwarf", "elf", "halfling", "human", "dragonborn", "gnome", "half elf", "half orc", "tiefling"]
        self.valid_classes = ["barbarian","bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue",
                              "sorcerer","warlock", "wizard"]
        self.game_response = ["roll", "more information", "more info", "get more information", "get more info", "information",
                              "info", "quit"]
        self.valid_rolls = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        self.bad_roll = ["oof.", "That sucks...", "Better luck next time!", "Nice try!", "Yikes."]
        self.okay_roll = ["Not bad.", "Okay!", "Could be better. Could be worse.", "¯\_(ツ)_/¯", "You tried!", "So close..."]
        self.good_roll = ["Whoo!!", "Good job!", "You're doing great, sweetie!", "Epic Success!", "Yay!", "NICE!"]
        self.crit_fail = ["Critical Failure!"]
        self.crit_hit = ["Critical Hit!"]
              
    def remove_punctuation(self, input_string):
        """
        The remove_punctuation function removes all punctuation from an input string
        Taken from Assignment 3.
        """
        out_string = ""
        for char in input_string:
            if char not in string.punctuation:
                out_string += char
        return out_string
    
    def prepare_text(self, input_string):
        """
        The prepare_text function prepares the inputs for processing.
        Uses string methods as well as remove_punctuation().
        functions: remove_punctuation(), lower()
        
        Taken and slightly modified from Assignment 3.
        """
        out_string = self.remove_punctuation(input_string.lower())
        return out_string
    
    #taken from A3 and modified 
    def selector(self, number, rng, return_list):
        """
        The selector function chooses a response for the chatbot after the player rolls.
        functions: random.choice()
        inputs: number(int), rng(range), return_list(list)
        output: output(string)
        Modified from the selector function in Assignment 3: somewhat original code.
        """
        output = None
        if number in rng:
            output = random.choice(return_list)
        return output
    
    #initializes Character object by askings questions to user  
    def character_questions(self):
        """
        The character_questions function creates a Character object by asking questions to the player and saving the input.
        functions: prepare_text(), input(), random.choice()
        input: player input
        output: strings
        
        used https://www.w3schools.com/python/python_try_except.asp for reference.
        """
        
        #ask for Player's name
        print("DUNGEON MASTER: \t" + random.choice(self.greeting))
        print("DUNGEON MASTER: \tWhat is your name?")
        name = input()
        print("DUNGEON MASTER: \tNice to meet you, " + name)
        
        #ask for Player's DND race 
        print("DUNGEON MASTER: \tWhat is your race?")
        dnd_race = self.prepare_text(input())
        
        #checks that the input is a DND race
        while dnd_race not in self.valid_races:
            self.more_info("races")
            print("DUNGEON MASTER: \tWhat is your race?")
            dnd_race = self.prepare_text(input())
            
        #ask for Player's dnd class
        print("DUNGEON MASTER: \tWhat is your class?")
        dnd_class = self.prepare_text(input())
   
        #checks that the input is a DND class
        while dnd_class not in self.valid_classes:
            self.more_info("classes")
            print("DUNGEON MASTER: \tWhat is your class?")
            dnd_class = self.prepare_text(input())
            
        #ask for Player's roll modifier
        print("DUNGEON MASTER: \tWhat is your modifier?")
        input_str = self.prepare_text(input("PLAYER: \t"))
        
        #checks that the roll modifier is an int and within the appropriate range (less than 5)
        try:
            modifier = int(input_str)
            if modifier > 5:
                raise ValueError
        except ValueError:
            while type(modifier) is not int or modifier > 5:
                print("DUNGEON MASTER: \tThe modifier must be a number less than five.")
                print("DUNGEON MASTER: \tWhat is your modifier?")
                input_str = self.prepare_text(input("PLAYER: \t"))
                try: 
                    modifier = int(input_str)
                except ValueError:
                    modifier = ""
       
        #creates the Character object from inputs
        return Character(name, dnd_race, dnd_class, modifier)
    
    
    def more_info(self, topic):
        """
        The more_info function gives the user more information about DND races and class. It also gives the user a link for
        information about basic DND rules.
        function: input()
        input: player input
        output: strings
        """
        #asks user if they would like more information
        print("DUNGEON MASTER: \tDo you need more information? [Y/N]")
        response = self.prepare_text(input()) 
        
        #checks user response
        if response == "yes" or response == "y":
            
            #checks the type of information the user wants
            if topic == "classes":
                print("DUNGEON MASTER: \tThe DND classes are: ", end = "")
                for cls in self.valid_classes:
                    print (cls, end = ", ")
                print("")
            elif topic == "races":
                print("DUNGEON MASTER: \tThe DND races are: ", end = "")
                for rcs in self.valid_races:
                    print(rcs, end = ", ")
                print("")
            elif topic == "rules":
                print("DUNGEON MASTER: \tGo to: https://dnd.wizards.com/products/tabletop/players-basic-rules/SS")
    
    
    def game_question(self, character):
        """
        The game question function asks the player what action they would like to do. 
        functions: prepare_text()  and get_name()
        input: player input
        output: response (string)
        """
        print("DUNGEON MASTER: \t" + character.get_name() + ", would you like to [roll], get [more information], or [quit]?")
        response = self.prepare_text(input("PLAYER: \t"))
        
        #check if the player inputs an invalid response and asks again
        while response not in self.game_response:
            print("DUNGEON MASTER: \tSorry, I cannot do that.")
            print("DUNGEON MASTER: \tWould you like to [roll], get [more information], or [quit]?")
            response = self.prepare_text(input("PLAYER: \t"))
        return response
        
    def roll_dice(self):
        """
        The roll_dice function simulate rolling a D20 dice
        functions: randrange(), sleep()
        
        sleep() function taken from: https://www.programiz.com/python-programming/time/sleep
        """
        #loop to simulate how many times the dice rolls 
        for i in range(0, 20):
            
            #generate and print a random number between 1 and 20
            number = random.randrange(1, 21)
            print(number, end = "")
            
            #pauses the "roll" for 0.25 seconds in order to see the number
            sleep(0.25)
            
            #deletes the number until the "roll" has stopped
            if number < 10:
                print("\b \b", end = "")
            else:
                print("\b\b  \b\b", end = "")
        
        #generate and print a random number 1-20 for the outcome of the "roll"
        number = random.randrange(1, 21)
        print(number)
        
        #save roll outcome for future use
        return number

    #let the games begin
    def start_game(self, character):
        """
        The start_game function asks the player if they are ready to play.
        functions: prepare_text(), input(), get_name()
        inputs: player input
        outputs: boolean, strings
        """
        #asks user if they are ready to play
        print("DUNGEON MASTER: \tAre you ready to play, " + character.get_name() + " ? [Y/N]")
        response = self.prepare_text(input('Player: \t'))
        
        #returns a True boolean if ready
        if response == "yes" or response == "y":
            return True
        
        #tells the user to come back when ready and returns False boolean if not ready
        else:
            print("DUNGEON MASTER: \tCome back when you are ready!")
            return False
        
    def play(self):
        """ Play is the main function to run the chatbot.
            Inspired by the have_a_chat function in Assignment 3, but is almost all original code.
            functions: character_questions(), start_game(), game_question(), roll_dice(), get_modifier(), selector(),
            more_info(), input(), range()
            inputs: player input
            outputs: mod, roll, out_msg
        """
        #assigns player as a character object
        player = self.character_questions()
    
        #play is the boolean result from start_game()
        play = self.start_game(player)
        while play:
            
            out_msg = None
            
            #Determine what the player would like to do:
            response = self.game_question(player)             
            
            #checks for end message
            if response == "quit":
                print("Dungeon Master: \tSee you next session, " + player.get_name() + "!")
                play = False
            
            #checks for roll action    
            elif response == "roll":
                print("DUNGEON MASTER: \t" + player.get_name() + ", what would you like to roll for?")
                response = self.prepare_text(input("PLAYER: \t"))
            
                #check that the action is valid
                while response not in self.valid_rolls:
                    print("DUNGEON MASTER: \tYou cannot roll for that")
                    print("DUNGEON MASTER: \t" + player.get_name() + ", what would you like to roll for?")
                    response = self.prepare_text(input("PLAYER: \t"))
            
                roll = self.roll_dice()
                
                #checks for the modifier of the player
                mod = player.get_modifier(response)
                print("Modifier = " + str(mod))
                
                #adds the modifier to the roll if the player has one
                roll += mod
                print("Total roll = " + str(roll))
            
                # Check for outcome of roll and give appropriate response to it
               
                #respond to a roll of one (1)
                out_msg = self.selector(roll, range(1,1), self.crit_fail)
            
                #respond to a bad roll
                if not out_msg:
                    out_msg = self.selector(roll, range(2,8), self.bad_roll)
            
                #respond to an okay roll
                if not out_msg:
                    out_msg = self.selector(roll, range(8,14), self.okay_roll)
            
                #respond to a good roll
                if not out_msg:
                    out_msg = self.selector(roll, range(14,20), self.good_roll)
            
                #respond to a roll of twenty (20)
                if not out_msg:
                    out_msg = self.selector(roll, range(20,20), self.crit_hit)

                print('DUNGEON MASTER: \t', out_msg)
           
            #gives more information to user about the rules
            else:
                self.more_info("rules")