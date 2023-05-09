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

    first = accept_val("First Value")
    second = accept_val("Second Value")

    result = mth.add(first, second)
    print(f"The sum of {first} and {second} = {result}")    
