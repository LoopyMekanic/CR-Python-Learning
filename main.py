# Arguments in a function go in the parenthesis
def my_function(str1, str2):
    print(str1)
    print(str2)

my_function("This is argument 1", "This is argument 2, which is also a string")
my_function("Stringy", "Hello World")

def print_something(name, age):
    # This is concatenating
    print("My name is " + name + " and my age is " + str(age))
    # This is without concatenating
    print("My name is", name, "and my age is", age)

def print_something2(name = "Someone", age = "Unknown"):
    print("My name is", name, "and my age is", age)

print_something("Tony", 41)
print_something2("Tony")