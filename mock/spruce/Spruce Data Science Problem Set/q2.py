# Spruce Data Science Problem Set
# Question 2

import unittest
import string

class TestSpruceQ2(unittest.TestCase):
    """
    Question 2 Unit Test for the 5 unit tests outlined in the readme
    I don't understand how Madam Arora is a palindrome
    since MAD != MAL


    I added three test cases to make sure I didn't miss something
    since the Madam Arora is bothering me

    """

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))
        self.assertFalse(is_palindrome("Python"))  
        # self.assertTrue(is_palindrome("Madam Arora teaches malayalam")) # How is this True?
        self.assertFalse(is_palindrome("Hello, World!")) 
        self.assertTrue(is_palindrome("Sit on a potato pan, Otis."))
        self.assertTrue(is_palindrome("Madam, I'm Adam."))
        self.assertTrue(is_palindrome("Able was I, ere I saw Elba."))

def clean_text(s: str) -> str:
    """
    clean_text: a helper function to remove punctuation, replace spaces 
    and make the text lowercase (i.e case-insensitve)
    """
    custom_punctuation = u" "
    punctuations = string.punctuation + custom_punctuation
    ss = [letter.translate(str.maketrans('','',punctuations)) for letter in s]
    ss = [letter.lower() for letter in ss]
    return ''.join(ss) 

def is_palindrome(s:str) -> str:
    """
    is_palindrome: a main function to check if the input is a palindrome. 
    """
    s = clean_text(s)
    print(s)
    reverse_s = s[::-1]

    for i, char in enumerate(s):
        if char == reverse_s[i]:
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    unittest.main(argv=[''],verbosity=2,exit=False)