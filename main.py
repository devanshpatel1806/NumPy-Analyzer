import numpy as np


class DataAnalytics:
    """NumPy Analyzer using Object-Oriented Programming."""

    def __init__(self):
        self.__array = None

    # Static method for converting input into numeric values
    @staticmethod
    def __read_numbers(message):
        values = list(map(float, input(message).split()))

        if all(value.is_integer() for value in values):
            return np.array(values, dtype=int)

        return np.array(values, dtype=float)

    # Private method for checking array availability
    def __check_array(self):
        if self.__array is None:
            print("Please create a NumPy array first.")
            return False
        return True

    # Class method
    @classmethod
    def welcome(cls):
        print("Welcome to the NumPy Analyzer!")

    # Static utility method
    @staticmethod
    def show_information():
        print("\nNumPy Analyzer")
        print("Python library: NumPy")
        print("Programming concepts: OOP and arrays")

    # 1. Array creation, indexing, and slicing
    def create_array(self):
        while True:
            print("\nSelect the type of array to create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            print("4. Indexing")
            print("5. Slicing")
            print("6. Go Back")

            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    self.__array = self.__read_numbers(
                        "Enter array elements separated by spaces: "
                    )

                elif choice == "2":
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))

                    if rows <= 0 or cols <= 0:
                        print("Dimensions must be positive.")
                        continue

                    values = self.__read_numbers(
                        f"Enter {rows * cols} elements separated by space: "
                    )

                    if values.size != rows * cols:
                        print("Incorrect number of elements.")
                        continue

                    self.__array = values.reshape(rows, cols)

                elif choice == "3":
                    depth = int(input("Enter the number of layers: "))
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))

                    if min(depth, rows, cols) <= 0:
                        print("Dimensions must be positive.")
                        continue

                    total = depth * rows * cols
                    values = self.__read_numbers(
                        f"Enter {total} elements separated by space: "
                    )

                    if values.size != total:
                        print("Incorrect number of elements.")
                        continue

                    self.__array = values.reshape(depth, rows, cols)

                elif choice == "4":
                    self.indexing()

                elif choice == "5":
                    self.slicing()

                elif choice == "6":
                    break

                else:
                    print("Invalid choice.")
                    continue

                if choice in ("1", "2", "3"):
                    print("\nArray created successfully:")
                    print(self.__array)

            except ValueError:
                print("Invalid input. Please enter valid numeric values.")

    def indexing(self):
        if not self.__check_array():
            return

        print("\nCurrent Array:")
        print(self.__array)

        try:
            indices = []
            for dimension in range(self.__array.ndim):
                index = int(input(
                    f"Enter index for dimension {dimension + 1}: "
                ))
                indices.append(index)

            print("Selected Element:", self.__array[tuple(indices)])

        except (ValueError, IndexError):
            print("Invalid index.")

    def slicing(self):
        if not self.__check_array():
            return

        print("\nCurrent Array:")
        print(self.__array)

        try:
            if self.__array.ndim == 1:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                result = self.__array[start:end]

            elif self.__array.ndim == 2:
                r1 = int(input("Enter row range start: "))
                r2 = int(input("Enter row range end: "))
                c1 = int(input("Enter column range start: "))
                c2 = int(input("Enter column range end: "))
                result = self.__array[r1:r2, c1:c2]

            else:
                d1 = int(input("Enter layer range start: "))
                d2 = int(input("Enter layer range end: "))
                result = self.__array[d1:d2]

            print("\nSliced Array:")
            print(result)

        except (ValueError, IndexError):
            print("Invalid slicing range.")

    # 2. Mathematical operations
    def mathematical_operations(self):
        if not self.__check_array():
            return

        while True:
            print("\nChoose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Dot Product")
            print("6. Matrix Multiplication")
            print("7. Go Back")

            choice = input("Enter your choice: ")

            if choice == "7":
                break

            if choice not in ("1", "2", "3", "4", "5", "6"):
                print("Invalid choice.")
                continue

            try:
                print("\nOriginal Array:")
                print(self.__array)

                if choice in ("1", "2", "3", "4"):
                    values = self.__read_numbers(
                        f"Enter {self.__array.size} elements "
                        "for the second array: "
                    )

                    if values.size != self.__array.size:
                        print("Incorrect number of elements.")
                        continue

                    second = values.reshape(self.__array.shape)

                    print("\nSecond Array:")
                    print(second)

                    if choice == "1":
                        result = np.add(self.__array, second)
                        name = "Addition"
                    elif choice == "2":
                        result = np.subtract(self.__array, second)
                        name = "Subtraction"
                    elif choice == "3":
                        result = np.multiply(self.__array, second)
                        name = "Multiplication"
                    else:
                        if np.any(second == 0):
                            print("Division by zero is not allowed.")
                            continue

                        result = np.divide(self.__array, second)
                        name = "Division"

                    print(f"\nResult of {name}:")
                    print(result)

                elif choice in ("5", "6"):
                    if self.__array.ndim != 2:
                        print("This operation requires a 2D array.")
                        continue

                    rows = int(input(
                        "Enter rows for the second matrix: "
                    ))
                    cols = int(input(
                        "Enter columns for the second matrix: "
                    ))

                    if rows <= 0 or cols <= 0:
                        print("Dimensions must be positive.")
                        continue

                    values = self.__read_numbers(
                        f"Enter {rows * cols} matrix elements: "
                    )

                    if values.size != rows * cols:
                        print("Incorrect number of elements.")
                        continue

                    second = values.reshape(rows, cols)

                    if choice == "5":
                        if self.__array.size != second.size:
                            print("Dot product requires equal-sized arrays.")
                            continue

                        result = np.dot(
                            self.__array.flatten(),
                            second.flatten()
                        )
                        print("\nDot Product Result:", result)

                    else:
                        if self.__array.shape[1] != second.shape[0]:
                            print("Matrix dimensions are incompatible.")
                            continue

                        result = np.matmul(self.__array, second)
                        print("\nMatrix Multiplication Result:")
                        print(result)

            except ValueError:
                print("Invalid input. Please try again.")

    # 3. Combine or split arrays
    def combine_split(self):
        if not self.__check_array():
            return

        while True:
            print("\nChoose an option:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")

            choice = input("Enter your choice: ")

            if choice == "3":
                break

            try:
                if choice == "1":
                    values = self.__read_numbers(
                        f"Enter the elements of another array "
                        f"({self.__array.size} elements separated by space): "
                    )

                    if values.size != self.__array.size:
                        print("Incorrect number of elements.")
                        continue

                    second = values.reshape(self.__array.shape)

                    print("\nOriginal Array:")
                    print(self.__array)
                    print("\nSecond Array:")
                    print(second)

                    if self.__array.ndim == 1:
                        result = np.concatenate((self.__array, second))
                    else:
                        print("\n1. Vertical Stack")
                        print("2. Horizontal Stack")
                        direction = input("Enter your choice: ")

                        if direction == "1":
                            result = np.concatenate(
                                (self.__array, second), axis=0
                            )
                        elif direction == "2":
                            result = np.concatenate(
                                (self.__array, second), axis=1
                            )
                        else:
                            print("Invalid choice.")
                            continue

                    print("\nCombined Array:")
                    print(result)

                elif choice == "2":
                    parts = int(input("Enter the number of parts: "))

                    if parts < 2:
                        print("Enter at least 2 parts.")
                        continue

                    if self.__array.ndim == 1:
                        if self.__array.size % parts != 0:
                            print("Array cannot be split equally.")
                            continue

                        result = np.split(self.__array, parts)

                    else:
                        axis = int(input(
                            f"Enter split axis (0 to "
                            f"{self.__array.ndim - 1}): "
                        ))

                        if not 0 <= axis < self.__array.ndim:
                            print("Invalid axis.")
                            continue

                        if self.__array.shape[axis] % parts != 0:
                            print("Array cannot be split equally on this axis.")
                            continue

                        result = np.split(self.__array, parts, axis=axis)

                    print("\nSplit Arrays:")
                    for index, part in enumerate(result, start=1):
                        print(f"Part {index}:")
                        print(part)

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Invalid input.")

    # 4. Search, sort, and filter arrays
    def search_sort_filter(self):
        if not self.__check_array():
            return

        while True:
            print("\nChoose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Go Back")

            choice = input("Enter your choice: ")

            if choice == "4":
                break

            try:
                print("\nOriginal Array:")
                print(self.__array)

                if choice == "1":
                    value = float(input("Enter the value to search: "))
                    positions = np.argwhere(self.__array == value)

                    if positions.size:
                        print("Value found at indices:")
                        print(positions)
                    else:
                        print("Value not found.")

                elif choice == "2":
                    print("1. Ascending")
                    print("2. Descending")
                    order = input("Choose sorting order: ")

                    if order == "1":
                        result = np.sort(self.__array, axis=-1)
                    elif order == "2":
                        result = np.sort(self.__array, axis=-1)[..., ::-1]
                    else:
                        print("Invalid choice.")
                        continue

                    print("\nSorted Array:")
                    print(result)
                    print("(Sorting applied along the last axis.)")

                elif choice == "3":
                    print("1. Greater than")
                    print("2. Less than")
                    print("3. Equal to")
                    condition = input("Choose a condition: ")
                    value = float(input("Enter comparison value: "))

                    if condition == "1":
                        result = self.__array[self.__array > value]
                    elif condition == "2":
                        result = self.__array[self.__array < value]
                    elif condition == "3":
                        result = self.__array[self.__array == value]
                    else:
                        print("Invalid choice.")
                        continue

                    print("\nFiltered Values:")
                    print(result)

                else:
                    print("Invalid choice.")

            except ValueError:
                print("Invalid input.")

    # 5. Aggregates and statistics
    def aggregates_statistics(self):
        if not self.__check_array():
            return

        while True:
            print("\nChoose an aggregate/statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum")
            print("7. Maximum")
            print("8. Percentile")
            print("9. Correlation Coefficient")
            print("10. OOP and Module Information")
            print("11. Go Back")

            choice = input("Enter your choice: ")

            if choice == "11":
                break

            try:
                print("\nOriginal Array:")
                print(self.__array)

                if choice == "1":
                    result = np.sum(self.__array)
                    name = "Sum"
                elif choice == "2":
                    result = np.mean(self.__array)
                    name = "Mean"
                elif choice == "3":
                    result = np.median(self.__array)
                    name = "Median"
                elif choice == "4":
                    result = np.std(self.__array)
                    name = "Standard Deviation"
                elif choice == "5":
                    result = np.var(self.__array)
                    name = "Variance"
                elif choice == "6":
                    result = np.min(self.__array)
                    name = "Minimum"
                elif choice == "7":
                    result = np.max(self.__array)
                    name = "Maximum"
                elif choice == "8":
                    percentile = float(input(
                        "Enter percentile (0 to 100): "
                    ))

                    if not 0 <= percentile <= 100:
                        print("Percentile must be between 0 and 100.")
                        continue

                    result = np.percentile(self.__array, percentile)
                    name = f"{percentile}th Percentile"

                elif choice == "9":
                    values = self.__read_numbers(
                        f"Enter {self.__array.size} elements "
                        "for the second array: "
                    )

                    if values.size != self.__array.size:
                        print("Incorrect number of elements.")
                        continue

                    first = self.__array.flatten()
                    second = values.flatten()

                    if first.size < 2:
                        print("At least two values are required.")
                        continue

                    if np.std(first) == 0 or np.std(second) == 0:
                        print("Correlation is undefined for constant data.")
                        continue

                    result = np.corrcoef(first, second)[0, 1]
                    name = "Correlation Coefficient"

                elif choice == "10":
                    self.welcome()
                    self.show_information()
                    print("\nDataAnalytics class attributes:")
                    print(dir(DataAnalytics))
                    print("\nNumPy version:", np.__version__)
                    continue

                else:
                    print("Invalid choice.")
                    continue

                print(f"\n{name} of Array: {result}")

            except ValueError:
                print("Invalid input.")

    # Main menu: exactly six options as specified
    def run(self):
        self.welcome()

        while True:
            print("=" * 40)
            print("Choose an option:")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_array()
            elif choice == "2":
                self.mathematical_operations()
            elif choice == "3":
                self.combine_split()
            elif choice == "4":
                self.search_sort_filter()
            elif choice == "5":
                self.aggregates_statistics()
            elif choice == "6":
                print(
                    "\nThank you for using the NumPy Analyzer! Goodbye!"
                )
                break
            else:
                print("Invalid choice. Please try again.")


# Main program
def main():
    analyzer = DataAnalytics()
    analyzer.run()


if __name__ == "__main__":
    main()
