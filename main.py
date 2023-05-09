#!/usr/bin/python3

def accept_val(prompt: str) -> int:
    while True:
        try:
            data = int(input(f"Enter {prompt}: "))
            return data
        except ValueError:
            print("Error: Provide a numeric data.")
    return 0

if __name__ == "__main__":
    import math_func as mth
    try:
        first = accept_val("First Value")
        second = accept_val("Second Value")

        add_result = mth.addition(first, second)
        print(f"The sum of {first} and {second} = {add_result}")
    
        sub_result = mth.subtract(first, second)
        print(f"The difference between {first} and {second} = {sub_result}")

        mul_result = mth.multiply(first, second)
        print(f"The product of {first} and {second} = {mul_result}")

        div_result = mth.divide(first, second)
        print(f"{first} divided bt {second} = {div_result}")

        print(f"12 divided by 0 = {mth.divide(12, 0)}")
    except (ValueError, TypeError, ZeroDivisionError) as err:
        print(err)
