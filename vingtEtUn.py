#
#   Eric Lesende
#
#   vingtEtUn.py
#
#
#   Menu driven interface program for a blackjack dice game where
#   the goal of the game is for the player to beat the house
#   by throwing dice and reaching a total of 21 without going over
#   The menu options are:
#                       1. See the rules
#                       2. Play Vingt-Et-Un
#                       3. Quit
#
#   The two players will take turns throwing dice as many times as desired and the program
#   will add up the totals on each round
#   A player who totals over 21 is bust and loses the game
#   The player whose total is nearest 21, after each player has had a turn, wins the game
#   In the case of an equality high total, the game is tied
#   The game is over at the end of a round when:
#                                               1. One or both players are bust
#                                               2. Both players choose to stay
#   Once a player totals 14 or more, one of the dice are dicarded for the consecutive turns
#   The house must throw the dice until the total is 17 or higher
#   At 17 or higher, the house must stay
#   Menu will work as follows:
#           1. If the user chooses 1 from the menu, display the rules
#           2. If the user chooses 2 from the menu, go into a loop of rounds where
#              player & house will take turns throwing the dice
#           3. If the user chooses 3 from the menu, display a good-bye message and quit
#   At each iteration of the loop, the system will ask the player/house whether to stay or roll
#   If the house has a running total of 17 or higher, it stays, and the turn passes to the player
#   If the player/house option is to roll, the program simulates the roll of the two dice
#   and updates & displays the player's running total
#   If the player/house starts the round with an accumulated total of 14 points or more, only one
#   die will be rolled
#   Once the game is over the system will display the result:
#       1. Winner
#       2. Loser
#       3. Tie
#   The user can play the game as many times as they wish until they choose 3 to Quit
#
#   This program will create these functions:
#       1. menu() which will display the menu
#       2. displayRules() which will display the rules
#       3. rollDice() which will roll the dice for the user and the house
#       4. playGame() which will play the game
#       5. displayResults() which will display the results of the game
#
#       Input: Ask user to input name then prompt user to select between the following options:
#           1. Display rules
#           2. Play Vingt-Et-Un
#           3. Quit
#       Processing: 1. Generate two numbers between 1-6. Add the numbers to a running total. Repeats for house.
#                   2. Following the turn, prompt user to roll or stay and add that number to running total.
#                   3. Check if running total is 14 or more then only one random number generated.
#                   4. Check if house running total is 17 or higher and stays if they are.
#                   5. Compare numbers when both user and house stay or either are at or over 21 with displayResults.
#
#       Output: Results of the game. Either Winner, Loser, or Tie.
#               Menu will display again.
#
#
#
#

#   Import the random library for the random number generator
import random
#   Define main as the main function of the program
def main():
    playerName = input('\nPlease enter your name: ')  #   Prompt user to input user name
    print(f'\nHello {playerName}.')                 #   Displays a greeting with the user's input name
    print('\nAre you ready to play Vingt-Et-Un?')   #   Displays an intro to the game
    userInput = menu()                              #   Calls the menu function to display the menu and assigns the value input by the
                                                    #   user to the variable userInput
    while True:                                     #   Initiate a while loop to execute user input 
        if userInput == '1':                        #   If statement. If user inputs 1
            displayRules()                          #   Calls the displayRules function to display the rules
            userInput = menu()                      #   Calls the menu function to display the menu and assigns the value input by the
                                                    #   user to the variable userInput
        elif userInput == '2':                      #   Continues the if statement, elif user inputs 2
            playGame(playerName)                    #   Calls the playGame function with the parameter playerName
            userInput = menu()                      #   Calls the menu function to display the menu and assigns the value input by the
                                                    #   user to the variable userInput
        elif userInput != '1' and userInput != '2' and userInput != '3':   #    Continues the if statement, elif validates the user input
            print(f'\n{userInput} is not a correct choice.')   #    If user does not input 1,2, or 3, displays the input is incorrect
            userInput = menu()      #   Calls the menu function to display the menu and assigns the value input by the
                                    #   user to the variable userInput
        else:   #   Ends the if statement with else
            print('\nThank your for playing! Goodbye.') #   If user inputs 3, display a goodbye message
            break    #   Break ends the program
def menu():  #   Defines the menu() function
    print('\nPlease choose from the following options\n') # Displays the menu and asks the user to enter
    print('\t1. See the rules.') # 1 for the rules
    print('\t2. Play Vingt-Et-Un.') # 2 to play the game
    print('\t3. Quit.')  # 3 to quit the game
    userInput = input('\nPlease make your selection: ') # Prompts user to input their selection and assigns the value to userInput
    return userInput #   Returns userInput
    
