#!/usr/bin/python3

def raise_exception():
    """Raises a type exception."""
    try:
        # Attempt to perform an operation that would raise a type exception
        result = 5 + "5"
    except TypeError as e:
        # If a TypeError occurs, print the error message
        print(f"TypeError: {e}")

# Call the function to see the exception
raise_exception()
