def all_numbers():
    """
    Create a Python program that prints all the numbers from 0 to 4 except two distinct numbers entered by the user.
    Note : Use 'continue' statement.

    If user input is
    ```
    3
    2
    ```
    Expected Output :
    '0 1 4'
    """

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    
    for i in range(0, 5):
        if i == num1 or i == num2:
            continue
        print(i)

def dog_years():
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

    h_age = int(input("Input a dog's age in human years: \n"))
    print(int(h_age * 4.9))



def consonant_or_vowel():
    """
    Build a program to check whether an alphabet is a consonant or vowel.

    Expected Output:
    ```
    Input a letter of the alphabet: k
    k is a consonant.
    ```
    """

    l = input("Input a letter of the alphabet: ")

    if l in "aeiou":
        print(f"{l} is a vowel")
    else:
        print(f"{l} is a consonant")


def month_numbers():
    """
    Create a program to as input month's name to the number of days it has. The first letter of the month name should always be a capital letter

    Expected Output:
    ```
    List of months: January, February, March, April, May, June, July, August, September, October, November, December
    Input the name of Month: February
    No. of days: 28/29 days
    ```
    """

    print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
    month_name = input("Input the name of Month: ")

    if month_name == "February":
        print("No. of days: 28/29 days")
    elif month_name in "January March May July August October December":
        print("No. of days: 31 days")
    else:
        print("No. of days: 30 days")


def pyramids():
    """
    Using a for loop, write a program to print the following pattern:

    @
    @@
    @@@
    @@@@
    @@@@@
    @@@@
    @@@
    @@
    @
    """

    rows = int(input())
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("@" * j)
        print("\r")

    for i in range(rows, 0, -1):
        for j in range(0, i - 1):
            print("@" * j)
        print("\r")


def fibonacci():
    """
    The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
    The Fibonacci series from 0 to 4181 is `0,  1 , 1,  2,  3,  5,  8 , 13,  21,  34 , 55,  89,  144,  233,  377,  610,  987,  1597  ,2584,  4181`
    Write a program that will take as user input any two consecutive numbers between 0 and `4181` in the Fibonacci sequence, e.g. `1` `1` or `34` `55`.
    Use a loop to print out the next 10 numbers in the sequence that follow the 2 entered as input e.g. If input is
    ```
    0
    1
    ```
    the output will be:
    ```
    Fibonacci sequence:
    0 1 1 2 3 5 8 13 21 34
    ```

    if the input is
    ```
    55
    89
    ```
    the output will be:
    ```
    Fibonacci sequence:
    55  89  144  233  377  610  987
    ```
    The program should stop printing after `987`. Any number in the series after 987 should not be printed
    """

    # first two numbers
    num1 = int(input())
    num2 = int(input())

    print("Fibonacci sequence:")
    # run loop 10 times
    for i in range():
        # print next number of a series
        if ():
            None
            #enter your code here


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    # all_numbers()
    # dog_years()
    # consonant_or_vowel()
    # month_numbers()
    pyramids()
    # fibonacci()
