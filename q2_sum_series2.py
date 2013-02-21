#Filename: q2_sum_series2.py
#Author: Tan Di Sheng
#Created: 20130221
#Modified: 20130221
#Description: This program computes a series

print("This program computes a series.")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def sum_series2(i):
        if i == 1:
            return 1 / 3
        else:
            return i / (2 * i + 1) + sum_series2(i - 1)

    while True:
        i = input("\nEnter an integer: ")
        try:
            int(i)
        except:
            print("\nPlease input an integer")
        else:
             break

    i = int(i)
    print(sum_series2(i))

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
