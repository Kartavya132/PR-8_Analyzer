import numpy as np
from sys import exit


def show_menu():
    print("----------------------------------------")
    print("|----Welcome to the Numpy Analyzer!----|")
    print("----------------------------------------\n")

    print("---------------------------")
    print("|-----Numpy main menu-----|")
    print("---------------------------")
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
                    break
                case "2":
                    row = int(input("Enter the no. of row : "))
                    col = int(input("Enter the no. of column : "))
                    no = input(
                        f"Enter {row * col} element(seperated by space) : "
                    ).split(" ")
                    if len(no) != row * col:
                        print("Please enter proper no. of elements")
                        continue
                    if not (row and col):
                        print("Enter the valid number not 0.")
                        continue
                    number = []
                    ic = 0
                    for _ in range(0, row):
                        de = []
                        for _ in range(0, col):
                            de.append(int(no[ic]))
                            ic += 1
                        number.append(de)
                    arr = np.array(number)
                    break
                case "3":
                    row = int(input("Enter the no. of row : "))
                    col = int(input("Enter the no. of column : "))
                    page = int(input("Enter the no. od pages : "))
                    if not (row and col and page):
                        print("Enter the valid number not 0.")
                        continue
                    no = input(
                        f"Enter {page * row * col} element(seperated by space) : "
                    ).split(" ")
                    if len(no) != (page * row * col):
                        print("Please enter proper no. of elements")
                        continue
                    ic = 0
                    number = []
                    for _ in range(0, page):
                        demo = []
                        for _ in range(0, row):
                            de = []
                            for _ in range(0, col):
                                de.append(int(no[ic]))
                                ic += 1
                            demo.append(de)
                        number.append(demo)
                    arr = np.array(number)
                    break
                case _:
                    print("Invalid Choice")
        except ValueError:
            print("Enter the integer only")
    print("The array is successfully created ::-")
    print(arr)
    basic_op()


def basic_op():
    while True:
        print("--------------------")
        print("Choose any operation")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Jump to main menu")
        cho = input("Enter your choice : ")
        print("--------------------")
        try:
            match cho:
                case "1":
                    if arr.ndim == 1:
                        row_i = int(input("Enter the index : "))
                        print(":-", arr[row_i])
                    elif arr.ndim == 2:
                        row_col = input("Enter the index (row column) : ").split(" ")
                        print(arr[int(row_col[0])][int(row_col[1])])
                    elif arr.ndim == 3:
                        pag_row_col = input(
                            "Enter the index (page row column) : "
                        ).split(" ")
                        print(
                            ":-",
                            arr[int(pag_row_col[0])][int(pag_row_col[1])][
                                int(pag_row_col[2])
                            ],
                        )
                    else:
                        print("Please retry again")
                case "2":
                    if arr.ndim == 1:
                        row_s = input("Enter the range (start:stop) : ").split(":")
                        print(":-", arr[int(row_s[0]) : int(row_s[1])])
                    elif arr.ndim == 2:
                        row_s = input("Enter the range of row (start:stop) : ").split(
                            ":"
                        )
                        col_s = input(
                            "Enter the range of column (start:stop) : "
                        ).split(":")
                        print(
                            ":-",
                            arr[int(row_s[0]) : int(row_s[1])][
                                int(col_s[0]) : int(col_s[1])
                            ],
                        )
                    elif arr.ndim == 3:
                        pag_s = input("Enter the range of page (start:stop) : ").split(
                            ":"
                        )
                        row_s = input("Enter the range of row (start:stop) : ").split(
                            ":"
                        )
                        col_s = input(
                            "Enter the range of column (start:stop) : "
                        ).split(":")
                        print(
                            ":-",
                            arr[int(row_s[0]) : int(row_s[1])][
                                int(col_s[0]) : int(col_s[1])
                            ][int(pag_s[0]) : int(pag_s[1])],
                        )
                case "3":
                    print("Thank you")
                    break
                case _:
                    print("Enter valid choice")
        except ValueError:
            print("Enter the integer as instructed")


def math_arr():
    if arr:
        while True:
            print("--------------------")
            print("Mathematics menu")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            cho = input("Enter your choice : ")
            if cho == "5":
                print("Thank you")
                break
            s_no = input(f"Enter {arr.size} elements(seperated by space) : ").split(" ")
            if len(s_no) != arr.size:
                print("Please enter proper no. of elements")
                continue
            try:
                s_num = [int(i) for i in s_no]
                sec_arr = np.array(s_num).reshape(arr.shape)
            except ValueError:
                print("Enter the integer as per instruction")
                continue
            match cho:
                case "1":
                    print(f"Original array:-\n{arr}")
                    print(f"Second array:-\n{sec_arr}")
                    print(f"The new array:-\n{arr + sec_arr}")
                case "2":
                    print(f"Original array:-\n{arr}")
                    print(f"Second array:-\n{sec_arr}")
                    print(f"The new array:-\n{arr - sec_arr}")
                case "3":
                    print(f"Original array:-\n{arr}")
                    print(f"Second array:-\n{sec_arr}")
                    print(f"The new array:-\n{arr * sec_arr}")
                case "4":
                    try:
                        print(f"Original array:-\n{arr}")
                        print(f"Second array:-\n{sec_arr}")
                        print(f"The new array:-\n{arr / sec_arr}")
                    except ZeroDivisionError:
                        print("Don't enter zero for division")
    else:
        print("There is no saved array")


def main():
    while True:
        choi = show_menu()
        print("-----------------------")
        match choi:
            case "1":
                create_array()
            case "2":
                math_arr()
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
