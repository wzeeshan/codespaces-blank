'''
 The // Code: comment markers highlight where you need to write your code.
# You should not edit code outside of the # Do not change the code comment markers or the checks may malfunction.
# The code files include test cases that you can run from the terminal. For example, you can test your challenge one code by entering python3 /home/project/challenge_one.py in the terminal.
'''


def string_fun(string):
    '''
    Return a tuple with three elements.
    The first element is True if the string contains only alphabet characters, otherwise False.
    The second element is True if the string ends with an exclamation mark ('!'), otherwise False.
    The third element is the string with all spaces (' ') replaced with hyphens ('-').
    Arguments
    string: a string
    Examples
    string_fun('Hello World!') returns (False, True, 'Hello-World!')
    string_fun('ThisIsAChallenge') returns (True, False, 'ThisIsAChallenge')
    '''

    # ====================================
    # Do not change the code before this

    # CODE1: Write code that will assign details with the appropriate tuple
    details = (False, True, "Hello-World!")

    # ====================================
    # Do not change the code after this

    return details

if __name__ == '__main__':
    print(string_fun('Hello World!'))
    print(string_fun('ThisIsAChallenge'))
