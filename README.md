# String Finder

## Description

The purpose of this test is to give us a small sample of your code and to see how you approach and solve a simple problem. This is a simple class to extract matching strings from an array regardless of the characters order.

You will write a Python class that accepts an array of strings in the constructor. The class will expose a find function that accepts a string. The function will return all strings from the array that contains the exact same characters as the string passed into it. The order of the characters in the strings is not relevant.

For example, the constructor should take an array as follows:
finder = Finder(['asd', 'asdd', 'fre']) Calling finder.find('sad') should return ['asd'].
In the case where more than one member of the initialization array matches the key the return array will have more than one member.

## Commands
**Run Test Cases:**
```
python -m unittest string_finder.py
```
**Run Programe:**
```
python string_finder.py
```
## Demo

```
----------String Finder------------

Enter Q to quit.

Input:
	Enter array of strings> ['asd', 'asdd', 'fre']
	Enter string> sad

Output> ['asd']

Input:
	Enter array of strings> Q
Quit
```
