#
#
#   Eric Lesende
#
#   gradeSummary.py
#
#   Create a file processing program that generates a course grades summary
#   report based on the course, instructor, and student data stored in a file by creating
#   a function that will read lines and will assign them to the correct variables and format.
#   The first three lines read will be the course, then the professor, then the term. The
#   lines follwing will be students and their grades. Use that same function to process the data and give the
#   user the number of students passed, number failed, passing percent, and average grade
#   and then ask user if they would like to process another file. Create a function to round numbers to
#   the nearest whole number to eliminate any decimals. Use exception handling to catch any errors. 
#
#
#   Input: Prompt user to enter course file
#
#   Processing: 1. Correctly formats course, professor and term
#               2. Display per line the student summary report with name on left and grade on
#                  right
#               3. Use exception handling to catch file processing errors
#               4. Display no decimal points and round the numbers to the nearest whole
#                  number
#               5. Prompt user to enter y or n, and validate input, to open another file
#
#   Output: A report of the data in the file the user input
#
#   To show what this program will do enter COP1000C.txt when the program prompts the user for the name of a course file
#
def main():#   Define main as the main function of the program
    
    print('Course Grades Summary Report ...')#   Use the print function to display program title

#   Create the output file COP1000C.txt and write the data for testing the code    
    outFile = open('COP1000C.txt', 'w')
    outFile.write('COP1000C - Introduction to Python\n')
    outFile.write('Prof. Tamika Clarke\n')
    outFile.write('Spring 2021\n')
    outFile.write('Alan Anderson\n'), (f'{57:10}')
    outFile.write('57\n')
    outFile.write('Boyd Bosh\n')
    outFile.write('89\n')
    outFile.write('Carolyn Cummings\n')
    outFile.write('95\n')
    outFile.write('Dante Dobbs\n')
    outFile.write('58\n')
    outFile.write('Elizabeth Perez\n')
    outFile.write('100\n')
    outFile.write('Frank Ferguson\n')
    outFile.write('100\n')
    outFile.write('Grant Gills\n')
    outFile.write('78\n')
    outFile.write('Daniella Cava\n')
    outFile.write('100\n')
    outFile.write('Edmund Edisson\n')
    outFile.write('85\n')
    outFile.write('Faruk Fahra\n')
    outFile.write('90\n')
    outFile.write('Ginette Gould\n')
    outFile.write('75\n')
    outFile.write('Hilda Hess\n')
    outFile.write('85\n')
    outFile.write('Irina Izquierdo\n')
    outFile.write('92\n')
    outFile.write('James Jones\n')
    outFile.write('60\n')
    outFile.write('Keysha King\n')
    outFile.write('100\n')
    outFile.close()
#   Assigns the value y to the variable again
    again = 'y'   
    while again == 'y':#   Creates a condition controlled while loop
        fileName = input('\nEnter name of course file: ')#   Assigns the user input to the variable fileName
        processData(fileName)#   Use the created processData function to open the fileName variable that the user input
        again = input('Would you like to process another file (y/n)? ')#   Prompts the user to enter y/n to process
                                                                       #   another file and assigns the value to the variable again
        while again != 'y' and again != 'n':#   Creates a condition controlled while loop that validates the users input as y/n
            print(f'\n{again} is not a correct choice ... Only choose between (y/n) ')#   If the user inputs something other than y/n
                                                                                      #   the print function displays this message
            again = input('\nWould you like to process another file (y/n)? ')#   Prompts the user to enter y/n to process
                                                                             #   another file and assigns the value to the variable again
            if again == 'n':#   Creates an if statement to test if the value n is input to the variable again, breaks the program
                break       #   Break the program if the value n is input as the variable again
           
    
def customRound(number):#   Creates the function customRound with the parameter number intended to round a decimal to the nearest round number
    if number - int(number) >= 0.5:#   If statement to validate if the decimal is greater than or equal to .5 after the number is subtracted by itself  
        return int(number) + 1#   Return the number + 1 
    else:#   Else to close the if statement
        return int(number)#   Return the number as is
    
def processData(fileName):#   Creates the function processData with the parameter fileName intended to process the file name input by the user
    try:#   Creates an exception handler try/except statement intended to catch any errors input by the user
        with open(fileName, 'r') as inFile:#   Creates a with statement to open and read fileName as the file variable inFile and closes it after its done
            courseInfo = inFile.readline().rstrip('\n')#   Reads the first line and strips \n and sets the line to the variable courseInfo
            profName = inFile.readline().rstrip('\n')#   Reads the next line and strips \n and sets the line to the variable profName
            term = inFile.readline().rstrip('\n')#   Reads the next line and strips \n and sets the line to the variable term
            totalGrades = 0#   totalGrades variable is set to 0
            numPassed = 0#   numPassed variable is set to 0
            numStudents = 0#   numStudents variable is set to 0
            studentReport = ''#   studentReport variable is set to an empty string
            studentName = inFile.readline().rstrip('\n')#   Reads the next line and strips \n and sets the line to the variable studentName
            while studentName != '':#   Creates a while conditional loop. As long as studentName is not assigned an empty string, do the following
                studentGrade = customRound(float(inFile.readline().rstrip('\n')))#   Reads the next line and strips \n. Converts the line into an integer then
                                                                                 #   uses the customRound function to test the integer and sets the value to
                                                                                 #   the variable studentGrade
                totalGrades += studentGrade#   Uses an augmented assign operator to add studentGrade to totalGrades count 
                numStudents += 1#  Uses an augmented operator to add 1 to numStudents count 
                if studentGrade >= 60:#   Creates an if statement to validate if the studentGrade variable is greater than or equal to 60
                    numPassed += 1#   Uses an augmented operator to add 1 to numPassed count
                studentReport += f'{studentName:<30} {studentGrade:>5}\n'#   Use an f string to format studentName and studentGrade and use
                                                                         #   an augmented operator to add it to studentReport list
                studentName = inFile.readline().rstrip('\n')#   Reads the next line and strips \n and sets the line to the variable studentName.
                                                            #   Continues the while statement until studentName is assigned empty string
            passingPercent = customRound((numPassed / numStudents) * 100)#   Divides numPassed by numStudents and multiplies the product by 100
                                                                         #   then uses the customRound function to validate the decimal and assigns
                                                                         #   the value to the variable passingPercent
            averageGrade = customRound((totalGrades / numStudents))#   Divides totalGrades by numStudents and then uses the customRound function to
                                                                   #   validate the decimal and assigns the value to the variable averageGrade  
            print('\n------------------------------------------------------------')#   
            print('          Broward College Grades Summary          ')            #   Uses print function to display grade summary header 
            print('------------------------------------------------------------\n')#
            print(courseInfo)#   Uses print function to display courseInfo
            print(f'Professor: {profName}             Term: {term}\n')#   Uses an f string to format profName and term and use print function to display
            print('Student Name                    Grade   ')#   Uses print function to label columns that will display the studentReport
            print('----------------------------------------')#
            print(studentReport)#   Uses print function to display studentReport
            print("Students' Performance")#   Uses print function to display students performance
            print('----------------------------------------')
            print(f'Passed: {numPassed:<15} Failed: {numStudents - numPassed:<5}')#   Uses an f string to format passed and failed students
            print(f'Passing Percent: {passingPercent}%')#   Uses an f string to format passingPercent
            print(f'Average Grade: {averageGrade}\n')#   Uses an f string to format averageGrade
    except FileNotFoundError:#   Uses the except statement to handle any FileNotFOundErrors
        print(f'Error ... {fileName} file not found.\n')#   Uses an f string to format the error message if the fileName is set to a file not
                                                        #   contained in the program then uses the print function to display the message
    except IOError:#   Uses the except statement to handle any IOErrors
        print(f'Error ... {fileName} file not found.\n')#   Uses an f string to format the error message and uses the print function to display the message











                    
if __name__ == '__main__':#   If statement to call the main function only if the file is being run as a standalone program
    main()#   Calling the main function
