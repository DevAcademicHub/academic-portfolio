# This code snippet demonstrates string slicing and manipulation in Python.
fruit = 'banana'
print(fruit[:3]) # Output: ban (first three characters)
print(fruit[3:]) # Output: ana (from the fourth character to the end)
print(fruit[3:3]) # Output: '' (empty string)
print(fruit[:])# Output: banana (full string)
print(fruit[::-1]) # Output: ananab (reversed string)

# String concatenation and replacement
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting) # Output: Jello, world! (replaces 'H' with 'J')

# Function to find the first occurrence of a letter in a word
def find(word, letter):
     index = 0
     while index < len(word):
          if word[index] == letter:
               return index
          index = index + 1
     return -1

print(find('banana', 'a')) # Output: 1 (index of first 'a')
print(find('banana', 'z')) # Output: -1 (not found)

# Function to find the first occurrence of a letter in a word starting from a specific index
def find(word, letter, start):
     index = start
     while index < len(word):
          if word[index] == letter:
               return index
          index = index + 1
     return -1
print(find('banana', 'a', 0)) # Output: 1 (index of first 'a')
print(find('banana', 'a', 1)) # Output: 3 (index of first 'a' after index 1)
print(find('banana', 'a', 2)) # Output: 3 (index of first 'a' after index 2)

# Function to count occurrences of a letter in a word
def count(word, letter):
     count = 0
     for letter in word:
          if letter == 'a':
               count = count + 1
     print(count)

print(count('banana', 'a')) # Output: 3 (count of 'a' in 'banana')

# Then rewrite the function so that instead of traversing the string, 
# it uses the three parameter version of find from the previous section.
def count(word, letter, start=0):
     count = 0
     index = find(word, letter, start)
     while index != -1:
          count += 1
          index = find(word, letter, index + 1)
     return count

print(count('banana', 'a')) # Output: 3 (count of 'a' in 'banana')

def in_both(word1, word2):
     for letter in word1:
          if letter in word2:
               print(letter)

in_both('apples', 'oranges') # Output: a e s (letters in both words)

def is_reverse(word1, word2):
     if len(word1) != len(word2):
          return False
     i = 0
     j = len(word2) - 1
     while j >= 0:
          print(i, j)
          if word1[i] != word2[j]:
               return False
          i = i+1
          j = j-1
     return True

is_reverse('pots', 'stop')