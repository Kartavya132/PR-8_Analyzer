import numpy
from sys import exit


def show_menu():
    print("----------------------------------------")
    print("|----Welcome to the Numpy Analyzer!----|")
    print("----------------------------------------\n")

    print("---------------------------")
    print("|-----Numpy main menu-----|")
    print("-----------------------")
    print("1. Create a Numpy Array")
    print("2. Perform mathematics Operations")
    print("3. Combine / Split Arrays")
    print("4. Search, Sort, or filter from array")
    print("5. Compute Aggregates aand statistics")
    print("6. Exit")
    return input("Enter the choice :")


def create_array():
    while True:
        print("----------------------")
        print("Select the type of array")
        print("1. 1D array")
        print("2. 2D array")
        print("3. 3D array")
        typ = input("Enter the choice : ")
        try:
            match typ:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case _:
                    print("Invalid Choice")
        except ValueError:
            print("Enter the integer only")


def main():
    while True:
        choi = show_menu()
        print("-----------------------")
        match choi:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                print("Thank you for using numpy analyzer")
                print("Good Bye")
                print("-----------------------")
                exit()
            case _:
                print("Invalid Choice!!")
