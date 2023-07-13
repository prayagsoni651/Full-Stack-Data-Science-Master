#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. What exactly is []?""
"""
A list or an array is a data structure that can hold multiple values of different types. By using square brackets with no elements inside, you indicate that the list or array is empty, meaning it doesn't contain any elements.

Here's an example in Python:


my_list = []  # An empty list



let myArray = [];  // An empty array

Empty lists or arrays can be useful when you want to initialize a data structure to be populated later or when you want to clear out the existing elements of a list or array.

"""


# In[2]:


# 9. What are the list concatenation and list replication operators?
"""
List Concatenation Operator (+):
The plus operator allows you to concatenate or join two lists together, creating a new list that contains all the elements from both lists in the order they appear.

Here's an example:


list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]
In this example, the two lists list1 and list2 are concatenated using the plus operator, and the resulting list is stored in the variable result.

List Replication Operator (*):
The asterisk operator allows you to replicate a list by a specified number of times. It creates a new list that repeats the elements of the original list.

Here's an example:


list1 = [1, 2, 3]
replicated_list = list1 * 3
print(replicated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]"""


# In[3]:


# 10. What is difference between the list methods append() and insert()?



"""

append() method:
The append() method is used to add an element to the end of a list. It takes a single argument, which is the element to be added, and appends it to the end of the list.

Here's an example:


my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
In this example, the append() method is called on my_list with the argument 4, and it adds 4 to the end of the list.

insert() method:
The insert() method is used to add an element at a specific position within the list. It takes two arguments: the first argument is the index where the element should be inserted, and the second argument is the element itself.

Here's an example:


my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]

"""


# In[4]:


# 11. What are the two methods for removing items from a list?
"""

There are two commonly used methods for removing items from a list in Python:

remove() method:
The remove() method is used to remove the first occurrence of a specified value from the list. It takes a single argument, which is the value to be removed.

Here's an example:


my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2, 4]
In this example, the remove() method is called on my_list with the argument 2. It removes the first occurrence of 2 from the list, modifying the list in-place.

It's important to note that if the specified value is not present in the list, a ValueError will be raised. So, it's a good practice to check if the value exists in the list before calling the remove() method.

pop() method:
The pop() method is used to remove and return an element from a specific index in the list. It takes an optional argument, which is the index of the element to be removed. If no index is provided, it removes and returns the last element of the list.

Here's an example:


my_list = [1, 2, 3, 4]
popped_element = my_list.pop(1)
print(my_list)         # Output: [1, 3, 4]
print(popped_element)  # Output: 2
In this example, the pop() method is called on my_list with the argument 1. It removes the element at index 1 (which is 2) from the list and returns it. The list is modified in-place.

If no argument is provided to pop(), it will remove and return the last element of the list:

my_list = [1, 2, 3]
popped_element = my_list.pop()
print(my_list)         # Output: [1, 2]
print(popped_element)  # Output: 3
"""


# In[6]:


# 12. Describe how list values and string values are identical

"""
Sequences:
Both lists and strings are sequences in Python, which means they are ordered collections of elements. Elements in both lists and strings can be accessed by their indices.

Indexing and Slicing:
Both lists and strings support indexing and slicing operations. You can access individual elements of a list or a string by their index, and you can extract sub-sequences (slices) using the slicing syntax.

Example:


my_list = [1, 2, 3, 4]
my_string = "Hello, World!"

print(my_list[0])            # Output: 1
print(my_string[7])          # Output: W

print(my_list[1:3])          # Output: [2, 3]
print(my_string[0:5])        # Output: Hello
Iteration:
Both lists and strings can be iterated over using loops, such as the for loop. You can iterate through each element in a list or string and perform operations on them.

Example:


my_list = [1, 2, 3]
my_string = "Hello"

for item in my_list:
    print(item)

for char in my_string:
    print(char)
Length:
Both lists and strings have a length that can be determined using the len() function. The length represents the number of elements (characters in the case of strings) contained within the sequence.

Example:


my_list = [1, 2, 3, 4]
my_string = "Hello"

print(len(my_list))        # Output: 4
print(len(my_string))      # Output: 5
"""


# In[7]:


# 13. What's the difference between tuples and lists?

"""


Tuples and lists are both types of sequences in Python, but they have some important differences in terms of mutability, syntax, and usage:

Mutability:
The main difference between tuples and lists is that tuples are immutable, while lists are mutable. This means that once a tuple is created, its elements cannot be modified, added, or removed. In contrast, lists can be modified by changing, adding, or removing elements after creation.

Syntax:
Tuples are defined using parentheses (), or without any delimiters by default if the parentheses are omitted. Elements within a tuple are separated by commas. Lists, on the other hand, are defined using square brackets [], and elements within a list are also separated by commas.

Example of tuple:


my_tuple = (1, 2, 3)
Example of list:

my_list = [1, 2, 3]
Usage:
Tuples are commonly used to represent collections of related values that should not be modified, such as coordinates, settings, or database records. They are often used when you want to ensure that the sequence of elements remains unchanged. Tuples are also frequently used in functions to return multiple values as a single entity.

Lists, on the other hand, are more versatile and commonly used when you need a mutable collection of elements. Lists allow you to add, modify, or remove elements freely. They are used in situations where you need to perform operations like sorting, appending, or iterating over the elements.

Performance:
Tuples are generally more lightweight and efficient than lists in terms of memory usage and performance. Since tuples are immutable, Python can optimize them more effectively. Lists, being mutable, require additional memory allocation and operations when elements are added, removed, or modified."""


