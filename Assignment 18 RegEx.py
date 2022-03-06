#!/usr/bin/env python
# coding: utf-8

# # Python – Check whether a string starts and ends with the same character or not (using Regular Expression)

# In[1]:


# import re module as it provides
# support for regular expressions
import re
 
# the regular  expression
regex = r'^[a-z]$|^([a-z]).*\1$'
 
# function for checking the string
def check(string):
 
    # pass the regular expression
    # and the string in the search() method
    if(re.search(regex, string)): 
        print("Valid") 
    else: 
        print("Invalid") 
 
if __name__ == '__main__' :
 
    sample1 = "abba"
    sample2 = "a"
    sample3 = "abcd"
 
    check(sample1)
    check(sample2)
    check(sample3)


# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# In[2]:


def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))


# Python | Remove all duplicates words from a given sentence

# In[4]:


from collections import Counter
 
def remov_duplicates(input):
 
    # split input string separated by space
    input = input.split(" ")
 
    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    UniqW = Counter(input)
    print(UniqW)
    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    print (s)
 
# Driver program
if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    remov_duplicates(input)


# Python | Remove all characters except letters and numbers
# 

# In[6]:


# initialising string
ini_string = "123abcjw:, .@! eiw"
  
# printing initial string
print ("initial string : ", ini_string)
  
# function to demonstrate removal of characters
# which are not numbers and alphabets using re
  
result = re.sub('[\W_]+', '', ini_string)
  
# printing final string
print ("final string...", result)


# Python Regex | Program to accept string ending with alphanumeric character

# In[7]:


# Make a regular expression to accept string
# ending with alphanumeric character
regex = '[a-zA-z0-9]$'
     
# Define a function for accepting string
# ending with alphanumeric character
def check(string):
 
     # pass the regular expression
     # and the string in search() method
    if(re.search(regex, string)):
        print("Accept")
         
    else:
        print("Discard")
     
 
# Driver Code
if __name__ == '__main__' :
     
    # Enter the string
    string = "ankirai@"
     
    # calling run function
    check(string)
 
    string = "ankitrai326"
    check(string)
 
    string = "ankit."
    check(string)
 
    string = "geeksforgeeks"
    check(string)


# How to check if a string starts with a substring using regex in Python?

# In[8]:


def find(string, sample) :
    
  # check substring present 
  # in a string or not
  if (sample in string):
  
      y = "^" + sample
  
      # check if string starts 
      # with the substring
      x = re.search(y, string)
  
      if x :
          print("string starts with the given substring")
  
      else :
          print("string doesn't start with the given substring")
  
  else :
      print("entered string isn't a substring")
  
  
# Driver code
string = "geeks for geeks makes learning fun"  
sample = "geeks"
  
# function call
find(string, sample)
  
sample = "makes"
  
# function call
find(string, sample)


# Check if an URL is valid or not using Regular Expression

# In[9]:


# Function to validate URL
# using regular expression
def isValidURL(str):
 
    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
 
# Driver code
 
# Test Case 1:
url = "https://www.geeksforgeeks.org"
 
if(isValidURL(url) == True):
    print("Yes")
else:
    print("No")


# Python program to validate an Ip address

# In[10]:


# Make a regular expression
# for validating an Ip-address
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
 
 
     
# Define a function for
# validate an Ip address
def check(Ip):
 
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, Ip)):
        print("Valid Ip address")
         
    else:
        print("Invalid Ip address")
     
 
# Driver Code
if __name__ == '__main__' :
     
    # Enter the Ip address
    Ip = "192.168.0.1"
     
    # calling run function
    check(Ip)
 
    Ip = "110.234.52.124"
    check(Ip)
 
    Ip = "366.1.2.2"
    check(Ip)


# In[ ]:




