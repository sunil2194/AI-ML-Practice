#combining Variables and text
name = "Alice"
age = 30


#Print Name and Age
#print(name,age)

#Print Age and Name with msg, Syntax , in between the variables and text
# My name is Alice and my age is 30
#print("My name is:", name, "and my age is:", age)

#The result variable will consider this as a tuple data type since we have used commas in between the variables and text.

#result = "My name is:", name, "and my age is:", age
#print(result)

# + Operator
# Python thinks to add an integer (30) to a string ("My age is ")
# + is used for concatenation of strings or the addition of numbers. Python will not automatically convert data types for you when using the + operator.
#print("My name is: " + name + " and my age is: " + age + ".")

#Take that age=30, convert it into the literal text string '30', and hand it over so that both sides of the + sign are strings.Python is a strongly typed language and will not automatically convert data types for you when using the + operator."
#print("My name is: " + name + " and my age is: " + str(age) + ".")

#result= "Hello, my name is " + name + " and my age is " + str(age) + "."

#print(result)
#print(type(result))

# Before Python 2.6 , %s for string and %d for integer
#print("Hello, my name is %s and I am %d years old." % (name,age)) #It requires exact data type for the variable anda trailing tuple. If you use %d for a string, it will throw an error.


# From Python 2.6 .format() method is introduced andused to format the string. It allows you to insert variables into a string using placeholders defined by curly braces {}. The variables are passed as arguments to the format() method in the order they appear in the string.
#print("Hello, my name is {0} and I am {1} years old.".format(name, age))

# From python 3.6 , f-strings (formatted string literals) are introduced and used to format the string. It allows you to embed expressions inside string literals, using curly braces {}. The variables are directly referenced within the string, making it more concise and readable.
#print(f"Hello, my name is {name} and I am {age} years old.")
#result = f"Hello, my name is {name} and I am {age} years old."
#print(result)