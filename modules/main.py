#Main script to test utility functions from various modules.
import vowels
import multiplication
import mario
import mario2
import list_sorter
import table_generator
import name_validator
import email_validator
import auth_checker

# Test vowel counting in a user-entered string
x = input("Enter a string: ")
print(f"There are {vowels.vowels_num(x)} Vowels")

print("-" * 50)
#----------------------------------------------------

# Test printing a multiplication table for a user-entered number
x = int(input("Enter a number: "))
multiplication.multiplication(x)

print("-" * 50)
#----------------------------------------------------

# Test printing a right-aligned star triangle with 4 rows
mario.mario(4)

print("-" * 50)
#----------------------------------------------------

# Test generating a shifting star pattern of size 7
mario2.mario2(7)

print("-" * 50)
#----------------------------------------------------

# Test sorting 5 user-entered numbers
list_sorter.sort_user_input(5)

print("-" * 50)
#----------------------------------------------------

# Test generating a nested multiplication table for numbers 1 to 5
table_generator.multiplication_table(5)

print("-" * 50)
#----------------------------------------------------

# Prompt user for name until valid
while True:
    name = input("Enter your name: ").strip()
    if name_validator.verify_name(name):
        break
    print("Please enter a valid name (letters, spaces, hyphens, or apostrophes only).")

#Print the validated name
print(f"\nName: {name}")

print("-" * 50)
#----------------------------------------------------------------------------

# Prompt user for email until valid
while True:
    email = input("Enter your email: ").strip()
    if email_validator.verify_email(email):
        break
    print("Please enter a valid email address (e.g., example@domain.com).")

# Print the validated email
print(f"Email: {email}")

print("-" * 50)
#-----------------------------------------------------------------------------

# Test credential verification with user-entered name and password
name = input("Enter a name: ")
password = input("Enter password: ")
if auth_checker.verify_credentials(name, password):
    print("valid name and password")
else:
    print("Invalid name or password")