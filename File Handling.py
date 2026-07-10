
# All about file handling:-

# Allow programs to manage file - open ( file name , mode )

 # Modes :-

   # * r - read ( default )
   # * w - write ( Overwrite )
   # * a - appends (add to ends)
   # * r+ - read and write

   # Practical :-
    # with is a function use to manage all resources .

    # 1. Writing to a file :-
with open("sample.txt" , "w" ) as file:  # First we open to create a file name "file"
    file.write("Hello World .\n")             # Then we write a message in it .

 # 2. Reading from a file :-
with open("sample.txt" , "r" ) as file:  # Open a file in read mode .
     content = file.read()               # To save file read in content variable it is optional
                                         # we can direct print "file.read"
     print(content)

  # 3. Appending to a file :-
with open("sample.txt" , "a" ) as file:
    file.write("What are you doing in Lahore .\n")    # To add content at last in file


# 2.  Again Reading from a file and print modified contents :-

with open("sample.txt", "r") as file:  # Open a file in read mode .
    content = file.read()
    print(content)

  # 4. Using r+ mode to modify file from beginning :-

with open("sample.txt", "r+") as file:
    file.write("Overwritten content.\n")                 # Overwrites beginning of file
    file.seek(0)                                         # To go back to the start
modified_content = content
print("\n Content after r+ modification")
print(modified_content)
