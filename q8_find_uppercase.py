#Filename: q8_find_uppercase.py
#Author: Tan Di Sheng
#Created: 20130221
#Modified: 20130221
#Description: This program writes a function that returns the number of
#uppercase letters in a string

print("""This program writes a function that returns the number of
uppercase letters in a string.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def find_num_uppercase(string):
        if len(string) == 1:
            if 64 < ord(string) < 91:
                return 1
            else:
                return 0
        else:
            if 64 < ord(string[0]) < 91:
                return 1 + find_num_uppercase(string[1:])
            else:
                return 0 + find_num_uppercase(string[1:])
 

    string = input("\nPlease input string here: ")

    print("The number of uppercase letters is " + str(find_num_uppercase(string)))

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
