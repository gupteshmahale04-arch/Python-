# Mini Project - Countdown Timer (with 1-second gap)
# Goal:
# brint a countdown before something "exciting" happens (like "Launching ... " or
# "Happy New Year!").
# Concepts Used: for loop, range( ), and the time module.
# Mini Project - Multiplication Table
# Goal: Print the multiplication table of a number using a loop.
# Sample Run:
# Enter a number: 5
# 5×1 = 5
# 5 × 2 = 10
# 5 × 10 = 50
# Mini Project - Guess the Number Game
# Concepts Used: while loop and user input.
# Sample Run:
# Guess a number between 1 and 10: 4

#            Count - Doun  Timer
import time
Count=int(input("Enter the no. of counter"))
print(" /n Cuntdown Start Now : ")
for i in range(Count,0,-1):
    print(i)
    
    time.sleep(1)
    
    print ("\n WOHOO ! Happy New Year ")
