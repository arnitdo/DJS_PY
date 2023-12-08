from common_utils import print_and_execute, dump_info

greater_of = lambda a,b: a if a > b else b

is_even = lambda num: True if num % 2 == 0 else False

dump_info()

print(
	f"greater_of(10, 20): {greater_of(10, 20)}"
)

print(
	f"is_even(10): {is_even(10)}"
)

print_and_execute(
	is_even,
	10
)
