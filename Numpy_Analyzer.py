import numpy as np
from sys import exit


class numpy_analyzer:
    def __init__(self):
        self.arr = None

    def create_array(self):
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
                        no = input("Enter the number(seperated by space) : ").split()
                        number = [int(i) for i in no]
                        arr = np.array(number)
                        break
                    case "2":
                        row = int(input("Enter the no. of row : "))
                        col = int(input("Enter the no. of column : "))
                        if row <= 0 or col <= 0:
                            print("Enter a valid number greater than 0.")
                            continue
                        no = input(
                            f"Enter {row * col} element(seperated by space) : "
                        ).split()
                        if len(no) != row * col:
                            print("Please enter proper no. of elements")
                            continue
                        number = []
                        ic = 0
                        for _ in range(row):
                            de = []
                            for _ in range(col):
                                de.append(int(no[ic]))
                                ic += 1
                            number.append(de)
                        arr = np.array(number)
                        break
                    case "3":
                        row = int(input("Enter the no. of row : "))
                        col = int(input("Enter the no. of column : "))
                        page = int(input("Enter the no. of pages : "))
                        if row <= 0 or col <= 0 or page <= 0:
                            print("Enter a valid number greater than 0.")
                            continue
                        no = input(
                            f"Enter {page * row * col} element(seperated by space) : "
                        ).split()
                        if len(no) != page * row * col:
                            print("Please enter proper no. of elements")
                            continue
                        ic = 0
                        number = []
                        for _ in range(page):
                            demo = []
                            for _ in range(row):
                                de = []
                                for _ in range(col):
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
        self.arr = arr
        print("The array is successfully created ::-")
        print(self.arr)
        self.basic_op()
        return self.arr

    def basic_op(self):
        if self.arr is None:
            print("There is no saved array")
            return

        arr = self.arr
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
                            row_col = input("Enter the index (row column) : ").split()
                            print(arr[int(row_col[0]), int(row_col[1])])
                        elif arr.ndim == 3:
                            pag_row_col = input(
                                "Enter the index (page row column) : "
                            ).split()
                            print(
                                ":-",
                                arr[
                                    int(pag_row_col[0]),
                                    int(pag_row_col[1]),
                                    int(pag_row_col[2]),
                                ],
                            )
                        else:
                            print("Please retry again")
                    case "2":
                        if arr.ndim == 1:
                            row_s = input("Enter the range (start:stop) : ").split(":")
                            print(":-", arr[int(row_s[0]) : int(row_s[1])])
                        elif arr.ndim == 2:
                            row_s = input(
                                "Enter the range of row (start:stop) : "
                            ).split(":")
                            col_s = input(
                                "Enter the range of column (start:stop) : "
                            ).split(":")
                            print(
                                ":-",
                                arr[
                                    int(row_s[0]) : int(row_s[1]),
                                    int(col_s[0]) : int(col_s[1]),
                                ],
                            )
                        elif arr.ndim == 3:
                            pag_s = input(
                                "Enter the range of page (start:stop) : "
                            ).split(":")
                            row_s = input(
                                "Enter the range of row (start:stop) : "
                            ).split(":")
                            col_s = input(
                                "Enter the range of column (start:stop) : "
                            ).split(":")
                            print(
                                ":-",
                                arr[
                                    int(pag_s[0]) : int(pag_s[1]),
                                    int(row_s[0]) : int(row_s[1]),
                                    int(col_s[0]) : int(col_s[1]),
                                ],
                            )
                    case "3":
                        print("Thank you")
                        break
                    case _:
                        print("Enter valid choice")
            except ValueError:
                print("Enter the integer as instructed")

    def math_arr(self):
        if self.arr is None or self.arr.size < 1:
            print("There is no saved array")
            return

        arr = self.arr
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
            s_no = input(f"Enter {arr.size} elements(seperated by space) : ").split()
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
                case _:
                    print("Invalid choice")

    def combine_split(self):
        if self.arr is None or self.arr.size < 1:
            print("There is no saved array")
            return

        arr = self.arr
        while True:
            print("------------------------")
            print("Choose an option")
            print("1. Combine")
            print("2. Split")
            print("3. Exit")
            cho = input("Enter your choice : ")
            match cho:
                case "1":
                    c_no = input(
                        f"Enter {arr.size} elements(seperated by space) : "
                    ).split()
                    if len(c_no) != arr.size:
                        print("Please enter proper no. of elements")
                        continue
                    try:
                        c_num = [int(i) for i in c_no]
                        sec_arr = np.array(c_num).reshape(arr.shape)
                    except ValueError:
                        print("Enter the integer as per instruction")
                        continue
                    vert_hori = input("Enter 1: vertical stack, 2: horizontal stack : ")
                    match vert_hori:
                        case "1":
                            print(f"Original array:-\n{arr}")
                            new_arr = np.vstack((arr, sec_arr))
                        case "2":
                            print(f"Original array:-\n{arr}")
                            new_arr = np.hstack((arr, sec_arr))
                        case _:
                            print("Invalid choice")
                            continue
                    self.arr = new_arr
                    arr = self.arr
                    print(f"Second array:-\n{sec_arr}")
                    print(f"The new array:-\n{arr}")
                case "2":
                    if arr.size <= 1:
                        print("You can't split this 1 element in the array")
                        break
                    if arr.ndim == 1:
                        row_s = input("Enter the range to split(start:end)").split(":")
                        try:
                            row_s = [int(i) for i in row_s]
                        except ValueError:
                            print("Invalid input, Enter the integer")
                            continue
                        print(f"Original array:-\n{arr}")
                        self.arr = arr[row_s[0] : row_s[1]]
                    elif arr.ndim == 2:
                        row_s = input("Enter the range of row (start:stop) : ").split(
                            ":"
                        )
                        col_s = input(
                            "Enter the range of column (start:stop) : "
                        ).split(":")
                        self.arr = arr[
                            int(row_s[0]) : int(row_s[1]), int(col_s[0]) : int(col_s[1])
                        ]
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
                        self.arr = arr[
                            int(pag_s[0]) : int(pag_s[1]),
                            int(row_s[0]) : int(row_s[1]),
                            int(col_s[0]) : int(col_s[1]),
                        ]
                    else:
                        print("Invalid choice")
                        continue
                    arr = self.arr
                    print(f"The new array:-\n{arr}")
                case "3":
                    print("Thank you")
                    break
                case _:
                    print("Invalid input")

    def sear_sort_filt(self):
        if self.arr is None or self.arr.size < 1:
            print("There is no saved array")
            return

        arr = self.arr
        while True:
            print("-------------------")
            print("Choose an option::")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Exit")
            cho = input("Enter the choice : ")
            match cho:
                case "1":
                    try:
                        search = int(input("Enter the element for search: "))
                    except ValueError:
                        print("Invalid input")
                        continue
                    result = np.where(arr == search)
                    if result[0].size == 0:
                        print(f"The element {search} is not in array")
                    else:
                        indices = list(result)
                        print(f"The search found indices: {indices[0:]}")
                case "2":
                    print(f"Original array:-\n{arr}")
                    self.arr = np.sort(arr)
                    arr = self.arr
                    print(f"The sorted array:-\n{arr} ")
                case "3":
                    try:
                        threshold = int(input("Show values greater than: "))
                    except ValueError:
                        print("Invalid input")
                        continue
                    filtered = arr[arr > threshold]
                    print(f"Filtered values greater than {threshold}:-\n{filtered}")
                case "4":
                    print("Thank you")
                    break
                case _:
                    print("Invalid choice")

    def aggre_stat(self):
        if self.arr is None or self.arr.size < 1:
            print("There is no saved array")
            return

        arr = self.arr
        while True:
            print("-------------------")
            print("Choose the option")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard deviation")
            print("5. Variance")
            print("6. Exit")
            cho = input("Enter the choice : ")

            match cho:
                case "1":
                    print(
                        f"The sum of all elements in the array\n:-{round(arr.sum(),2)}"
                    )
                case "2":
                    print(
                        f"The mean of all the elements in the array\n:-{round(arr.mean(),2)}"
                    )
                case "3":
                    print(
                        f"The median of all the elements in the array\n:-{round(np.median(arr),2)}"
                    )
                case "4":
                    print(
                        f"The standard deviation of all the elements in array\n:-{round(np.std(arr),2)}"
                    )
                case "5":
                    print(
                        f"The variance of all elements in the array\n:-{round(np.var(arr),2)}"
                    )
                case "6":
                    print("Thank you")
                    return
                case _:
                    print("Invalid Input")


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
    print("5. Compute Aggregates and statistics")
    print("6. Exit")
    return input("Enter the choice :")


def main():
    numpy_al = numpy_analyzer()
    while True:
        choi = show_menu()
        print("-----------------------")
        match choi:
            case "1":
                numpy_al.create_array()
            case "2":
                numpy_al.math_arr()
            case "3":
                numpy_al.combine_split()
            case "4":
                numpy_al.sear_sort_filt()
            case "5":
                numpy_al.aggre_stat()
            case "6":
                print("Thank you for using numpy analyzer")
                print("Good Bye")
                print("-----------------------")
                exit()
            case _:
                print("Invalid Choice!!")


if __name__ == "__main__":
    main()
