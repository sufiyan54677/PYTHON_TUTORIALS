# STRING METHODS IN PYTHON

#  srtings are immutable in python. we can use the following methods to perform operations on strings:

name = "SufiyanBeg!!!!!!!!!!!!!!!!"

print(name.upper()) # this will print the string in uppercase
print(name.lower()) # this will print the string in lowercase
print(name.strip()) # this will remove any whitespace from the beginning or end of the string
print(name.replace("SufiyanBeg", "Mohammed")) # this will replace a substring with another substring
print(name.split(",")) # this will split the string into a list of substrings
print(name.rsplit("!")) # this will split the string into a list of substrings from the right
print(name.split(" ")) # this will split the string into a list of substrings based on whitespace
print(name.find("Beg")) # this will return the index of the first occurrence of the substring

# Capitalization

bloghearing = "hello, my dog is cute"
print(bloghearing.capitalize()) # this will capitalize the first character of the string

# Center(width, fillchar)
str1 = "hello"
print(len(str1)) # this will print the length of the string
print(len(str1.center(20))) # this will center the string in a field of

# Count(substring, start, end)
str2 = "hello, my dog is cute !!!!!"  
print(str2.count("e")) # this will count the number of occurrences of the substring in the string

# ENDSWITH(suffix)
print(str2.endswith("!!!!!")) # this will return True if the string ends with the specified suffix
print(str2.endswith("cute")) # this will return False if the string does not end with the specified suffix
print(str2.endswith("cute", 6, 20)) # this will return True if the string ends with the specified suffix in the specified range

# FIND(substring, start, end)
print(str2.find("cute")) # this will return the index of the first occurrence of the substring
print(str2.find("me")) # this will return -1 if the substring is not found

# isalnum() - this will return True if all characters in the string are alphanumeric

str3 = "hello123"
print(str3.isalnum()) # this will return True if all characters in the string are alphanumeric
str4 = "hello"
str5 = " hello 123"
print(str4.isalnum()) # this will return True if all characters in the string are alphanumeric
print(str5.isalnum()) # this will return False if all characters in the string are not alphanumeric\
str6 = "      "
print(str6.isalnum()) # this will return False if all characters in the string are not alphanumeric

# isalpha() - this will return True if all characters in the string are alphabetic
str7 = "Word Health Organization"
print(str7.istitle()) # this will return True if the string is in title case    

# startswith(prefix, start, end)
str8 = "pyhton is a programing language"
print(str8.startswith("pyhton")) # this will return True if the string starts with the specified prefix

# swapcase() - this will return a new string with all uppercase characters converted to lowercase and vice versa
str9 = "Hello World"    
print(str9.swapcase()) # this will return a new string with all uppercase characters converted to lowercase and vice versa

#  Title() - this will return a new string with the first character of each word capitalized
str10 = "python is a programming language"
print(str10.title()) # this will return a new string with the first character of each word capitalized