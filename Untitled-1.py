# # # # ==== Reversing a String

# # # def reverse_string(messeage1_type1):
# # #      """
# # #      Reverse a given string.

# # #      Args:
# # #          message1_type1 (str): The string to be reversed.

# # #      Returns:
# # #          str: The reversed string.

# # #      Examples:
# # #          >>> reverse_string("Hello")
# # #          "olleH"
# # #      """
    
# # #      new_str = " "

# # #      i = len(messeage1_type1)
# # #      while i > 0:
# # #          new_str += messeage1_type1[ i -1]

# # #          i = i - 1

# # #      return new_str


# # #  print(reverse_string(messeage1_type1="Hello"))




# # # # def reverse_string(message1_type1):
# # # #     """
# # # #     Reverse a given string.

# # # #     Args:
# # # #         message1_type1 (str): The string to be reversed.

# # # #     Returns:
# # # #         str: The reversed string.

# # # #     Examples:
# # # #         >>> reverse_string("Hello")
# # # #         "olleH"
# # # #     """
# # # #     return message1_type1[::-1]


# # # # print(reverse_string(message1_type1="Hello"))


# # # def user_num(heloo):
    
# # #     if heloo == int():
# # #         return heloo()
# # #     else:
# # #         return heloo[:]

# # # def country_code(heloo):

# # #     return heloo[:3]


# # #heloo = "+919910666254"

# # # print(f"Customer Mobile Number : ",user_num(heloo))
# # # print(f"Country code : ",country_code(heloo))




# # # def reverse_string(hello):
# # #     new_string = ""

# # #     for i in range(len(hello) - 1, -1, -1):
# # #         new_string += hello[i]

# # #     return new_string

# # # print(reverse_string(hello="+919910666254"))


# # #-------------------------------Reversing string (str)-----------------------------------------
# # #                                 TWO POINTER Algo

# # # def reverse_string(input_string):
# # #     characters = list(input_string)
# # #     left = 0
# # #     right = len(characters) - 1

# # #     while left < right:
# # #         characters[left], characters[right] = characters[right], characters[left]
# # #         left += 1
# # #         right -= 1

# # #     reversed_string = ''.join(characters)
# # #     return reversed_string

# # # # Example usage
# # # message = "Hello, World!"
# # # reversed_message = reverse_string(message)
# # # print(reversed_message)  # Output: "!dlroW ,olleH"



# # #--------------- reversing a string containing multi-byte or variable-length characters-------------

# # def reverse_string_multibyte(input_string):
# #     # Convert the string to a list of characters or code points
# #     characters = list(input_string)

# #     # Reverse the list of characters
# #     characters.reverse()

# #     # Reconstruct the reversed string while handling multi-byte characters
# #     i = 0
# #     while i < len(characters):
# #         # Check if the character is part of a multi-byte sequence
# #         if (ord(characters[i]) & 0xC0) == 0xC0:
# #             # Find the end index of the multi-byte sequence
# #             j = i + 1
# #             while (j < len(characters)) and ((ord(characters[j]) & 0xC0) == 0x80):
# #                 j += 1

# #             # Reverse the multi-byte sequence
# #             characters[i:j+1] = characters[i:j+1][::-1]

# #             # Move to the next character after the multi-byte sequence
# #             i = j + 1
# #         else:
# #             # Move to the next character
# #             i += 1

# #     # Reconstruct the reversed string
# #     reversed_string = ''.join(characters)

# #     return reversed_string

# # # Example usage
# # message = "Hello, 你好, नमस्ते"
# # reversed_message = reverse_string_multibyte(message)
# # print(reversed_message)  # Output: "एत्समन ,好你 ,olleH"


# # #---------Reverse a string using bitwise operator XOR or without using any built-in string manipulation functions----

# # def reverse_string_bitwise(input_string):
# #     # Convert the string to a list of characters
# #     characters = list(input_string)

