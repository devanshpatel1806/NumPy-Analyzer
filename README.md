# 🧮 NumPy Analyzer – Array Operations and Statistical Analysis

## 📌 Project Overview

**NumPy Analyzer** is a menu-driven Python application developed using the NumPy library and Object-Oriented Programming (OOP) concepts. The project provides a simple way to create, manipulate, analyze, and perform mathematical operations on multidimensional NumPy arrays.

The application allows users to create 1D, 2D, and 3D arrays, perform mathematical calculations, combine and split arrays, search for particular values, sort and filter data, and calculate statistical measures.

The program uses an interactive console-based menu so that users can select the required operation and view the result immediately. It also demonstrates the practical use of Python classes, objects, constructors, encapsulation, private methods, class methods, and static methods.

This project was created for learning and practice to strengthen Python programming skills and understand numerical data analysis using NumPy.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To understand the NumPy library and its importance in numerical computing.
- To create and manipulate one-dimensional, two-dimensional, and three-dimensional arrays.
- To perform mathematical operations on arrays.
- To understand array indexing and slicing.
- To combine multiple arrays and split arrays into smaller parts.
- To search for specific elements and perform sorting and filtering operations.
- To calculate statistical measures using NumPy functions.
- To implement Object-Oriented Programming concepts in a practical application.
- To develop an interactive, menu-driven Python program.
- To improve input validation and error-handling skills.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Array manipulation and numerical calculations |
| Visual Studio Code | Code development and execution |
| GitHub | Source code hosting and project documentation |

---

## ✨ Main Features

### 1. Create NumPy Arrays

This feature allows users to create arrays of different dimensions according to their requirements.

**Operations included:**
- Creating 1D arrays.
- Creating 2D arrays by specifying rows and columns.
- Creating 3D arrays by specifying layers, rows, and columns.
- Displaying the created array.
- Accessing individual elements through indexing.
- Extracting portions of arrays through slicing.

**Example:**

```python
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print(arr)
```

Output:

```text
[[10 20 30]
 [40 50 60]]
```

### 2. Perform Mathematical Operations

This feature performs numerical calculations on arrays using NumPy functions.

**Operations included:**
- **Addition:** Adds corresponding elements.
- **Subtraction:** Subtracts corresponding elements.
- **Multiplication:** Multiplies corresponding elements.
- **Division:** Divides corresponding elements, with checks for division by zero.
- **Dot Product:** Calculates the dot product of arrays.
- **Matrix Multiplication:** Multiplies compatible matrices.

These operations demonstrate how NumPy simplifies calculations compared with manually processing each array element.

### 3. Combine or Split Arrays

This feature demonstrates array manipulation techniques.

**Operations included:**
- Combining arrays using concatenation.
- Combining two-dimensional arrays vertically.
- Combining two-dimensional arrays horizontally.
- Splitting an array into multiple equal parts when the dimensions permit it.

These operations are useful when working with datasets that need to be joined or separated for analysis.

### 4. Search, Sort, or Filter Arrays

This feature helps users locate values and organize array data.

**Operations included:**
- Searching for a specific value.
- Displaying the indices where the value occurs.
- Sorting elements in ascending order.
- Sorting elements in descending order.
- Filtering values greater than a specified number.
- Filtering values less than a specified number.
- Selecting values equal to a specified number.

Filtering and sorting make it easier to understand and process numerical data.

### 5. Compute Aggregates and Statistics

This feature calculates descriptive statistical measures from the current array.

| Statistical operation | Description |
|---|---|
| Sum | Calculates the total of all elements |
| Mean | Calculates the arithmetic average |
| Median | Finds the middle value of the sorted data |
| Standard Deviation | Measures the spread of values around the mean |
| Variance | Measures the average squared deviation from the mean |
| Minimum | Finds the smallest element |
| Maximum | Finds the largest element |
| Percentile | Calculates a selected percentile |
| Correlation Coefficient | Measures the linear relationship between two numerical datasets |

The correlation coefficient requires a second dataset containing the same number of values. A constant dataset does not provide a defined correlation coefficient.

### 6. Object-Oriented Programming

The application uses a `DataAnalytics` class to organize its operations.

**OOP concepts demonstrated:**

- **Class:** `DataAnalytics` groups the methods related to array analysis.
- **Object:** An instance of `DataAnalytics` is created to run the application.
- **Constructor:** `__init__()` initializes the array attribute.
- **Encapsulation:** The current array is stored in a private attribute named `__array`.
- **Private methods:** Methods such as `__check_array()` and `__read_numbers()` support internal operations.
- **Class method:** `welcome()` demonstrates the use of the `@classmethod` decorator.
- **Static method:** `show_information()` demonstrates a method that does not depend on instance data.

These concepts help make the program organized and demonstrate the use of OOP in a practical Python project.

---

## 🖥️ Main Menu

When the application starts, it displays the following menu:

