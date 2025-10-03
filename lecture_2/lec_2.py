import numpy as np

def main():
    i = 3
    a = 5
    n = 10.1
    x = 19.0

    sum_result = n + x
    print("Sum of floats:", sum_result)
    print("Data type:", type(sum_result), "\n")

    diff_result = a - i
    print("Difference of two integer is:", diff_result)
    print("Data type:", type(diff_result), "\n")

    prod_result = a * n
    print("Product of a float and an integer:", prod_result)
    print("Data type:", type(prod_result), "\n")

if __name__ == "__main__":
    main()