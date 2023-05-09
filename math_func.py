#!/usr/bin/python3

def addition(val_a: int|float, val_b: int|float) -> int | float:
    if type(val_a) == int or type(val_a) == float:
        if type(val_b) == float or type(val_b) == int:
            return val_a + val_b
        else:
            raise Exception("Second value must be numeric.")
    else:
        raise Exception("First value must be numeric.")

def subtract(val_a: int|float, val_b: int|float) -> int | float:
    if type(val_a) == int or type(val_a) == float:
        if type(val_b) == float or type(val_b) == int:
            return val_a - val_b
        else:
            raise Exception("Second value must be numeric.")
    else:
        raise Exception("First value must be numeric.")

def multiply(val_a: int|float, val_b: int|float) -> int | float:
    if type(val_a) == int or type(val_a) == float:
        if type(val_b) == float or type(val_b) == int:
            return val_a * val_b
        else:
            raise Exception("Second value must be numeric.")
    else:
        raise Exception("First value must be numeric.")

def divide(val_a: int|float, val_b: int|float) -> int | float:
    if type(val_a) == int or type(val_a) == float:
        if type(val_b) == float or type(val_b) == int:
            if val_b != 0:
                return val_a / val_b
            else:
                raise ZeroDivisionError("You cannot divide by 0")
        else:
            raise Exception("Second value must be numeric.")
    else:
        raise Exception("First value must be numeric.")

