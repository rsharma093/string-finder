from collections import defaultdict
import unittest
import ast

class Finder:
    def __init__(self, arr):
        self.arr = arr
        self.output = []

    # Convert string in lower case and remove whitespace if any
    def format_string(self, s):
        s = s.lower().strip()
        if " " in s:
            s = [i for i in s if i != " "]
            s = "".join(s)
        return s
    
    # Compare string character counts with target string counts
    def compare_counts(self, s, count):
        temp = count.copy()
        for char in s:
            if temp[char] == 0:
                return False
            else:
                temp[char] -= 1
                
        return True
    
    # Return main output array of matched strings
    def find(self, str1):
        # Format string first
        str1 = self.format_string(str1)

        # Get target string counts
        count = defaultdict(int)
        for char in str1:
            count[char] += 1

        # Match strings from array with target string    
        for s2 in self.arr:
            str2 = self.format_string(s2)
        
            # Check if lenght is not same
            if len(str1) != len(str2):
                continue
            else:
                if str1 == str2:
                    self.output.append(s2)
                    continue
                else:
                    if self.compare_counts(str2, count):
                        self.output.append(s2)
                    else:
                        continue
                    
        return self.output

## Test
class FinderTest(unittest.TestCase):
    def test(self):
        f = Finder(['asd', 'asdd', 'fre', 'dsa', 'mna'])
        self.assertEqual(f.find('sad'), ['asd', 'dsa'])

    def test_whitespace(self):
        f = Finder(['asmd', 'rtyh', 'tyul', 'dm  sa'])
        self.assertEqual(f.find('msa d'), ['asmd', 'dm  sa'])

    def test_upper(self):
        f = Finder(['Jal', 'Lam', 'mno', 'L aj'])
        self.assertEqual(f.find('alJ'), ['Jal', 'L aj'])

        print ('ALL TEST CASES PASSED')


if __name__ == "__main__":
    print("----------String Finder------------\n Input:\n\tEnter array of strings> [​'asd'​, ​'asdd'​, ​'fre'​]\n\tEnter string> sad\n\n Output: ['asd']\n\nEnter Q to quit.\n")
    is_quit = False
    while not is_quit:
        arr = input("\nEnter array of strings> ")
        string = input("Enter string>")
        if arr == "Q" or string == "Q":
            is_quit = True
        else:
            f = Finder(ast.literal_eval(arr))
            print("Output> {}".format(f.find(string)))