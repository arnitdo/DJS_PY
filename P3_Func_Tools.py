from functools import reduce
from common_utils import dump_info

cube_of = lambda x: x * x * x

some_arr = [1, 2, 3, 5, 20]

dump_info()

print(
    f"Cubes of {some_arr}: ",
	list(
		map(
			cube_of,
			some_arr
		)
	)
)

is_even = lambda x: True if x % 2 == 0 else False

some_arr_2 = list(range(0, 10))

print(
    f"Even numbers in {some_arr_2}: ",
    list(
        filter(
            is_even,
            some_arr_2
		)
	)
)

make_sum = lambda prev, curr: prev + curr

some_arr_3 = list(range(1, 6))

print(
    f"Sum of {some_arr_3}:",
    reduce(
        make_sum,
        some_arr_3
	)
)