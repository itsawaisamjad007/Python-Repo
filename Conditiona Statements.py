# Condition Statements :-
                # Conditional statements let program to decide which action to take
                # based on Conditions.
#    * if statement
#    * else statement
#    * elif statement
#    * nested statement

a = 5
b = 10
if a == b:
    print("a is equal to b")
    if a % 2 == 0:                 # nested if statement
        print("a is even")

else:
    print("a is not equal to b")