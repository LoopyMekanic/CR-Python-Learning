numbers = [1,2,3,4,5]
numbers2 = ["Tony", "Someone", "Another Person"]

for item in numbers:
    print(item)
for item in numbers2:
    print("This persons name is", item)

run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1
