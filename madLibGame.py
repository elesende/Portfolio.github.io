#
#   Eric Lesende
#
#   madLibGame.py
#
#   Prompts the user for data to create a madlib game and then prompts the user
#   to input yes to loop and restart the game or no to end the game and close
#   the program
#

    #Defining main function as the main function for the module
    
def main():
    while True:  # Loop to repeat the game if the user wants to play again
        # Introduction
        print("\nMadLib Game")
        print("\nPlease enter the following words to play the Mad Lib Game")

        # Data Collection
        PNOUN1 = input("A plural noun: ").strip()
        FNAME = input("A person's first name: ").strip()
        NOUN1 = input("A noun: ").strip()
        LNAME = input("A person's last name: ").strip()
        PNOUN2 = input("A second plural noun: ").strip()
        PLACE1 = input("A place: ").strip()
        PNOUN3 = input("A third plural noun: ").strip()
        print("Okay. You're about half way now. You can do it!")
        PLACE2 = input("Another place: ").strip()
        PNOUN4 = input("A fourth plural noun: ").strip()
        NOUN2 = input("A second noun: ").strip()
        ADJECTIVE1 = input("An adjective: ").strip()
        print("You're almost done. I promise.")
        ADJECTIVE2 = input("A second adjective: ").strip()
        VERB = input("A verb: ").strip()
        ADJECTIVE3 = input("A third adjective: ").strip()

        # Displays the story using f-strings to control formatting
        print("\nThe Big Game!!!")
        print(f"Hello there, sports {PNOUN1}! This is {FNAME}, talking to you from the press {NOUN1} "
              f"in {LNAME} Stadium, where 57,000 cheering {PNOUN2} take on the {PLACE2} {PNOUN4}. "
              f"Even though the {NOUN2} is shining, it's a/an {ADJECTIVE1} cold day with the temperature in the {ADJECTIVE2} 20s. "
              f"We'll be back for the opening {VERB}-off after a few words from our {ADJECTIVE3} sponsor.")

        # Input validation for playing again
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                break  # Restart the game
            elif play_again == "no":
                print("Thanks for playing!")
                return  # End the program
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

# Calling the main function
main()
        
