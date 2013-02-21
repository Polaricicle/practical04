#Filename: q4_print_reverse.py
#Author: Tan Di Sheng
#Created: 20130221
#Modified: 20130221
#Description: This program writes a function that reverses the digits
#of an integer

print("""This program writes a function that reverses the digits
of an integer.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def reverse_int(n):
        if n == 0:
            return ""
        else:
            return str(n % 10) + str(reverse_int(int(n / 10)))
 

    while True:
        n = input("\nEnter an integer: ")
        try:
            int(n)
        except:
            print("\nPlease input an integer")
        else:
             break

    n = int(n)
    print(reverse_int(n))

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
