"""
This program helps boot camp participants track their progress
using the learning map.
"""

import sys

def display_greeting():
    """
    Formats and prints the program greeting.
    """
    # Init.
    title = " Skills progress "

    print("\n{:*^80s}\n".format(title.title()))
    print("\tThis program helps boot camp participants track their progress")
    print("\tusing the learning map.")
    print("\n{:*^80s}\n".format("*"))

def main():
    # Display the program greeting.
    display_greeting()

    while True:
        # Ask if the user wants to continue.
        while True:
            response = input("\nContinue? (y/n): ")
            if response in "yYnN":
                break
            print("Invalid response")
        if response.lower() == "n":
            print("\nGoodbye")
            break

if __name__ == "__main__":
    main()