```text
Welcome to the NumPy Analyzer!
========================================
Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
Enter your choice:
```

Users enter the number of the operation they want to perform. The program executes the selected operation and returns to the main menu, allowing users to continue working until they choose Exit.

---

## 📸 Project Screenshots

This section displays the outputs of the NumPy Analyzer project, demonstrating its main features and operations.

### 1. Main Menu
Displays the six main options available in the application.

![Main Menu](screenshots/main_menu.png)

### 2. Array Creation
Demonstrates creating one-dimensional, two-dimensional, and three-dimensional NumPy arrays.

![Array Creation](screenshots/array_creation.png)

### 3. Array Indexing and Slicing
Shows how to access individual elements and extract selected portions of arrays.

![Array Indexing and Slicing](screenshots/indexing_slicing.png)

### 4. Mathematical Operations
Demonstrates addition, subtraction, multiplication, division, dot product, and matrix multiplication.

![Mathematical Operations](screenshots/mathematical_operations.png)

### 5. Combining and Splitting Arrays
Shows how to combine multiple arrays and split an array into smaller parts.

![Combining and Splitting Arrays](screenshots/combine_split.png)

### 6. Searching, Sorting, and Filtering
Demonstrates searching for elements, sorting array values, and filtering data using conditions.

![Searching, Sorting, and Filtering](screenshots/search_sort_filter.png)

### 7. Aggregates and Statistics
Displays statistical operations such as sum, mean, median, standard deviation, variance, minimum, maximum, and percentile.

![Aggregates and Statistics](screenshots/aggregates_statistics.png)

### 8. Object-Oriented Programming (OOP)
Shows the OOP concepts implemented in the project, including classes, objects, encapsulation, class methods, and static methods.

![OOP Concepts](screenshots/oop_module_information.png)

## ⚙️ Installation and Setup

Follow these steps to install and run the NumPy Analyzer on your computer.

### Prerequisites

Before running the application, ensure that you have:

- Python installed on your computer.
- Visual Studio Code installed.
- The NumPy library installed.

### Step 1: Download or Clone the Repository

Clone the repository using Git:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your actual GitHub repository.

Alternatively, download the repository as a ZIP file and extract it.

### Step 2: Open the Project

Open the `NumPy_Analyzer` folder in Visual Studio Code.

### Step 3: Open the Terminal

In Visual Studio Code, select **Terminal → New Terminal**.

### Step 4: Install NumPy

Execute the following command:

```bash
python -m pip install numpy
```

Wait until the installation completes.

### Step 5: Run the Application

Execute:

```bash
python main.py
```

The welcome message and main menu will appear in the terminal.

---

## 📁 Project Structure

The project can be organized using the following folder structure:

```text
NumPy_Analyzer/
│
├── main.py
│
├── requirements.txt
│
├── README.md
│
└── screenshots/
    ├── main_menu.png
    ├── array_creation.png
    ├── indexing_slicing.png
    ├── mathematical_operations.png
    ├── combine_split.png
    ├── search_sort_filter.png
    ├── aggregates_statistics.png
    ├── oop_module_information.png
    └── exit_message.png
```

**File descriptions:**

- `main.py` — Contains the complete Python application.
- `README.md` — Provides project documentation and usage instructions.
- `screenshots/` — Contains screenshots showing the program's outputs.


## 📚 Learning Outcomes

By developing this project, I practised:

1. Creating and manipulating multidimensional NumPy arrays.
2. Performing mathematical operations on numerical data.
3. Using indexing and slicing to access array elements.
4. Combining and splitting arrays.
5. Applying searching, sorting, and filtering techniques.
6. Calculating descriptive statistical measures.
7. Implementing classes, objects, constructors, and encapsulation.
8. Using private, class, and static methods.
9. Handling invalid inputs and common runtime errors.
10. Building a menu-driven console application.
11. Organizing code and documenting a project using GitHub.

---

## 🔮 Future Enhancements

The project can be extended in the future by adding:

- A graphical user interface.
- CSV file import and export.
- Graphical visualizations of statistical results.
- More advanced statistical operations.
- Additional array manipulation features.
- Automated unit tests for individual operations.

## Conclusion

The **NumPy Analyzer** project provides a simple, menu-driven application for performing numerical computations and array operations using Python and NumPy. It allows users to create one-dimensional, two-dimensional, and three-dimensional arrays, perform mathematical and matrix operations, combine and split arrays, search, sort, filter data, and calculate statistical measures.

This project also demonstrates important Object-Oriented Programming (OOP) concepts, including classes, objects, constructors, encapsulation, class methods, and static methods. The interactive menu makes the application easy to use and helps users understand how NumPy simplifies numerical calculations and data analysis.

Overall, this project strengthened practical knowledge of Python programming, NumPy array manipulation, mathematical computations, statistical analysis, and OOP concepts. It serves as a useful learning project for understanding numerical data processing in Python.
