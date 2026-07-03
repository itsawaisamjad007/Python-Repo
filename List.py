#Data type used to store character string or any other data type in ordered form
#Data can be modified deleted(mutable)

EList = [] #empty List
my_List = [1,2,3,"python"] #with elements of any other data type

#accessing elements

print(my_List) #to print whole elements

#Elements store in such sequence that 1 is stored on 0th index & 2 stored in 1st index
# and so on

print(my_List[0]) #to print only (1)

print(my_List[1:4])  # to print elements from (2 to python)

# To modify List after created
my_List.append(5) #append is used to add data at last

my_List.insert(0, 5) #insert is used to add data at any index number

add=6,7,8 # To use extend , first we save elements in any variable
my_List.extend(add) # To add multiple element in list

#To remove any element from list
my_List.pop(0) #To remove element reference to index number

my_List.remove("python") #To remove element reference to its name

my_List.clear()    #To remove all elements from List