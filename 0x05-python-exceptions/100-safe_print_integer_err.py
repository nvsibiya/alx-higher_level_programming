#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raises a name exception with a message."""
    try:
        # Raise a NameError with the specified message
        raise NameError(message)
    except NameError as e:
        # If a NameError occurs, print the error message
        print(f"NameError: {e}")

# Call the function with a custom message
raise_exception_msg("This is a custom error message.")
