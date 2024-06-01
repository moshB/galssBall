import math


# This code was written by Mosh.bo
# Student at Ariel University


# Function to create a matrix filled with algorithm
def create_matrix(rows, cols):
    matrix = [[1 for _ in range(cols)] for _ in range(rows)]  # Initialize all elements as 1

    # Fill the remaining elements using the formula (excluding first row and column)
    for i in range(1, rows):  # Use i as loop counter
        for j in range(0, cols):
            matrix[i][j] = sum(matrix[i - 1][0:j]) + 1
    return matrix


# Function to create a "perfect matrix" for the algorithm
def create_perfect_matrix(n, k):
    """Creates a matrix suitable for the ball polling algorithm based on total balls (k) and layers (n).

  Args:
      k: Total number of balls.
      n: The number of floors for the resulting matrix.

  Returns:
      A list of lists representing the "perfect matrix".
  """

    # Calculate the number of columns based on the logarithm of n (base 2)
    cols = math.ceil(math.log2(n))  # Explanation: This calculates the minimum number of bits needed to represent n

    # Create a base matrix using the helper function
    matrix = create_matrix(k, cols)

    # Loop until the sum of the last row is less than the total number of floors (n)
    while sum(matrix[k - 1]) < n:
        # Append 1 to the first row (represents adding a new polling layer)
        matrix[0].append(1)

        # Update elements in subsequent rows based on the previous row's values
        for i in range(1, len(matrix)):
            # Calculate the sum of elements in the previous row (up to the current column)
            row_sum = sum(matrix[i - 1][
                          :len(matrix[i - 1])])  # Explanation: This excludes elements beyond the current column length
            matrix[i].append(row_sum)  # Append the calculated sum to the current row
    return matrix


# Function to check the number of columns needed for a given number of balls (n) and floors (k)
def checking_number(n: int, k: int) -> int:
    """Checks the validity of layers (k) and returns the number of columns needed for polling n balls.

  Args:
      n: Total number of floors.
      k: Number of balls (rows).

  Returns:
      The number of columns needed in the "perfect matrix", or None if k is invalid.
  """

    if k < 1:
        return None  # Raise an error or handle invalid k here (e.g., print("Invalid number of balls"))

    # Create the "perfect matrix" and return the number of columns
    matrix = create_perfect_matrix(n, k)
    return len(matrix[0])


# Function that finds the first index to testing, when there is (n) floors
def index_first_floor(n: int) -> int:
    return math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2)


def jumping_test(potential, b):
    """Checks if a value (b) is less than a (potential).
  Returns:
      True if b is less than potential, False otherwise.
  """

    return b < potential  # Concise comparison


def index_floor(f_i: list[int], b: int) -> int:
    """Searches for an index in a list (f_i) based on a threshold (b) and potentially using information from index_first_floor (unclear function).

  This function appears to search for the first element in f_i that's greater than the threshold (b) while potentially leveraging some pre-calculated information from a function called index_first_floor. However, the exact role of index_first_floor needs further investigation.

  Args:
      f_i: A list of integers to search within.
      b: An integer representing the threshold value.

  Returns:
      The index of the first element in f_i that's greater than b, or -1 if no such element exists.
  """

    floor_min = 0  # Initialize a variable to track the minimum search index (floor)
    f_i_l = f_i.copy()  # Create a copy of the input list to avoid modifying the original

    bol = True
    while bol:
        local_n = len(f_i_l)  # Get the length of the current working list

        # Call index_first_floor (unclear purpose - needs investigation)
        index_floor = index_first_floor(local_n)

        if jumping_test(f_i_l[index_floor - 1], b):  # Check if element at index_floor-1 is less than b
            for i in range(index_floor):  # Iterate from 0 to index_floor-1
                if f_i_l[i] > b:  # Check if any element is greater than b within the "floor" range
                    return i + floor_min + 1  # Return the index if found

        else:
            f_i_l = f_i_l[index_floor:]  # Update working list by removing elements before index_floor
            floor_min += index_floor  # Update minimum search index by adding index_floor

        if len(f_i_l) == 0:  # Loop exits if the working list becomes empty
            bol = False

    return -1  # Return -1 if no element satisfies the condition


#testers
def test_index_first_floor():
    # Test cases with expected results (heuristic assumptions)
    test_cases = [
        (1, 1), (2, 2), (3, 2),
        (4, 3), (5, 3), (6, 3),
        (7, 4), (8, 4), (9, 4),
        (10, 4), (11, 5), (12, 5),
        (13, 5), (14, 5), (15, 5),
        (16, 6), (17, 6), (18, 6)
    ]

    # Run tests and print results
    for n, expected_index in test_cases:
        actual_index = index_first_floor(n)
        if actual_index == expected_index:
            print(f"Test passed: Expected index {expected_index} for {n} layers")
        else:
            print(f"Test failed: Expected index {expected_index}, got {actual_index} for {n} layers")


def test_checking_number():
    # Test cases with expected results
    test_cases = [
        (1, 1, 1), (1, 2, 1), (2, 2, 2),
        (3, 2, 2), (4, 2, 3), (5, 2, 3),
        (6, 2, 3), (7, 2, 4), (8, 2, 4),
        (9, 2, 4), (10, 2, 4), (11, 2, 5),
        (1, 3, 1), (2, 3, 2), (3, 3, 2),
        (4, 3, 3), (5, 3, 3), (6, 3, 3),
        (7, 3, 3), (8, 3, 4), (9, 3, 4),
        (10, 3, 4), (11, 3, 4),
    ]

    # Run tests and print results
    for n, k, expected_result in test_cases:
        try:
            actual_columns = checking_number(n, k)
            if expected_result is None:
                print(f"Test failed: Expected error for {n} layers and {k} balls")
            else:
                if actual_columns == expected_result:
                    print(f"Test passed: Expected {expected_result} columns for {n} layers and {k} balls")
                else:
                    print(
                        f"Test failed: Expected {expected_result} columns, got {actual_columns} for {n} layers and {k} balls")
        except Exception as e:  # Catch any exceptions raised by checking_number
            if expected_result is None:
                print(f"Test passed: Error raised for {n} layers and {k} layers ({e})")
            else:
                print(
                    f"Test failed: Expected {expected_result} columns, got an exception ({e}) for {n} layers and {k} balls")


def test_index_floor():
    # Test cases with expected results
    test_cases = [
        ([1], 2, -1),
        ([2], 1, 1),
        ([1, 2, 3], 2, 3),
        ([1, 2, 34, 345], 3, 3),
        ([1, 2, 3, 4], 0, 1),
        ([7, 8, 9, 10], 11, -1),
    ]

    # Run tests and print results
    for test_list, threshold, expected_index in test_cases:
        actual_index = index_floor(test_list.copy(), threshold)
        if actual_index == expected_index:
            print(f"Test passed: Expected index {expected_index} for list {test_list} and threshold {threshold}")
        else:
            print(
                f"Test failed: Expected index {expected_index}, got {actual_index} for list {test_list} and threshold {threshold}")


if __name__ == '__main__':
    # Run the tester
    test_index_floor()
    # Run the tester
    test_checking_number()
    # Run the tester
    test_index_first_floor()
