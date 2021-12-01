all_numbers = [int(number.strip("\n")) for number in open("input.txt", "r")]
numbers = list(filter(lambda x: any(x + y == 2020 for y in all_numbers), all_numbers))
print(numbers[0] * numbers[1])
