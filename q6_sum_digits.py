#Filename: q6_sum_digits.py
#Author: Tan Di Sheng
#Created: 20130221
#Modified: 20130221
#Description: This program writes a function that sums up the digits
#of an integer

print("""This program writes a function that sums up the digits
of an integer.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def sum_digits(n):
        if n == 0:
            return n
        else:
            return (n % 10) + sum_digits(int(n / 10))
 

    while True:
        n = input("\nEnter an integer: ")
        try:
            int(n)
        except:
            print("\nPlease input an integer")
        else:
             break

    n = int(n)
    print(sum_digits(n))

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
