
# Print -20 to and including 50. Use any loop you want.

x = range(-20, 51)
for idx in x:
    print(idx)

# Create a loop that prints even numbers from 0 to and including 20.Hint: You can find multiples of 2 with (whatever_number % 2 == 0)


x = range(0, 21, +2)
for idx in x:
    print(idx)

# Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered. Refer to example below replacing NUMBER1, NUMBER2, NUMBER3, and THEAVERAGE with the actual values.

# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE

ask1 = int(input("Enter 1st number: "))
ask2 = int(input("Enter 2nd number: "))
ask3 = int(input("Enter 3rd number: "))
total = ask1 + ask2 + ask3
average = total / 3
print(average)
print ("The average of", ask1, ask2, ask3, "is", str(average))
