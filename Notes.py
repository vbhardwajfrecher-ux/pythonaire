qQuetions: 1 #Generators in python?

#1-filter

example:

syntax and Description>  
my_list = [1,2,3,4,5,6,7,8] 



def addnum(num1,num2)
                                                                """                       
                            As filter takes two arg
                       call_func 1st arg , calling_list  
                             ⇓               ⇓
                                                                """
USER_TEMP_VAR = filter(Function, Function_input_data(my_list))

#?>call the functions results

resturn list(USER_TEMP_VAR)
or
print (list(USER_TEMP_VAR))

output> [2,4,6,8]

------------------------------------------------------------------------------------------------------------------------------
Quesion: 2 #lamda or anonymus functions and expression strength?

"""
Solving the above with Lamda function
"""


my_list = [1,2,3,4,5,6,7,8] >>> LIST

"""                       
                                 As filter takes two arg

                         call_func 1st arg,          calling_list. 
                          by lambda func.  
                                 ⇓                       ⇓
"""

USER_TEMP_VAR = filter(lambda num: num%2 == 0, Function_input_data(my_list))

@Printing result
    #Here_working_on_LIST_FOR_RESULT
         ⇓   
print (list(USER_TEMP_VAR))

output> [2,4,6,8]

------------------------------------------------------------------------------------------------------------------------------------

# .split() methods with '#' tag
"""
In Python, the split() method is used to split a string into a list of substrings
based on a specified delimiter. If the delimiter is not specified, the default delimiter is whitespace.

To split a string using the '#' character as the delimiter,
you can use the split() method with '#' as the argument. Here's an example:
"""
Ex.>
import re
string = "Hello#world#Python"
split_string = string.split("#") 
print(split_string)

Output>>> ['Hello', 'world', 'Python']
"""
In the above example, the split() method is used to split the string variable 
into a list of substrings using the '#' character as the delimiter. 
The resulting list contains three elements: 'Hello', 'world', and 'Python'.
You can also use the maxsplit parameter to specify the maximum number of splits to make.
"""

string = "Hello#world#Python#programming"
split_string = string.split("#", 2)
print(split_string)

Output>>> ['Hello', 'world', 'Python#programming']

"""
the split() method splits the string variable
into a list of substrings using the '#' character as the delimiter, 
but it only makes two splits. 
The resulting list contains three elements: 'Hello', 'world', and 'Python#programming'.
"""

------------------------------------------------------------------------------------------------------------------------------

"""
Delimeters used in Python
"""
#Whitespace (default delimiter)

string = "Hello World" 
split_string = string.split()
print(split_string)


Output: ['Hello', 'World']

#Comma ',' (delimiter)
 
string = "apple,banana,orange"
split_string = string.split(",")
print(split_string)

Output: ['apple', 'banana', 'orange']

#Semicolon ';'

string = "apple;banana;orange"
split_string = string.split(";")
print(split_string)

Output: ['apple', 'banana', 'orange']

#Colon ':'

string = "apple:banana:orange"
split_string = string.split(":")
print(split_string)

Output: ['apple', 'banana', 'orange']

#PIPE '|'

string = "apple|banana|orange"
split_string = string.split("|")
print(split_string)

Output: ['apple', 'banana', 'orange']

#DASH '_'

string = "apple-banana-orange"
split_string = string.split("-")
print(split_string)

Output: ['apple', 'banana', 'orange']

#Underscore '_'

string = "apple_banana_orange"
split_string = string.split("_")
print(split_string)

Output: ['apple', 'banana', 'orange']


#---Delimeter with other methods---

#>>>> JOIN method

list_of_strings = ['apple', 'banana', 'orange']
delimiter = ","
joined_string = delimiter.join(list_of_strings)
print(joined_string)

Output: apple,banana,orange
#>>>> REPLACE method

string = "apple,banana,orange"
new_string = string.replace(",", ";")
print(new_string)

Output: apple;banana;orange 
#>>>> Strip method

string = "  apple,banana,orange  "
stripped_string = string.strip()
print(stripped_string)

#>>>> Endwith  and Startwith method

#Here we're checking the string starts with "apple" and ends with "orange"
string = "apple,banana,orange"

#Passing the 1st arg 
starts_with_apple = string.startswith("apple")

#Passing the 2nd arg
ends_with_orange = string.endswith("orange")

print(starts_with_apple)

print(ends_with_orange)

Output: True
        
--------------------------------------------------------------------------------------------------------------------------------

@REGULAR_EXPRESSIONS #REGEX
(re methods)
"""
The re module in Python is used for working with regular expressions. 
A regular expression is a sequence of characters that defines a search pattern. 
Regular expressions can be used to perform various operations on strings such as searching, replacing, and extracting text.

The re module provides several functions and methods that can be used to work with regular expressions.
"""
#>>>> Methods

#Search method "search()"

>>>>> #This method searches for a pattern in a string and returns the first occurrence of that pattern.

import re
string = "The quick brown fox jumps over the lazy dog"
pattern = "fox"
result = re.search(pattern, string)
print(result.group())

#Findall method "findall()"
>>>>> #This method finds all occurrences of a pattern in a string and returns them as a list.
 
import re
string = "The quick brown fox jumps over the lazy dog"
pattern = "o"
result = re.findall(pattern, string)
print(result)

#Match method "match()"
>>>>> #This method searches for a pattern at the beginning of a string and returns the first occurrence of the pattern.

import re
string = "The quick brown fox jumps over the lazy dog"
pattern = "The"
result = re.match(pattern, string)
print(result.group())

#SUB method "sub()"
>>>>> #This method replaces all occurrences of a pattern in a string with a specified replacement string.


import re

enter_paragraph = input("Enter the Paragraph: ")
find_word = input("Enter the search word: ")
Enter_replacement = input("Enter the replacement: ")

string = enter_paragraph
pattern = find_word
replacement = Enter_replacement

result = re.sub(pattern, replacement, string)
print(result)



---------------------------------------------------------------------------------------------------------------------------------         
#camel casing & snake casing



#python process_managers 
         ⇓
1> Waitress: ?
2> Tornado: ?
3> uWSGI: ?
4> Gunicorn: ?
5> Systemd: ?
6> Circus: ?

#list comprehention

#python, > control flow

#enumerators?

#decorators ?

     