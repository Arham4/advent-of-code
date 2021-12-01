from functools import reduce

all_numbers = [int(number.strip("\n")) for number in open("input.txt", "r")]
numbers = list(filter(lambda x: any(x + y + z == 2020 for y in all_numbers for z in all_numbers), all_numbers))
print(reduce((lambda x, y: x * y), numbers))