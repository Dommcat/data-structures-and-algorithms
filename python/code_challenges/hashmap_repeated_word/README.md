# Python 401: Code Challenge Class 31
## Hash table repeated word

## Whiteboard Process:
<!-- Embedded whiteboard image -->
 <!-- [WhiteBoard Code Challenge 12](wbcc12animal.png) -->
[WhteBoard](/python/Assets/hashmap-repeated-word.png)
<!--
[//]: # (## Approach & Efficiency)

[//]: # (What approach did you take? Why? What is the Big O space/time for this approach?) -->


### Feature Tasks
Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: string


## Solution Code:
<!-- Show how to run your code, and examples of it in action -->

[Code Challenge 31 - Code Example](/python/code_challenges/hashmap_repeated_word/hashmap_repeated_word.py)

## Code Re/Sources:
ChatGPT
Class Demo File
Code Fellows TA Assistance

## Testing:

feature tests to prove the following functionality:

- Test blank string: expected None
- Test string with no repeated words: expected None
- Test string with one repeated word: expected the repeated word
- Test string with two repeated words of the same type: expected the repeated word
- Test string with two repeated words of different types: expected the first repeated word
- Test string with two repeated words of different types in reverse order: expected the second repeated word
- Test string with repeated words of different cases: expected the repeated word in lower case
- Test string with repeated words of different cases in reverse order: expected the repeated word in upper case
- Test string with repeated words and punctuation marks: expected the repeated word without punctuation marks
- Test string with repeated words and multiple punctuation marks: expected the repeated word without punctuation marks

All tests passing
