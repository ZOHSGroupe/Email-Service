"""
generate_random_code Function

This function generates a random code of the specified length using a character set
consisting of uppercase letters, lowercase letters, and digits.

Parameters:
- length (int): The length of the random code to generate. Default is 10.

Returns:
- str: The generated random code.

Example:
    random_code = generate_random_code()
"""

import secrets
import string


def generate_random_code(length=6):
    """
    Generate a random code of the specified length.

    Parameters:
    - length (int): The length of the random code to generate. Default is 10.

    Returns:
    - str: The generated random code.
    """
    # Define the character set for the code
    characters = string.ascii_letters + string.digits

    # Generate a random code with the specified length
    random_code = ''.join(secrets.choice(characters) for _ in range(length))

    return random_code
