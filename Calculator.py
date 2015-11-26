# Make a calculator that does +, -, *, and /, however, alerting if the special "ZeroDivisionError" or any errors occur.
import sys
def InputFunction():
    try:
        FirstNumber = float(input("What is the first number? "))
        SecondNumber = float(input("What is the second number? "))
        Operation = input("What is the operation? +, -, *, or / ")
        if Operation == "/":
            Divide(FirstNumber, SecondNumber)
        elif Operation == "+":
            Add(FirstNumber, SecondNumber)
        elif Operation == "*":
            Multiply(FirstNumber, SecondNumber)
        elif Operation == "-":
            Subtract(FirstNumber, SecondNumber)
        else:
            print("We're sorry, however, your command cannot be recognized. Please look at the operation syntax on the prompt.")
            InputFunction()
    except:
        ErrorName = sys.exc_info()[0]
        ErrorHandle(ErrorName)
def Add(FirstNumber, SecondNumber):
    try:
        AddResult = FirstNumber + SecondNumber
        print(AddResult)
    except:
        ErrorName = sys.exc_info()[0]
        ErrorHandle(ErrorName)
    AskContinue()
def Subtract(FirstNumber, SecondNumber):
    try:
        SubtractResults = FirstNumber - SecondNumber
        print(SubtractResults)
    except:
        ErrorName = sys.exc_info()[0]
        ErrorHandle(ErrorName)
    AskContinue()
def Multiply(FirstNumber, SecondNumber):
    try:
        MultiplyResults = FirstNumber * SecondNumber
        print(MultiplyResults)
    except:
        ErrorName = sys.exc_info()[0]
        ErrorHandle(ErrorName)
    AskContinue()
def Divide(FirstNumber, SecondNumber):
    try:
       DivisionResult =  FirstNumber / SecondNumber
       print(DivisionResult)
       Flag = False
    except ZeroDivisionError:
        ErrorName = sys.exc_info()[0]
        print("We're sorry for the error. This error will occur when you try to divide a number by zero.")
        print(ErrorName)
        print("Please try again.")
        InputFunction()
    except:
        ErrorName = sys.exc_info()[0]
        ErrorHandle(ErrorName)
    AskContinue()
def AskContinue():
    try:
        Continue = input("Do you want to continue? ")
        ContinueString = Continue.upper()
        if ContinueString == "YES":
            InputFunction()
        else:
            print("Thank you!")
    except:
        ErrorName = sys.exc_info()[0]
        ErrorHandle(ErrorName)
def ErrorHandle(ErrorName):
    print("We're sorry, an error has occurred.")
    print("Please use this error name when contacting support or troubleshooting: ")
    print(ErrorName)
    print("Please try again.")
    InputFunction()
print("Welcome to the calculator!")
InputFunction()
