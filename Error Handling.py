 # Error Handling :-
 # * Try
 # * Except
 # * Finally

try:
    file = open("file.txt","r")
except FileNotFoundError:
    print("File not found.")

finally:
    print("Closing file if opened.")
    file.close() if 'file' in locals() else None

