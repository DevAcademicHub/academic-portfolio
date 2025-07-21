"""
For each function, describe what it actually does when called with a string argument. 
If it does not correctly check for lowercase letters, 
give an example argument that produces incorrect results, 
and describe why the result is incorrect.
"""

# 1

def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False

print(any_lowercase1("Hello")) # Output: False (incorrect result)
# This will return False, which is incorrect
# The function incorrectly returns False after checking the first character 'H',
# which is uppercase, without checking the rest of the string.
# Why?
# The function stops checking after the first character, so it does not consider


# 2

def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'

print(any_lowercase2("Hello"))  # Output: 'True' (incorrect result)
any_lowercase2("Hello")  # This will always return 'True', which is incorrect
# The function checks if the character 'c' is lowercase, which it always is,
# and returns 'True' without checking the input string.
# Why?
# The function stops checking after the first character, so it does not consider


# 3

def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag

print(any_lowercase3("Hello")) # Output: False (incorrect result)
# This will return False, which is incorrect
# The function only checks the last character of the string,
# so if the last character is uppercase, it returns False.
# Why?
# The function does not accumulate the results of checking each character,
# it only returns the result of the last character checked.

# 4

def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag

print(any_lowercase4("Hello")) # Output: True (correct result)
# This will return True, which is correct
# The function correctly checks each character and returns True if any character is lowercase.
# Why?
# The function accumulates the results of checking each character using the `or` operator,
# so it returns True if at least one character is lowercase.

# 5

def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True

print(any_lowercase5("Hello"))  # Output: False (incorrect result)
# This will return False, which is incorrect
# The function checks if all characters are lowercase,
# and returns False if it finds any uppercase character.
# Why?
# The function stops checking after the first uppercase character, so it does not consider
# the case where there are lowercase characters present in the string.