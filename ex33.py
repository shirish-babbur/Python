numbers = []
i = 0
def loopthrough(limit, incrementby):
    #i = 0
    global i
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incrementby
        print("Numbers Now: ",numbers)
        print(f"At the bottom i is {i}")

print("The numbers: ")
loopthrough(10,2)
for num in numbers:
    print(num)