# In[8]:


#  17. How do you distinguish between copy.copy() and copy.deepcopy()?
"""
copy.copy():
The copy.copy() function performs a shallow copy of an object. It creates a new object and then copies the references of the original object's elements to the new object. If the original object contains references to other objects, the copied object will also contain references to the same objects.

Example:


import copy

original_list = [1, 2, [3, 4]]
copied_list = copy.copy(original_list)

original_list[2].append(5)

print(original_list)   # Output: [1, 2, [3, 4, 5]]
print(copied_list)     # Output: [1, 2, [3, 4, 5]]
In this example, copy.copy() is used to create copied_list from original_list. When we modify the nested list original_list[2] by appending 5, the change is reflected in both original_list and copied_list. This is because both lists contain references to the same nested list object.

copy.deepcopy():
The copy.deepcopy() function, on the other hand, performs a deep copy of an object. It creates a new object and recursively copies all the elements and nested objects of the original object, ensuring that no references to the original objects remain in the copied object. This means that modifications made to the original object or its nested objects will not affect the copied object.

Example:


import copy

original_list = [1, 2, [3, 4]]
copied_list = copy.deepcopy(original_list)

original_list[2].append(5)

print(original_list)   # Output: [1, 2, [3, 4, 5]]
print(copied_list)     # Output: [1, 2, [3, 4]]
"""


# In[1]:


# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

"""
Variables that "contain" list values are not lists themselves but rather references or pointers to the list objects in memory. In many programming languages, including Python, variables are used to store memory addresses where the list objects are stored rather than directly containing the list data.

When you assign a list to a variable, the variable stores the memory address of the list object. This allows you to access and manipulate the list using the variable. Multiple variables can refer to the same list object, so changes made through one variable will be reflected when accessing the list through another variable.

For example, consider the following code snippet in Python:

my_list = [1, 2, 3]
another_list = my_list

# Modifying the list using the 'my_list' variable
my_list.append(4)

print(another_list)  # Output: [1, 2, 3, 4]
"""


# In[2]:


# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?
"""
To convert a list value to its tuple form, you can use the tuple() function. It takes an iterable (such as a list) as an argument and returns a tuple containing the elements of the iterable. Here's an example:


my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)

print(my_tuple)  # Output: (1, 2, 3, 4, 5)
In the example above, tuple(my_list) converts the list my_list to a tuple, and the resulting tuple is assigned to the variable my_tuple.

To convert a tuple value to its list form, you can use the list() function. It also takes an iterable (such as a tuple) as an argument and returns a list containing the elements of the iterable. Here's an example:


my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)

print(my_list)  # Output: [1, 2, 3, 4, 5]
"""


# In[3]:


# 14. How do you type a tuple value that only contains the integer 42?

"""
In Python, you can create a tuple value that only contains the integer 42 by using parentheses () and placing the integer inside them. Here's an example:


my_tuple = (42,)
In the example above, (42,) creates a tuple with a single element, which is the integer 42. The comma after 42 is important to indicate that it's a tuple with one element. Without the comma, Python would interpret it as just an integer.
"""


# In[27]:


# 3. What is the value of spam[int(int('3' * 2) / 11)]?
# spam[int(int('3' * 2) / 11)]

spam =[int(int('3' * 2) / 11)]
print(spam)


# In[2]:


# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# 4. What is the value of spam[-1]?

spam = ['a','b','c','d']
print(spam[-1])


# In[3]:


# 5. What is the value of spam[:2]?

spam = ['a','b.','c','d']
print(spam[:2])


# In[9]:


# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# 6. What is the value of bacon.index('cat')?



# In[24]:


list = [3.14, 'cat' ,11, 'cat', True]
list.index('cat')



# In[20]:


#  7. How does bacon.append(99) change the look of the list value in bacon?

bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99)
print(bacon)


# In[26]:


# 8. How does bacon.remove('cat') change the look of the list in bacon?
list = [3.14, 'cat', 11, 'cat', True]
list.remove('cat')
print(list)


# In[33]:


# 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? 
# (Assume [2, 4, 6, 8, 10] are in spam.)

spam = [2,4,6,8,10]
spam[3] = 'hello'
print(spam)


# In[ ]:





# In[ ]:




