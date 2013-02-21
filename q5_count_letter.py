#Filename: q5_count_letter.py
#Author: Tan Di Sheng
#Created: 20130221
#Modified: 20130221
#Description: This program finds the number of occurrences of a
#specified letter in a string

print("""This program finds the number of occurrences of
a specified letter in a string.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def count_letter(string, ch):
        if len(string) == 1 and string == ch:
            return 1
        elif len(string) == 1 and string != ch:
            return 0
        else:
            #Checks the start of the string to see if it is the same as
            #the character to be searched for. If it is not, False is returned
            #and the first letter is taken away from the string and put through
            #the function again
            return (string[0] == ch) + count_letter(string[1:], ch)
 
    string = input("Please input string here: ")
    ch = input("Please input letter to search for here: ")

    print(count_letter(string, ch))
    
    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
