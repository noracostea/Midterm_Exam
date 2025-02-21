# Question 1
a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2

# Question 2
print((2+3)*6/2 and 18.0)

# Question 3
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

# Question 4
def is_palindrome(word):
    return word == word[::-1]

options = {
    "A": "4257304920394478392772938744930294037524",
    "B": "7798338247658278460338648728567428338977",
    "C": "2704702208931031198668911301398022074072",
    "D": "0974101607733149676776769413377061014790"
}

for key, value in options.items():
    print(f"{key}: {'Palindrome' if is_palindrome(value) else 'Not a palindrome'}")

# Question 5
def count_pattern_occurrences(text):
    """
    Counts words that:
    - Start with 'un'
    - End with 'an'
    - Have at least one letter in between
    """

    words = text.split()  # Step 1: Split text into words
    count = 0  # Step 2: Initialize count

    for word in words:  # Step 3: Iterate through each word
        if word.startswith("un") and word.endswith("an") and len(word) > 4:
            count += 1  # Step 4: Increment if the word matches

    return count  # Step 5: Return the final count


# Example Usage
text = "uncommon unbroken unican unusualun universalun unpatternan"
print(count_pattern_occurrences(text))  # Expected Output: 3

# Question 6
my_list = [1, 2, 3]
print("Original list:", my_list)

my_list[0] = 100  # Modifying the first element
print("Modified list:", my_list)

# Original list: [1, 2, 3]
# Modified list: [100, 2, 3]


my_string = "hello"
# my_string[0] = "H"  # This will cause an error

# TypeError: 'str' object does not support item assignment

# This is how you actually modify a string
my_string = "hello"
new_string = "H" + my_string[1:]  # Creating a new string
print(new_string)  # "Hello"

# Question 7
import random

# Step 1: Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Step 2: Process the list based on the given conditions
for i in range(len(random_numbers)):  # Loop through each index
    if random_numbers[i] > 80:
        # If the number is greater than 80, replace it with its negative value
        random_numbers[i] = -random_numbers[i]
    elif random_numbers[i] < 40:
        # If the number is less than 40, replace it with the sum of its digits
        digits = str(random_numbers[i])  # Convert number to string
        digit_sum = int(digits[0]) + int(digits[1])  # Sum of digits
        random_numbers[i] = digit_sum  # Replace with digit sum

# Step 3: Print the final modified list
print(random_numbers)

# Question 8
def is_valid_url(url):
    """
    Checks if the given string follows a basic URL structure.
    A valid URL must:
    - Start with "http://" or "https://"
    - Contain at least one "." after the domain part
    - End with common domain endings like ".com", ".org", ".net"
    """

    # Step 1: Check if URL starts with 'http://' or 'https://'
    if url.startswith("http://") or url.startswith("https://"):

        # Step 2: Remove the protocol part
        url = url.split("//")[1]  # Get the part after "http://"

        # Step 3: Ensure there is at least one "."
        if "." in url:

            # Step 4: Ensure it ends with a common domain extension
            if url.endswith(".com") or url.endswith(".org") or url.endswith(".net"):
                return True  # It's a valid URL

    return False  # If any condition fails, it's not a valid URL


# Example Usage
print(is_valid_url("http://example.com"))  # True
print(is_valid_url("https://mywebsite.org"))  # True
print(is_valid_url("ftp://wrongprotocol.com"))  # False
print(is_valid_url("http://invalid-url"))  # False

# Question 9
def calculate_days_passed(birthday):
    """
    Given a birthday in "DD-MM-YYYY" format, calculates the number of days
    that have passed since the birth year (excluding birth year and current year).
    Assumes each year has 365 days.
    """

    # Step 1: Extract the birth year from the input string
    birth_year = int(birthday[-4:])  # Last 4 characters represent the year

    # Step 2: Extract the current year from user input
    current_year = int(input("Enter the current year: "))  # Must be manually provided

    # Step 3: Calculate the number of whole years passed (excluding birth and current year)
    years_passed = current_year - birth_year - 1  # We exclude birth and current year

    # Step 4: Convert years to days (365 days per year)
    days_passed = years_passed * 365

    return days_passed


# Example Usage
print(calculate_days_passed("26-05-2005"))