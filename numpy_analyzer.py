import numpy as np
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
    global arr
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
                    no = input("Enter the number(seperated by space) : ").split(" ")
                    number = [int(i) for i in no]
                    arr = np.array(number)
                    print("A 1D array is created")
                    return
                case "2":
                    row = int(input("Enter the no. of row : "))
                    col = int(input("Enter the no. of column : "))
                    no = input(f"Enter {row * col} element(seperated by space) : ")
                    number = []
                    for i in range(0, row):
                        de = []
                        for j in range(0, col):
                            de.append(no[i * col + j])
                        number.append(de)
                    arr = np.array(number)
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
                create_array()
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


if __name__ == "__main__":
    main()
