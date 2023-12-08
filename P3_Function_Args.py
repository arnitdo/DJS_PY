from common_utils import print_and_execute

def some_task(pos_arg_a, pos_arg_b):
	print(f"pos_arg_a: {pos_arg_a}, pos_arg_b: {pos_arg_b}")
	
def some_variable_task(initial_arg, *other_args):
	print(f"initial_arg: {initial_arg}, other_args: {other_args}")

def some_default_task(darg_a = 10, darg_b = 10):
	print(f"arg_a: {darg_a}, arg_b: {darg_b}")

def some_kw_task(**kwargs):
	print(f"Name: {kwargs.get('name', 'not provided')}")
	print(f"Age: {kwargs.get('age', 'not provided')}")

print_and_execute(
	some_task,
	10, 20
)

print_and_execute(
	some_variable_task,
	10, 20, 30, 50, 100
)

print_and_execute(
	some_default_task
)

print_and_execute(
	some_default_task,
	10, 20
)

print("some_kw_task()")
some_kw_task()

print("some_kw_task(name='Arnav')")
some_kw_task(
	name='Arnav'
)

print("some_kw_task(age=18)")
some_kw_task(
	age=18
)

print("some_kw_task(name='Arnav', age=18)")
some_kw_task(
	name='Arnav',
	age=20
)

def calculate(a, b):
	return (
		a + b,
		a - b,
		a * b,
		a / b
	)

sum, *others = calculate(20, 10) # int, int[]

print(sum, others)

*others, sum = calculate(20, 10) # int[], int
print(others, sum)