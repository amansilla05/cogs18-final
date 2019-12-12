import pytest

def get_name(self):
    #returns the player's name
    return self.name

    assert player_name == self.name
    

    
    def roll_dice(self):
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
    
        assert roll >= 1 and roll <=20
    
    