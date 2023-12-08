from common_utils import dump_info
import re

def match_pattern(pat_str: str, re_flags: int = 0) -> None:
	reg_pat = re.compile(pat_str, re_flags)

	user_inp = input(f"Input [ pattern = {pat_str} ]: ")

	matches = list(re.finditer(reg_pat, user_inp))

	if (len(matches) > 0):
		for index, match in enumerate(matches):
			print(f"Match {index + 1}: {match.group(0)}")
	else:
		print(f"Input {user_inp} does not match pattern {pat_str}")

phone_re = r'^(\d{3})-?(\d{3})-?(\d{4})$'
name_re = r'^([A-Za-z-]+\s[A-Za-z-]+)$'
email_re = r'^([\w.-])+\@([\w.-]+\.[a-z]{2,})$'
address_re = r'^([\w\s.])+\,\s([A-Za-z-\'\s]+\s[A-Z]{2})\s(\d{5})$'

# # Phone Numbers
# match_pattern(
# 	phone_re
# )

# # Names
# match_pattern(
# 	name_re
# )

# # Emails
# match_pattern(
# 	email_re
# )

test_file = open("re_test_cases.txt", "r")
test_data = test_file.read()
test_file.close()

pattern_names = ["Phone", "Name", "Email", "Address"]
result_counts = []

dump_info()

for index, pattern in enumerate([phone_re, name_re, email_re, address_re]):
	pat_name = pattern_names[index]
	print(pat_name)

	pat_matches = list(
		re.finditer(
			re.compile(
				pattern,
				re.RegexFlag.MULTILINE
			),	
			test_data
		)
	)

	result_counts.append(len(pat_matches))

	for match in pat_matches:
		print(match.group(0))

phone_count, name_count, email_count, address_count, *ignore = result_counts
for index, count in enumerate([phone_count, name_count, email_count, address_count]):
	if ((phone_count + name_count + email_count + address_count) / 4) != count:
		print(f"Not all tests passed for {pattern_names[index]}! Passed: {count}")
	else:
		print(f"Test case passed for {pattern_names[index]}! Count: {count}")

dump_info()