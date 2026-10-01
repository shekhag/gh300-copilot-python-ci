# add functions here
def add(a, b):
    return a + b

# add multiply function here
def multiply(a, b):
    return a * b

# add main function to run the test
if __name__ == "__main__":
    print(add(2, 3))  # Expected output: 5
    print(add(-2, -3))  # Expected output: -5
    print(add(-2, 3))  # Expected output: 1

    assert add(2, 3) == 5  # Expected output: 5
    assert add(-2, -3) == -5  # Expected output: -5
    assert add(-2, 3) == 1  # Expected output: 1

    print(multiply(2, 3))  # Expected output: 6
    print(multiply(-2, -3))  # Expected output: 6
    print(multiply(-2, 3))  # Expected output: -6

    assert multiply(2, 3) == 6  # Expected output: 6
    assert multiply(-2, -3) == 6  # Expected output: 6
    assert multiply(-2, 3) == -6  # Expected output: -6
    print("All tests passed!")

