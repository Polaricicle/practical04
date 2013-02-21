#Filename: q7_find_largest.py
#Author: Tan Di Sheng
#Created: 20130221
#Modified: 20130221
#Description: This program writes a function that returns the largest
#integer in an array

print("""This program writes a function that returns the largest
integer in an array.""")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def find_largest(alist):
        if len(alist) == 1:
            return alist[0]
        elif len(alist) == 2:
            if alist[0] > alist[1]:
                return alist[0]
            else:
                return alist[1]
        else:
            if alist[0] > alist[1]:
                alist[1] = alist[0]
            return find_largest(alist[1:])
 

    while True:
        n = input("\nEnter number of integers to be put in list: ")
        try:
            int(n)
        except:
            print("\nPlease input an integer")
        else:
             break

    alist = []
    n = int(n)
    for i in range (1, n + 1):
        a = input("Enter integer to be put in list: ")
        alist.append(a)

    print(find_largest(alist))

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
