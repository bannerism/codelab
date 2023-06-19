# Spruce Data Science Problem Set
# Question 3

import unittest

class TestSpruceQ3(unittest.TestCase):
    """
    Question 3 Unit Test for the 4 unit tests outlined in the readme
    """

    def test_unique_elements(self):
        self.assertEqual(unique_elements([4, 2, 3, 2, 1, 4, 5, 4]), [4, 2, 3, 1, 5])
        self.assertEqual(unique_elements([3, 3, 3, 3, 3]),[3])  # 
        self.assertEqual(unique_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]),[1, 2, 3, 4, 5])  # 
        self.assertEqual(unique_elements([]),[])  # 

def unique_elements(lst:list) -> list:
    """
    unique_elements: list of elements in, list of unique elements out
    the unique elements retain their order as the input
    """
    uniq_elem = []
    for elem in lst:
        if elem not in uniq_elem:
            uniq_elem.append(elem)
    return uniq_elem



if __name__ == "__main__":
    unittest.main(argv=[''],verbosity=2,exit=False)