from common_utils import dump_info
import os

dump_info()

with open("file_io_input.txt", "r") as input_file:
	file_lines = input_file.readlines()

	num_lines = list(map(
		lambda str_line: int(str(str_line).strip().replace('\n', '')),
		file_lines
	))

	sorted_nums = sorted(num_lines)

	with open("file_io_output.txt", "w") as output_file:
		sorted_strings = list(map(
			lambda num: str(num) + "\n",
			sorted_nums
		))

		output_file.writelines(sorted_strings)