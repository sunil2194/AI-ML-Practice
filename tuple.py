# A tuple is an ordered immutable collection of items. Tuples are defined by having values between parentheses ( ).
groceries = ("milk", "eggs")

# If you try to change a value like this: groceries[0] = "bread", you will get an error because tuples are immutable. You cannot change the values of a tuple after it has been created.
# Python will crash with a TypeError because tuples cannot be modified!

print(groceries)
# You cannot change an item (tuples are immutable)
#groceries[0] = "bread"  # This will raise a TypeError