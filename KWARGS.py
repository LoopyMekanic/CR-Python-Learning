def print_something(name = "Someone", age = "Unknown"):
    print("My name is ", name, "and my age is ", age)

print_something(27)
print_something(None, 27)
print_something(age = 41)
print_something(age = 41, name = "Tony")