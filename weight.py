#
#    Eric Lesende
#
#    weight.py
#
#    Prompt user to choose one of three options from a menu that displays either:
#       1.Display "10 ways to cut 500 calories" guideline.
#       2.Generate next semester expected weight table.
#       3.Quit.
#
#    If user chooses 1. Display the following: Try these 10 ways to cut 500 calories every day
#    Then display the following as a list wih a * before it: Swap your snack,
#    Cut one high-calorie treat, DO NOT drink your calories, Skip seconds,
#    Make low calorie substitutions, Ask for a doggie bag, Just sat "no" to fried food,
#    Build a thinner pizza, Use a smaller plate, Avoid alcohol
#    
#    If user chooses 2. Prompt user to enter weight. Validate weight input by >=100
#    Generate a table with month in the left column and weight in the right column. Month would
#    increase by 1 month each row until it reaches 6 months and weight would decrease by 4 each row.
#    If user enters a weight that is <100 print Error ... Invalid weight. Try Again
#
#    If user chooses 3. Display Good Bye ... and the program ends
#
#    If user chooses anything other than 1, 2, or 3, Display an Error message and reprint menu
#
#    After user enters 1 or 2 and the corresponding information is displayed, reprint the menu until
#    user chooses 3 to quit out and end program
#
#
#    Input:  Prompt user to define variable menuInput as either 1, 2, or 3 and if user chooses 2 ask user to define variable weight
#
#    Processing: After user defines variable weight, subtract 4 pounds from weight for every month, for 6 months
#                using the augmented assignment operator weight-=4
#
#    Output: Display a table showing 1-6 months in the left column and a subtraction of 4 pounds from the weight for each corresponding
#            month with a count controlled for loop in range (1, 7)
#
#    Please see comments for more information on what each section and block will do
#
#



#    Defining main function as the main function of the module

def main():

#    Will display introduction to program menu and asks user to input either 1, 2 or 3 

        print('500 Less a Day Makes the Weight Go Away ...')
        print('\nChoose one of the following options:')
        print('\t1. Display "10 ways to cut 500 calories" guideline.')
        print('\t2. Generate next semester expected weight table.')
        print('\t3. Quit')

        menuInput=int(input('Option: ')) #    Defines the variable menuIpnut by asking user to input their choice between option 1, 2, or 3

        while True: #    Creates a condition-controlled while loop using a Boolean value of True

            if menuInput==1:  #    Begins the if elif else decision structure block. If user enters 1 the following information is displayed
       
                print('\nTry these 10 ways to cut 500 calories every day.') #     Displays this information if user defines variable menuInput as 1
                print('\t* Swap your snack.')
                print('\t* Cut one high-calorie treat.')
                print('\t* DO NOT drink your calories.')
                print('\t* Make low calorie substitutions.')
                print('\t* Ask for a doggie bag.')
                print('\t* Just say "no" to fried food.')
                print('\t* Build a thinner pizza.')
                print('\t* Use a smaller plate.')
                print('\t* Avoid alcohol.')
                print('Source: US National Library of Medicine')
                print('\nChoose one of the following options:') #    Asks user again to enter either 1, 2, or 3
                print('\t1. Display "10 ways to cut 500 calories" guideline.')
                print('\t2. Generate next semester expected weight table.')
                print('\t3. Quit')
                menuInput=int(input('Option: ')) #    Defines the variable menuInput by asking user to input their choice between option 1, 2, or 3

            elif menuInput==2: #    Elif user enters 2 user is prompted to define variable weight
                print()
                weight=int(input('Please enter starting weight in pounds (>=100): ')) # Asks user for weight to validate variable weight is >= 100

                if weight<100: #    Begins nested if elif validation loop, if variable weight is < 100, displays an error message
                               #    and asks user to once again enter weight >= 100 
                    print('\tError ... Invalid weight. Try Again') #    Displays error message

                elif weight>=100: #    Elif variable weight is >= 100, display a table with month and weight 
                    print('-----------------')
                    print('Month\tWeight') #    Displays heading of month/weight table
                    print('-----------------')
                    for month in range(1, 7): #    Begins a nested count controlled for loop. Range starts at 1 and ends at 6
                        weight-=4 #    Augmented assignment operator that subtracts 4 pounds from the users input weight for each month
                        print(f'{month:3}\t{weight} lb.') #    Displays table with 1-6 months on the left column and the corresponding
                                                          #    weight loss for those 1-6 months on the right column and uses an f string to
                                                          #    format the information

                    print('\nChoose one of the following options:') #    Asks user again to enter either 1, 2, or 3
                    print('\t1. Display "10 ways to cut 500 calories" guideline.')
                    print('\t2. Generate next semester expected weight table.')
                    print('\t3. Quit')
                    menuInput=int(input('Option: ')) #    Defines the variable menuInput by asking user to input their choice between option 1, 2, or 3

            elif menuInput<=0 or menuInput>=4: #    Elif validation loop, elif menuInput variable entered by user is <=0 or >=4, an error is displayed
                                               #    and user is once again asked to enter either 1, 2, or 3 as their option
                print('\nError ... Invalid option. Try Again') #    Displays error message
                print('\nChoose one of the following options:') #    Asks user again to enter either 1, 2, or 3
                print('\t1. Display "10 ways to cut 500 calories" guideline.')
                print('\t2. Generate next semester expected weight table.')
                print('\t3. Quit')
                menuInput=int(input('Option: ')) #    Defines the variable menuInput by asking user to input their choice between options 1, 2, or 3

            else: #    Ends the if elif else decision structure block. Else user enters 3, display Goodbye and end program
                print('\nGoodbye ...') #    Displays Goodbye
                break                  #    Breaks the while True statement and prevents an infinte loop when user enters 3 as their choice

main() #    Calling the main function
