import random

pincode = input("Input your pin code (blank results in ABCD): ").strip()
if not pincode.isnumeric():
    pincode = "ABCD"

width = 9
height = 4

numbers = []

print("-"*(width*3+1))
for y in range(0, height):
    for x in range(0, width):
        index = y*width+x
        index = str(index).zfill(2)
        print("|{}".format(index), end="")
        numbers.append(random.randint(0, 9))
    print("|")
    print("-"*(width*3+1))

positions = input("Input which indices to put (Example: 03 11 19 27): ").split()
for i in range(0, len(positions)):
    position = int(positions[i])
    numbers[position] = pincode[i]

print("-"*(width*2+1))
for i in range(0, len(numbers)):
    print("|{}".format(numbers[i]), end='')
    if (i+1) % width == 0 and i != 0:
        print("|")
        print("-"*(width*2+1))

print("Done")
