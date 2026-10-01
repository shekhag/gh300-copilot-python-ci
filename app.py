# add functions here
def add(a, b):
    return a + b

# add main function to run the test
if __name__ == "__main__":
    print(add(2, 3))  # Expected output: 5
    print(add(-2, -3))  # Expected output: -5
    print(add(-2, 3))  # Expected output: 1

    assert add(2, 3) == 5  # Expected output: 5
    