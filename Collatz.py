#A function named Collatz
def collatz(number):
    if (number%2) == 0:
        return (number // 2)
    else:
        return (3 * number + 1)


try:
    number = int(input())
    while True:
        if number != 1:
           number = collatz(number)
           print(number)
        else:
            break
except ValueError:
    print("Error:Invalid value entered. Please enter an Integer value to proceed")
except NameError:
    print("Please enter an integer values only!")

