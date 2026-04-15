import re
print("Our Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter your equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        previous = eval(equation)

        print("You typed", previous)

while run:
    performMath()