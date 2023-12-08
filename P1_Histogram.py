from common_utils import dump_info, print_and_execute
from math import ceil

some_list = ["Apple", "Orange"]
some_set = {1, 2, 3}
some_tuple = (100, 200, 300)
some_dict = {
	"key": "value"
}

print(f"some_list: {some_list}")
print(f"some_set: {some_set}")
print(f"some_tuple: {some_tuple}")
print(f"some_dict: {some_dict}")

def histogram(nums: list[int]):
	num_histogram = [(num, nums.count(num)) for num in nums]
	return num_histogram


def perfect(num):
	divisors = []
	for pot_divisor in range(1, ceil((num / 2) + 1)):
		if num % pot_divisor == 0:
			divisors.append(pot_divisor)

	sum = 0
	for divisor in divisors:
		sum += divisor

	return sum == num

dump_info()
print_and_execute(histogram, [13,12,11,13,14,13,7,7,13,14,12])
print_and_execute(histogram, [7,12,11,13,7,11,13,14,12])
print_and_execute(histogram, [13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7])

print_and_execute(perfect, 6)