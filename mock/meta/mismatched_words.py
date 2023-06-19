import unittest


"""
Return Mismatched Words

Given an input of two strings consisting of english letters (a-z; A-Z) and spaces, complete a function that returns a list containing all the mismatched words (case sensitive) between them.
You can assume that a word is a group of characters delimited by spaces.
A mismatched word is a word that is only in one string but not the other.
Add mismatched words from the first string before you add mismatched words from the second string in the output array.

"""

class MetaTestCase(unittest.TestCase):
    def test_ex_1(self):
        self.assertEqual(mismatched(str1 = "Firstly this is the first string",
                                    str2 = "Next is the second string"),
                                    ["Firstly", "this", "first", "Next", "second"])
        
        self.assertEqual(mismatched(str1= "",
                                    str2 = "This is the second string"),
                                    ["This","is","the","second","string"])

        self.assertEqual(mismatched(str1= "This is the first string",
                                    str2 = "This is the second string"),
                                    ["first", "second"])

        self.assertEqual(mismatched(str1= "This is the first string extra",
                                    str2 = "This is the second string"),
                                    ["first", "extra", "second"])

        self.assertEqual(mismatched(str1= "This is the first text",
                                    str2 = "This is the second string"),
                                    ["first", "text", "second", "string"])



def mismatched_sets(str1:str,str2:str)-> list:
    """
    a helper function to compare two lists and return the difference between them
    using set methods

    note: this will not return a correct output but is a MVP
    """
    s1 = str1.split(' ')
    s2 = str2.split(' ')

    _s1 = set(s1).difference(set(s2))
    _s2 = set(s2).difference(set(s1))

    return list(_s1.union(_s2))

def list_difference(s1,s2):
    diff = []
    for w in s1:
        if w not in s2:
            diff.append(w)
    
    return diff


def mismatched(str1,str2):
    """
    a helper function to compare two lists and return a list of differences 
    without using set methods.
    """
    s1 = str1.split()
    s2 = str2.split(" ")

    _s1 = list_difference(s1,s2)
    _s2 = list_difference(s2,s1)

    res = _s1 + _s2
    return res
    


if __name__ == "__main__":
    unittest.main(argv=[''],verbosity=2,exit=False)
    # print(mismatched('Firstly this is the first string','Next is the second string'))


