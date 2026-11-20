# string slicing and operations
name = "SufiyanBeg"
length = len(name)
print("Length of the string is: ",length)
print(name[0:6]) # this will print the first 6 characters of the string
print(name[0:-3])
print(name[-3:-1]) # this will print the last 3 characters of the string except the last character
print(name[-1:len(name)-3]) # this will print the last 3 characters of the string except the last character

# Quick quiz:
nm="SufiyanBeg" 
print(nm)
print(nm[-10:-1:2]) # this will print the first 10 characters of the string except the last character with a step of 2