# #     # Get the indices of the first and last characters
# #     left = 0
# #     right = len(characters) - 1

# #     # Reverse the string using bitwise XOR
# #     while left < right:
# #         # Swap the characters using bitwise XOR
# #         characters[left] = chr(ord(characters[left]) ^ ord(characters[right]))
# #         characters[right] = chr(ord(characters[left]) ^ ord(characters[right]))
# #         characters[left] = chr(ord(characters[left]) ^ ord(characters[right]))

# #         # Move the indices towards the center
# #         left += 1
# #         right -= 1

# #     # Convert the list of characters back to a string
# #     reversed_string = ''.join(characters)

# #     return reversed_string

# # # Example usage
# # message = "Hello, World!"
# # reversed_message = reverse_string_bitwise(message)
# # print(reversed_message)  # Output: "!dlroW ,olleH"


# # #----------Reverse a string using bitwise operator AND or without using any built-in string manipulation functions

# # def reverse_string_bitwise(input_string):
# #     # Convert the string to a list of characters
# #     characters = list(input_string)

# #     # Get the indices of the first and last characters
# #     left = 0
# #     right = len(characters) - 1

# #     # Reverse the string using bitwise AND
# #     while left < right:
# #         # Swap the characters using bitwise AND
# #         characters[left] = chr(ord(characters[left]) & ord(characters[right]))
# #         characters[right] = chr(ord(characters[left]) & ord(characters[right]))
# #         characters[left] = chr(ord(characters[left]) & ord(characters[right]))

# #         # Move the indices towards the center
# #         left += 1
# #         right -= 1

# #     # Convert the list of characters back to a string
# #     reversed_string = ''.join(characters)

# #     return reversed_string

# # # Example usage
# # message = "Hello, World!"
# # reversed_message = reverse_string_bitwise(message)
# # print(reversed_message)  # Output: "!dlroW ,olleH"


# # #----------Reverse a string using bitwise operator NOT or without using any built-in string manipulation functions-------

# # def reverse_string_bitwise(input_string):
# #     # Convert the string to a list of characters
# #     characters = list(input_string)

# #     # Get the indices of the first and last characters
# #     left = 0
# #     right = len(characters) - 1

# #     # Reverse the string using bitwise NOT
# #     while left < right:
# #         # Swap the characters using bitwise NOT
# #         characters[left] = chr(~ord(characters[left]))
# #         characters[right] = chr(~ord(characters[right]))
# #         characters[left] = chr(~ord(characters[left]))

# #         # Move the indices towards the center
# #         left += 1
# #         right -= 1

# #     # Convert the list of characters back to a string
# #     reversed_string = ''.join(characters)

# #     return reversed_string

# # # Example usage
# # message = "Hello, World!"
# # reversed_message = reverse_string_bitwise(message)
# # print(reversed_message)  # Output: "!dlroW ,olleH"


# # #-----------reverse a string that contains right-to-left (RTL) characters or bidirectional text without affecting their order------

# # def reverse_string_bidirectional(input_string):
# #     # Split the string into segments of RTL text and non-RTL text
# #     segments = []
# #     current_segment = ""
# #     is_rtl_segment = False

# #     for char in input_string:
# #         is_rtl = is_rtl_character(char)

# #         if is_rtl != is_rtl_segment:
# #             segments.append(current_segment)
# #             current_segment = char
# #             is_rtl_segment = is_rtl
# #         else:
# #             current_segment += char

# #     segments.append(current_segment)

# #     # Reverse each segment individually, preserving the order of RTL segments
# #     reversed_segments = [segment[::-1] if is_rtl_character(segment[0]) else segment for segment in segments]

# #     # Join the reversed segments back into a string
# #     reversed_string = "".join(reversed_segments)

# #     return reversed_string


