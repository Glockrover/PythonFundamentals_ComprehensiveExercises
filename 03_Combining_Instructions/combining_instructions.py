def max_three():
    """
    Write a Python function to find the Max of three numbers.
    Use the following as test input in STDIN

    Input:
    ```
    1
    8
    6
    ```
    """

    def max_of_two( x, y ):
        if x > y:
            return x
        return y
    def max_of_three( x, y, z ):
        if x > y and x > z:
            return x
        elif y > x and y > z:
            return y
        return z

    num1 = int(input("Please enter num1: "))
    num2 = int(input("Please enter num2: "))
    num3 = int(input("Please enter num3: "))
    biggest = max_of_three(num1, num2, num3)
    print("The max of the three numbers is:", biggest)


def between_3_and_9(n):
    """
    Write a Python function to check whether a number falls between 3 and 9
    """

    if n in range(3, 9):
        print(n)
    else:
        print("The number is outside the given range.")


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    max_three()
    between_3_and_9()
