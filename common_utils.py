def print_and_execute(some_fn, *fn_args):
	global_vars = globals()
	global_entries = global_vars.items()
	global_key = some_fn.__name__
	for key,value in global_entries:
		if (id(value) == id(some_fn)):
			global_key = key
			break
	print(f"-- {global_key}{tuple(list(fn_args))} --")
	fn_result = some_fn(*fn_args)
	print(f"-- {global_key}{tuple(list(fn_args))} returned {fn_result} --")


def dump_info(exp_no = None):
	if not exp_no:
		print("C3 - 2 : 60004230285 ARNAV NITIN DEO")
	else:
		print(f"C3 - 2 : 60004230285 ARNAV NITIN DEO - EXPERIMENT {exp_no}")