# # def is_rtl_character(char):
# #     # Add your logic here to determine if a character is RTL
# #     # You can use character properties or Unicode ranges for identification
# #     # This is a simplified example assuming RTL characters start with the RTL mark (U+200F)
# #     return ord(char) >= 0x200F


# # # Example usage
# # message = "Hello, مرحبا بك"
# # reversed_message = reverse_string_bidirectional(message)
# # print(reversed_message)  # Output: "كب ابحرم ,olleH"




# # #-------Handle and reversing a string that contains surrogate pairs, 
# # # which are used to represent characters outside the Basic Multilingual Plane (BMP) in Unicode-----

# # def reverse_string_with_surrogate_pairs(input_string):
# #     # Split the string into individual characters
# #     characters = list(input_string)

# #     # Reverse the string while considering surrogate pairs
# #     left = 0
# #     right = len(characters) - 1

# #     while left < right:
# #         # Check if the current characters form a surrogate pair
# #         if is_surrogate_pair(characters[left], characters[left + 1]):
# #             # Swap the surrogate pair characters
# #             characters[left], characters[left + 1] = characters[left + 1], characters[left]
# #             left += 2
# #         else:
# #             # Swap the non-surrogate characters
# #             characters[left], characters[right] = characters[right], characters[left]
# #             left += 1
# #             right -= 1

# #     # Convert the list of characters back to a string
# #     reversed_string = "".join(characters)

# #     return reversed_string


# # def is_surrogate_pair(char1, char2):
# #     # Check if the two characters form a surrogate pair
# #     return (
# #         "\uD800" <= char1 <= "\uDBFF"
# #         and "\uDC00" <= char2 <= "\uDFFF"
# #     )


# # # Example usage
# # message = "Hello, \U0001F600"
# # reversed_message = reverse_string_with_surrogate_pairs(message)
# # print(reversed_message)  # Output: "😀 ,olleH"


# import gc

# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"MyClass({self.name})"

# # Create instances of MyClass
# obj1 = MyClass("Object 1")
# obj2 = MyClass("Object 2")

# # Add references to a cyclic data structure (causing memory leak)
# obj1.ref = obj2
# obj2.ref = obj1

# # Remove the references
# del obj1
# del obj2

# # Manually trigger garbage collection
# gc.collect()

# # Check the garbage collector's statistics
# print(gc.get_stats())
# print(gc.get_referents())
# print(gc.is_tracked())

# import gc

# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"MyClass({self.name})"

# # Create instances of MyClass
# obj1 = MyClass("Object 1")
# obj2 = MyClass("Object 2")

# # Add references to a cyclic data structure (causing memory leak)
# obj1.ref = obj2
# obj2.ref = obj1

# # Remove the references
# del obj1
# del obj2

# # Check if objects are tracked by the garbage collector
# is_tracked_obj1 = gc.is_tracked(obj1)
# is_tracked_obj2 = gc.is_tracked(obj2)

# print(f"obj1 is tracked: {is_tracked_obj1}")
# print(f"obj2 is tracked: {is_tracked_obj2}")

# # Manually trigger garbage collection
# gc.collect()

# # Check if objects are tracked after garbage collection
# is_tracked_obj1 = gc.is_tracked(obj1)
# is_tracked_obj2 = gc.is_tracked(obj2)

# print(f"obj1 is tracked after GC: {is_tracked_obj1}")
# print(f"obj2 is tracked after GC: {is_tracked_obj2}")

# import gc

# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"MyClass({self.name})"

# # Create instances of MyClass
# obj1 = MyClass("Object 1")
# obj2 = MyClass("Object 2")

# # Add references to a cyclic data structure (causing memory leak)
# obj1.ref = obj2
# obj2.ref = obj1

# # Check if objects are tracked by the garbage collector
# is_tracked_obj1 = gc.is_tracked(obj1)
# is_tracked_obj2 = gc.is_tracked(obj2)

# print(f"obj1 is tracked: {is_tracked_obj1}")
# print(f"obj2 is tracked: {is_tracked_obj2}")

# # Remove the references
# del obj1
# del obj2

# # Manually trigger garbage collection
# gc.collect()

# # Check if objects are tracked after garbage collection
# is_tracked_obj1 = gc.is_tracked(obj1)
# is_tracked_obj2 = gc.is_tracked(obj2)

# print(f"obj1 is tracked after GC: {is_tracked_obj1}")
# print(f"obj2 is tracked after GC: {is_tracked_obj2}")

# import gc

# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"MyClass({self.name})"

# # Create instances of MyClass
# obj1 = MyClass("Object 1")
# obj2 = MyClass("Object 2")

# # Add references to a cyclic data structure (causing memory leak)
# obj1.ref = obj2
# obj2.ref = obj1

# # Check if objects are tracked by the garbage collector
# is_tracked_obj1 = gc.is_tracked(obj1)
# is_tracked_obj2 = gc.is_tracked(obj2)

# print(f"obj1 is tracked: {is_tracked_obj1}")
# print(f"obj2 is tracked: {is_tracked_obj2}")

# # Manually trigger garbage collection
# gc.collect()

# # Check if objects are tracked after garbage collection
# is_tracked_obj1 = gc.is_tracked(obj1)
# is_tracked_obj2 = gc.is_tracked(obj2)

# print(f"obj1 is tracked after GC: {is_tracked_obj1}")
# print(f"obj2 is tracked after GC: {is_tracked_obj2}")

# import gc

# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"MyClass({self.name})"

# # Create instances of MyClass
# obj1 = MyClass("Object 1")
# obj2 = MyClass("Object 2")

# # Add references to a cyclic data structure (causing memory leak)
# obj1.ref = obj2
# obj2.ref = obj1

# # Check if objects are tracked by the garbage collector
# is_tracked_obj1 = gc.is_tracked(obj1)
# is_tracked_obj2 = gc.is_tracked(obj2)

# print(f"obj1 is tracked: {is_tracked_obj1}")
# print(f"obj2 is tracked: {is_tracked_obj2}")

# # Manually trigger garbage collection
# gc.collect()

# # Check if objects are tracked after garbage collection
# is_tracked_obj1 = gc.is_tracked(obj1)
# is_tracked_obj2 = gc.is_tracked(obj2)

# print(f"obj1 is tracked after GC: {is_tracked_obj1}")
# print(f"obj2 is tracked after GC: {is_tracked_obj2}")


# # Delete obj1 and obj2
# del obj1
# del obj2

# # Check if garbage is deleted and untrackable
# garbage_objects = gc.garbage
# is_deleted = obj1 in garbage_objects and obj2 in garbage_objects

# print(f"Garbage is deleted and untrackable: {is_deleted}")

# import gc

# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"MyClass({self.name})"

# # Create instances of MyClass
# obj1 = MyClass("Object 1")
# obj2 = MyClass("Object 2")

# # Add references to a cyclic data structure (causing memory leak)
# obj1.ref = obj2
# obj2.ref = obj1

# # Check if objects are tracked by the garbage collector
# is_tracked_obj1 = None
# is_tracked_obj2 = None

# try:
#     is_tracked_obj1 = gc.is_tracked(obj1)
#     is_tracked_obj2 = gc.is_tracked(obj2)
# except NameError:
#     pass

# print(f"obj1 is tracked: {is_tracked_obj1}")
# print(f"obj2 is tracked: {is_tracked_obj2}")

# # Delete the objects
# del obj1
# del obj2

# # Manually trigger garbage collection
# gc.collect()

# # Check if objects are tracked after garbage collection
# is_tracked_obj1 = None
# is_tracked_obj2 = None

# try:
#     is_tracked_obj1 = gc.is_tracked(obj1)
#     is_tracked_obj2 = gc.is_tracked(obj2)
# except NameError:
#     pass

# # Check if objects are deleted and untrackable
# is_deleted_obj1 = obj1 is None
# is_deleted_obj2 = obj2 is None

# print(f"obj1 is tracked after GC: {is_tracked_obj1}")
# print(f"obj2 is tracked after GC: {is_tracked_obj2}")
# print(f"obj1 is deleted: {is_deleted_obj1}")
# print(f"obj2 is deleted: {is_deleted_obj2}")


# import gc

# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"MyClass({self.name})"

# # Create instances of MyClass
# objects = [MyClass("Object 1"), MyClass("Object 2")]

# # Add references to a cyclic data structure (causing memory leak)
# objects[0].ref = objects[1]
# objects[1].ref = objects[0]

# # Check if objects are tracked by the garbage collector
# is_tracked_objects = [gc.is_tracked(obj) for obj in objects]

# print("Objects are tracked:", is_tracked_objects)

# # Delete the objects
# del objects

# # Manually trigger garbage collection
# gc.collect()

# # Check if objects are tracked after garbage collection
# is_tracked_objects = [gc.is_tracked(obj) for obj in object]

# # Check if objects are deleted and untrackable
# is_deleted_objects = [obj is None for obj in object]

# print("Objects are tracked after GC:", is_tracked_objects)
# print("Objects are deleted:", is_deleted_objects)


# # Prompt the user for input
# n = int(input("Enter the number to partition: "))

# # Create a matrix to store the intermediate results
# dp = [[0] * (n + 1) for _ in range(n + 1)]

# # Initialize the base cases
# for i in range(1, n + 1):
#     dp[i][1] = 1  # Each integer can be partitioned into itself

# # Compute the number of ways to partition the sum
# for i in range(2, n + 1):
#     for j in range(1, i):
#         dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]

# # Calculate the total number of ways
# ways = sum(dp[n][1:])

# # Print the result
# print("Number of ways to partition", n, ":", ways)


# def find_partitions(n):
#   """Finds all possible partitions of a number.

#   Args:
#     n: The number to partition.

#   Returns:
#     A list of all possible partitions.
#   """

#   # Create a table to store the number of partitions for each possible sum.
#   dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

#   # Initialize the table.
#   for i in range(n + 1):
#     dp[i][0] = 1

#   # Fill in the table.
#   for i in range(1, n + 1):
#     for j in range(1, i + 1):
#       dp[i][j] = dp[i - j][j] + dp[i][j - 1]

#   # Find all possible partitions.
#   partitions = []
#   for i in range(1, n + 1):
#     for j in range(1, i + 1):
#       if dp[i][j] > 0:
#         partitions.append([j] * j for _ in range(dp[i][j]))

#   return partitions


# def main():
#   n = 5
#   partitions = find_partitions(n)

#   for partition in partitions:
#     print(partition)


# if __name__ == "__main__":
#   main()


# # Prompt the user for input
# n = int(input("Enter the number to partition: "))

# # Create a matrix to store the intermediate results
# dp = [[0] * (n + 1) for _ in range(n + 1)]

# # Initialize the base cases
# for i in range(1, n + 1):
#     dp[i][1] = 1  # Each integer can be partitioned into itself

# # Compute the number of ways to partition the sum and store the partitions
# partitions = []
# for i in range(2, n + 1):
#     for j in range(1, i):
#         dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
#         if dp[i][j] > 0:
#             partitions.append((i, j))

# # Calculate the total number of ways
# ways = sum(dp[n][1:])

# # Print the partitions
# print("Partitions:")
# for partition in partitions:
#     print(partition)

# # Print the result
# print("Number of ways to partition", n, ":", ways)


# # Prompt the user for input
# n = int(input("Enter the number to partition: "))

# # Create a matrix to store the intermediate results
# dp = [[0] * (n + 1) for _ in range(n + 1)]

# # Initialize the base cases
# for i in range(1, n + 1):
#     dp[i][1] = 1  # Each integer can be partitioned into itself

# # Compute the number of ways to partition the sum and store the partitions
# partitions = []
# for i in range(2, n + 1):
#     for j in range(1, i):
#         dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
#         if dp[i][j] > 0:
#             partitions.append((i, j))

# # Calculate the total number of ways
# ways = sum(dp[n][1:])

# # Print the partitions
# print("Partitions:")
# for partition in partitions:
#     num_parts = partition[1]
#     parts = [1] * (n - num_parts) + [num_parts]
#     print(parts)

# # Print the result
# print("Number of ways to partition", n, ":", ways)



# # Prompt the user for input
# n = int(input("Enter the number to partition: "))

# # Create a matrix to store the intermediate results
# dp = [[0] * (n + 1) for _ in range(n + 1)]

# # Initialize the base cases
# for i in range(1, n + 1):
#     dp[i][1] = 1  # Each integer can be partitioned into itself

# # Compute the number of ways to partition the sum and store the partitions
# partitions = set()
# for i in range(2, n + 1):
#     for j in range(1, i):
#         dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
#         if dp[i][j] > 0:
#             partitions.add(tuple(sorted([j, i - j])))

# # Calculate the total number of ways
# ways = sum(dp[n][1:])

# # Print the partitions
# print("Partitions:")
# for partition in partitions:
#     parts = list(partition) + [1] * (n - sum(partition))
#     print(parts)

# # Print the result
# print("Number of ways to partition", n, ":", ways)



# # Prompt the user for input
# n = int(input("Enter the number to partition: "))

# # Create a matrix to store the intermediate results
# dp = [[0] * (n + 1) for _ in range(n + 1)]

# # Initialize the base cases
# for i in range(1, n + 1):
#     dp[i][i] = 1  # Each integer can be partitioned into itself

# # Compute the number of ways to partition the sum and store the partitions
# partitions = set([(i,) for i in range(1, n + 1)])
# for i in range(2, n + 1):
#     temp_partitions = set()
#     for j in range(1, i):
#         for partition in partitions:
#             if j >= partition[-1]:
#                 temp_partitions.add(partition + (j,))
#         temp_partitions.add((j,))
#     partitions.update(temp_partitions)

# # Calculate the total number of ways
# ways = len(partitions)

# # Print the partitions
# print("Partitions:")
# for partition in partitions:
#     parts = list(partition) + [1] * (n - sum(partition))
#     print(parts)

# # Print the result
# print("Number of ways to partition", n, ":", ways)

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number
    
# solution = Solution()
# roman_numeral = 'MXCD'
# result = solution.romanToInt(roman_numeral)
# print(f"The integer value of {roman_numeral} is: {result}")


# def isStrobogrammatic(num: str) -> bool:
#     strobogrammatic_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
#     left, right = 0, len(num) - 1
    
#     while left <= right:
#         if num[left] not in strobogrammatic_map or strobogrammatic_map[num[left]] != num[right]:
#             return False
#         left += 1
#         right -= 1
    
#     return True

# # Take user input
# number = input("Enter a number: ")

# # Check if the number is strobogrammatic
# if isStrobogrammatic(number):
#     print("The number is strobogrammatic.")
# else:
#     print("The number is not strobogrammatic.")

# str1 = "HelloWorld Hahaha"
# swapped_str1 = ''
# for char in str1:
#     if char.islower():
#         swapped_str1 += char.upper()
#     elif char.isupper():
#         swapped_str1 += char.lower()
#     else:
#         swapped_str1 += char
# print (swapped_str1)

def move_zeros_to_end(array):
    if len(array) <= 1:
        return array

    if array[0] == 0:
        return move_zeros_to_end(array[1:]) + [0]
    else:
        return [array[0]] + move_zeros_to_end(array[1:])

array = [1, 2, 0, 3, 0, 4, 0, 5, 5, 6]
new_array = move_zeros_to_end(array)

print(new_array)


