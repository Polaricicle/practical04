#Filename: q1_sum_series1.py
#Author: Tan Di Sheng
#Created: 20130221
#Modified: 20130221
#Description: This program computes a series

print("This program computes a series.")

#Creates a loop so that the user can keep using the application
#without having to keep restarting the application
while True:

    def sum_series1(i):
        if i == 1:
            return 1
        else:
            return 1 / i + sum_series1(i - 1)

    while True:
        i = input("\nEnter an integer: ")
        try:
            int(i)
        except:
            print("\nPlease input an integer")
        else:
             break

    i = int(i)
    print(sum_series1(i))

    #gives the user an option to quit the application
    contorquit = input("\nContinue? Type no to quit: ")
    if contorquit == "no":
        quit()
    else:
        continue
