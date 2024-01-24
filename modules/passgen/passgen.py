"""
Generates a password of the specified length from a combination of 
uppercase and lowercase letters, numbers, and selected symbols 
commonly allowed in password fields.

This is intended to be run from the command line with optional arguments.

If run with no arguments, the script will generated a random 15-character
password using all character categories (including symbols) and will 
ensure there is at least one each of a number, lowercase letter, 
and uppercase letter.

"""

# Some code below adapted in part from examples in the official 
# Python documentation at https://docs.python.org/3/library/secrets.html
# which is licensed under the Zero Clause BSD License.

import string
import secrets
import sys
import argparse

ALPHANUMERIC = string.ascii_letters + string.digits
SYMBOLS = "!@$%^*<>?"
ALL_CHARS = ALPHANUMERIC + SYMBOLS


def passgen(length, ns):
    if ns == True:
        while True:
            password = "".join(secrets.choice(ALPHANUMERIC)
                for i in range(int(length)))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
                    break
        return password
    elif ns == False:
        while True:
            password = "".join(secrets.choice(ALL_CHARS)
                for i in range(int(length)))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
                    break
        return password
    else:
        print("There was an error.  Please use the -h option to see usage info")
        
parser = argparse.ArgumentParser(
    prog="python passgen",
    description="A password generator using the Python secrets module",
    epilog=""
)
parser.add_argument(
    "-l",
    "--length",
    default=15, 
    help="Specify password length in characters"
)
parser.add_argument(
    "-ns",
    action="store_true",
    default=False,
    help="If this argument is provided, no symbols will be included "
        "in the passcode"
)


args = parser.parse_args()

print("Your password is:  ", end="")
print(passgen(**vars(args)))

