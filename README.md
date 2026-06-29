# 📊 NumPy Analyzer

An interactive command-line NumPy application built using Python that allows users to create, manipulate, analyze, and perform various operations on multidimensional arrays.
---

# 📌 Overview

NumPy Analyzer is a menu-driven Python project designed to help users learn and work with NumPy arrays interactively.

The application supports:

- Creating 1D, 2D, and 3D arrays
- Mathematical operations
- Array indexing and slicing
- Combining and splitting arrays
- Searching, sorting, and filtering
- Statistical analysis
- Aggregate computations

This project is useful for:

- Python beginners
- Data Science students
- NumPy learners
- Programming practice

---

# 🚀 Features

## ✅ Array Creation

Supports:

- 1D Arrays
- 2D Arrays
- 3D Arrays

Example:

```python
1D:
[1 2 3 4]

2D:
[[1 2]
 [3 4]]

3D:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

---

## ✅ Basic Operations

### Indexing

```python
arr[2]
arr[1,2]
arr[0,1,1]
```

### Slicing

```python
arr[1:4]
arr[0:2,1:3]
arr[0:1,0:2,1:3]
```

---

## ✅ Mathematical Operations

Perform:

- Addition
- Subtraction
- Multiplication
- Division

Example:

```python
Array A:
[1 2 3]

Array B:
[4 5 6]

Addition:
[5 7 9]
```

---

## ✅ Combine Arrays

### Vertical Stack

```python
np.vstack()
```

Output:

```python
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

### Horizontal Stack

```python
np.hstack()
```

Output:

```python
[1 2 3 4 5 6]
```

---

## ✅ Split Arrays

Supports:

- 1D splitting
- 2D splitting
- 3D splitting

Example:

```python
Original:
[1 2 3 4 5]

Split:
[2 3 4]
```

---

## ✅ Search Operations

Uses:

```python
np.where()
```

Example:

```python
Array:
[1 5 3 5 7]

Search 5:

Output:
(array([1,3]),)
```

---

## ✅ Sorting

Uses:

```python
np.sort()
```

Example:

```python
Before:
[5 2 9 1]

After:
[1 2 5 9]
```

---

## ✅ Filtering

Example:

```python
Input:
[4 12 18 7 22]

Filter > 10

Output:
[12 18 22]
```

---

## ✅ Statistical Operations

Compute:

- Sum
- Mean
- Median
- Standard Deviation
- Variance

Example:

```python
Array:
[10 20 30 40]

Sum      = 100
Mean     = 25
Median   = 25
Std Dev  = 11.18
Variance = 125
```

---

---

# ⚙ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| NumPy | Numerical Computing |
| OOP | Class Design |
| Match-Case | Menu Handling |

---

# 📚 Class Structure

```text
numpy_analyzer
│
├── create_array()
├── basic_op()
├── math_arr()
├── combine_split()
├── sear_sort_filt()
└── aggre_stat()
```

---

# 🔄 Program Flow

```text
Start
   |
   V
Main Menu
   |
   ├── Create Array
   ├── Mathematical Operations
   ├── Combine/Split
   ├── Search/Sort/Filter
   ├── Statistics
   └── Exit
```

---

# 📸 Sample Output

## Create Array

```bash
Select the type of array

1. 1D array
2. 2D array
3. 3D array

Enter choice: 1

Enter numbers:
1 2 3 4 5

The array is successfully created:
[1 2 3 4 5]
```

---

## Mathematical Operations

```bash
Original Array:
[1 2 3]

Second Array:
[4 5 6]

Addition Result:
[5 7 9]
```

---

## Statistics

```bash
Choose Option

1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance

Output:

Sum = 15
Mean = 3.0
Median = 3
Std = 1.41
Variance = 2.0
```

---

# 📦 Installation


---

# 🧪 NumPy Functions Used

```python
np.array()
np.where()
np.sort()
np.vstack()
np.hstack()
np.mean()
np.median()
np.std()
np.var()
```

---

# 🎯 Learning Outcomes

This project helps in understanding:

- NumPy Arrays
- Multidimensional Arrays
- Array Manipulation
- Statistical Analysis
- Searching and Filtering
- Object-Oriented Programming
- Exception Handling
- Python Match-Case
- Interactive CLI Applications
---