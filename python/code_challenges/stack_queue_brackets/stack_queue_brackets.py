from .stacks import Stack

"""
Write a function called validate brackets
Arguments: string

Return: boolean
representing whether or not the brackets in the string are balanced

There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}
"""


def multi_bracket_validation (str):
    lst = ['(','[','{']
    brackets = Stack()
    for i in str:
        if i in lst:
            brackets.push(i)
        if brackets.top:
            if i == ")":
                if brackets.peek() == "(":
                    brackets.pop()
                else:
                    return False

            if i == "}":
                if brackets.peek() == "{":
                    brackets.pop()
                else:
                    return False

            if i == "]":
                if brackets.peek() == "[":
                    brackets.pop()
                else:
                    return False

    if brackets.top:
        return False
    else:
        return True


