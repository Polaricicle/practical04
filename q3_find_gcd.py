#Filename: q3_find_gcd.py
#Author: Tan Di Sheng
#Created: 20130221
#Modified: 20130221
#Description: This program finds the greatest common divisor of two positive
#integers

print("""This program finds the greatest common divisor of two positive
integers.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def gcd(m, n):
        if m % n == 0:
            return n
        else:
            return gcd(n, m % n)

    while True:
        m = input("\nEnter the first integer: ")
        n = input("Enter the second integer: ")
        try:
            int(m) and int(n)
        except:
            print("\nPlease input an integer")
        else:
             break

    m = int(m)
    n = int(n)
    print(gcd(m, n))

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
