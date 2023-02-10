# Calculator
from art import logo
from replit import clear

print(logo)


def addition(n1, n2):
    return n1 + n2


def multiplication(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtraction(n1, n2):
    return n1 - n2


def calculater():
    num1 = float(input("Enter the first number:"))

    operation = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': divide,
    }

    again = True
    while again:
        num2 = float(input("enter the next number:"))
        for operator in operation:
            print(operator)

        do_operation = input("What operation want to perform: ")
        doing_calculate = operation[do_operation]
        answer = doing_calculate(num1, num2)
        print(f"{num1} {do_operation} {num2} = {answer}")

        if input(
                "Do you want to continue with the result: Type 'y' for yes or 'n' for no "
        ) == 'y':
            num1 = answer
            continue
        else:
            clear()
            calculater()


calculater()