def displayRules(): #   Defines the displayRules() function
                    #   Displays the rules of the game
    print('\nVingt-et-un is a dice game (known as Blackjack in the USA), where a player competes against the computer (house).')
    print('The goal of the game is to score 21 points, or as near as possible without going over. The two players take')
    print('turns throwing two dice as many times as desired and adding up the numbers thrown on each round.\n')
    print('\t•A player who totals over 21 is bust and loses the game.')
    print('\t•The player whose total is nearest 21, after each player has had a turn, wins the game.')
    print('\t•In the case of an equality high total, the game is tied.')
    print('\nThe game is over at the end of a round when:\n')
    print('\t•One or both players are bust.')
    print('\t•Both players choose to stay.')
    print('\nOnce a player totals 14 or more, one of the die is discarded for the consecutive turns.')
    print('The house must throw the dice until the total is 17 or higher. At 17 or higher, the house must stay.\n')          
def rollDice(numDice):                                          #   Define the rollDice(numDice) function with the numDice parameter
    return sum(random.randint(1, 6) for _ in range(numDice))    #   Uses the sum of a number generated from 1-6 in the range of numDice
                                                                #   and returns the value
def playGame(playerName): #   Defines the function playGame(playerName) with the parameter playerName
    user = 0            #   Initiates the user counter to 0
    house = 0           #   Initiates the house counter to 0
    total = rollDice(2) #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable             
    user += total       #   Uses an augmented assignment operator to add the value of total to the user counter
    total = rollDice(2) #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable    
    house += total      #   Uses an augmented assignment operator to add the value of total to the house counter
    print(f'\n{playerName} rolled {user}')  #   F-string that displays what playerName rolled
    print(f'\nThe house rolled {house}')    #   F-string that displays what the house rolled
    again = input(f'\n{playerName}, would you like to roll or stay? ')  #   Prompts user to roll or stay
    while again != 'roll' and again != 'stay':      #   Initiates a while loop to validate the user input is either roll or stay
        print(f'\n{again} is an incorrect choice.') #   F-string that displays the user input is not a correct choice
        again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
    else:       #   Else statement to close the while loop when the while loop is not True, the following happens
        while again == 'stay':  #   Initiates a while loop while the string 'stay' is assigned to the variable again and the following will happen
            while house < 14:   #   Initiates a while loop while the house < 14, the following will happen
                total = rollDice(2) #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable                     
                print(f'\nHouse rolled {total}')  #   F-string that displays what the house rolled  
                house += total      #   Uses an augmented assignment operator to add the value of total to the house counter
                print(f'\nHouse new total is {house}') #   F-string displays the new house total variable
            while 14 <= house < 17:   #   Initiates while loop while 14 <= house < 17 the following will happen
                total = rollDice(1)   #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable
                print(f'\nHouse rolled {total}')   #   F-string that displays what the house rolled
                house += total                     #   Uses an augmented assignment operator to add the value of total to the house counter 
                print(f'\nHouse new total is {house}')  #   F-string displays the new house total variable
            if house >= 17:                 #   If statement if house >= 17, the following will happen
                displayResults(user, house, playerName)  #   Calls the displayResults function with the parameters user, house and playerName
                return              #   Returns the value of displayResults         
    while again == 'roll':      #   Initiates a while loop. While the string 'roll' is assigned to the variable again, the following will happen
        while user < 14 and house < 14:     #   Initiates a while. While user < 14 and house < 14, the following will happen
            total = rollDice(2)             #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable 
            print(f'\n{playerName} rolled {total}') #   F-string that displays what playerName rolled
            user += total                           #   Uses an augmented assignment operator to add the value of total to the user counter
            print(f'\nYour new total is {user}')    #   F-string that displays what the house rolled
            total = rollDice(2)                     #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable  
            print(f'\nHouse rolled {total}')        #   F-string that displays what the house rolled  
            house += total                          #   Uses an augmented assignment operator to add the value of total to the house counter
            print(f'\nHouse new total is {house}')  #   F-string displays the new house total variable
            if user >=21 or house >=21:             #   If statement. If user >= 21 or house >= 21, the following will happen
                displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                return                              #   Return the value of displayResults
            else:                                   #   Else statement if the if statement above is not True, the following happens
                again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                while again != 'roll' and again != 'stay':  #   Initiates a while loop to validate the user input is either roll or stay
                    print(f'\n{again} is an incorrect choice') #   F-string that displays the user input is not a correct choice
                    again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                else:   #   Else statement to close the while loop when the while loop is not True, the following happens
                    while again == 'stay': #   Initiates a while loop while the string 'stay' is assigned to the variable again and the following will happen
                        if house < 14:  #   Initiates an if statement. If the house < 14, the following will happen
                            total = rollDice(2) #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable 
                            print(f'\nHouse rolled {total}') #   F-string that displays what the house rolled  
                            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
                            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable
                        elif 14<= house < 17: #   Elif statement if 14 <= house < 1, the following will happen
                            total = rollDice(1) #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable
                            print(f'\nHouse rolled {total}') #   F-string that displays what the house rolled  
                            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
                            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable
                        elif house >= 17: #   Elif statement. If house >= 17, the following will happen
                            displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                            return  #   Return the value of displayResults
        while user < 14 and 14 <= house < 17: #   Initiates a while loop. While user < 14 and 14 <= house < 17, the following will happen
            total = rollDice(2) #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable
            print(f'\n{playerName} rolled {total}') #   F-string that displays what playerName rolled
            user += total #   Uses an augmented assignment operator to add the value of total to the user counter
            print(f'\nYour new total is {user}')  #   F-string that displays what the house rolled
            total = rollDice(1)  #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable  
            print(f'\nHouse rolled {total}') #   F-string that displays what the house rolled  
            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable
            if user >=21 or house >=21:  #   If statement. If user >= 21 or house >= 21, the following will happen
                displayResults(user, house, playerName)  #   Calls the displayResults function with the parameters user, house and playerName
                return #   Return the value of displayResults
            else:   #   Else statement if the if statement above is not True, the following will happen
                again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                while again != 'roll' and again != 'stay': #   Initiates a while loop to validate the user input is either roll or stay
                    print(f'\n{again} is an incorrect choice') #   F-string that displays the user input is not a correct choice
                    again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                else: #   Else statement to close the while loop when the while loop is not True, the following happens
                    while again == 'stay': #   Initiates a while loop while the string 'stay' is assigned to the variable again and the following will happen
                        if 14 <= house < 17:  #   If statement if 14 <= house < 1, the following will happen
                            total = rollDice(1) #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable 
                            print(f'\nHouse rolled {total}') #   F-string that displays what the house rolled  
                            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
                            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable
                        elif house >= 17:  #   Elif statement. If house >= 17, the following will happen
                            displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                            return #   Return the value of displayResults                     
        while user >= 14 and house < 14: #   Initiates a while loop. While user >= 14 and house < 14, the following will happen
            total = rollDice(1) #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable
            print(f'\n{playerName} rolled {total}') #   F-string that displays what playerName rolled
            user += total #   Uses an augmented assignment operator to add the value of total to the user counter
            print(f'\nYour new total is {user}') #   F-string that displays what the house rolled
            total = rollDice(2) #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable
            print(f'\nHouse rolled {total}') #   F-string displays the new house total variable
            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable
            if user >=21 or house >=21: #   If statement. If user >= 21 or house >= 21, the following will happen
                displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                return #   Return the value of displayResults      
            else: #   Else statement if the if statement above is not True, the following happens
                again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                while again != 'roll' and again != 'stay': #   Initiates a while loop to validate the user input is either roll or stay
                    print(f'\n{again} is an incorrect choice.') #   F-string that displays the user input is not a correct choice
                    again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                else: #   Else statement to close the while loop when the while loop is not True, the following happens
                    while again == 'stay': #   Initiates a while loop while the string 'stay' is assigned to the variable again and the following will happen
                        if house < 14: #   Initiates an if statement. If the house < 14, the following will happen
                            total = rollDice(2) #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable
                            print(f'\nHouse rolled {total}') #   F-string displays the new house total variable
                            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
                            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable           
                        elif 14 <= house < 17: #   Elif statement if 14 <= house < 1, the following will happen
                            total = rollDice(1) #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable
                            print(f'\nHouse rolled {total}') #   F-string displays the new house total variable
                            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
                            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable     
                        elif house >= 17:  #   Elif statement. If house >= 17, the following will happen
                            displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                            return #   Return the value of displayResults        
        while user >= 14 and 14 <= house < 17: #   Initiates a while loop. While user >= 14 and 14 <= house < 17, the following will happen
            total = rollDice(1) #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable
            print(f'\n{playerName} rolled {total}') #   F-string that displays what playerName rolled
            user += total #   Uses an augmented assignment operator to add the value of total to the user counter
            print(f'\nYour new total is {user}') #   F-string that displays what the house rolled
            total = rollDice(1) #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable
            print(f'\nHouse rolled {total}') #   F-string displays the new house total variable
            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable  
            if user >=21 or house >=21: #   If statement. If user >= 21 or house >= 21, the following will happen
                displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                return #   Return the value of displayResults 
            else: #   Else statement if the if statement above is not True, the following happens
                again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                while again != 'roll' and again != 'stay': #   Initiates a while loop to validate the user input is either roll or stay
                    print(f'\n{again} is an incorrect choice.') #   F-string that displays the user input is not a correct choice
                    again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                else: #   Else statement to close the while loop when the while loop is not True, the following happens
                    while again == 'stay': #   Initiates a while loop while the string 'stay' is assigned to the variable again and the following will happen
                        if 14 <= house < 17: #   If statement if 14 <= house < 1, the following will happen
                            total = rollDice(1) #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable
                            print(f'\nHouse rolled {total}') #   F-string displays the new house total variable
                            house += total #   Uses an augmented assignment operator to add the value of total to the house counter
                            print(f'\nHouse new total is {house}') #   F-string displays the new house total variable           
                        elif house >= 17:  #   Elif statement. If house >= 17, the following will happen
                            displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                            return #   Return the value of displayResults             
        while user < 14 and house >= 17: #   Initiates a while loop. While user >= 14 and 14 <= house < 17, the following will happen
            total = rollDice(2) #   Calls the rollDice function with 2 as numDice and assigns the returned value to total variable
            print(f'\n{playerName} rolled {total}') #   F-string that displays what playerName rolled
            user += total #   Uses an augmented assignment operator to add the value of total to the user counter
            print(f'\nYour new total is {user}') #   F-string that displays what the house rolled
            if user >=21 or house >=21: #   If statement. If user >= 21 or house >= 21, the following will happen
                displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                return #   Return the value of displayResults 
            else: #   Else statement if the if statement above is not True, the following happens
                again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                while again != 'roll' and again != 'stay': #   Initiates a while loop to validate the user input is either roll or stay
                     print(f'\n{again} is an incorrect choice.') #   F-string that displays the user input is not a correct choice
                     again = input(f'{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                else: #   Else statement to close the while loop when the while loop is not True, the following happens
                    if again == 'stay': #   Initiates an if statement. If the string 'stay' is assigned to the variable again, the following will happen
                        displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                        return #   Return the value of displayResults  
        while user >= 14 and house >= 17: #   Initiates a while loop. While user >= 14 and house >= 17, the following will happen
            total = rollDice(1) #   Calls the rollDice function with 1 as numDice and assigns the returned value to total variable
            print(f'\n{playerName} rolled {total}') #   F-string that displays what playerName rolled
            user += total #   Uses an augmented assignment operator to add the value of total to the user counter
            print(f'\nYour new total is {user}') #   F-string that displays what the house rolled
            if user >=21 or house >=21: #   If statement. If user >= 21 or house >= 21, the following will happen
                displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                return #   Return the value of displayResults   
            else: #   Else statement if the if statement above is not True, the following happens
                again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                while again != 'roll' and again != 'stay': #   Initiates a while loop to validate the user input is either roll or stay
                     print(f'\n{again} is an incorrect choice.') #   F-string that displays the user input is not a correct choice
                     again = input(f'\n{playerName}, would you like to roll or stay: ') #   F-string that prompts user playerName to roll or stay 
                else: #   Else statement to close the while loop when the while loop is not True, the following happens
                    if again == 'stay': #   Initiates an if statement. If the string 'stay' is assigned to the variable again, the following will happen
                         displayResults(user, house, playerName) #   Calls the displayResults function with the parameters user, house and playerName
                         return #   Return the value of displayResults  
def displayResults(user, house, playerName): #  Defines the function displayResults() with user, house, and playerName as parameters
    if user > 21: #  If statement. If user > 21, do the following
        print(f'\n{playerName}, you are bust. House wins!') #  F-string that displays playerName is bust and the house wins
    elif house > 21: #  Elif statement. If the above isn't True, if house > 21, do the following
        print(f'\nHouse is bust. {playerName} wins!') #  F-string that displays the house is bust and playerName won
    elif user > house: #  Elif statament. If the above isn't True, do the following
        print(f'\n{playerName} wins!') #  F-string that displays playerName wins
    elif user < house: #  Elif statement. If the above isn't True, the following happens
        print('\nHouse wins!') #  Displays the house wins
    else: #  Else statement. If none of the above is true, displays the following
        print("\nIt's a tie!") #  Displays the game ends in a tie
        
        
if __name__ == '__main__': #  If statement. Assigns '__main__' to the __name__ variable, and the following happens
    main() #  Calls the main() function
