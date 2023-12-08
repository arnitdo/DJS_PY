import sqlite3
import sys
from common_utils import dump_info

db = sqlite3.connect("P5_SQLite.db")

cursor = db.cursor()

H_BORDER_CHAR = "-"
V_SEP_CHAR = "|"
_meta_column_names = ["sap_id", "f_name", "l_name", "contact_no"]

def print_border_row(header_dict: dict[str, int]):
	final_print_length = 0
	all_lengths = header_dict.values()
	for length in all_lengths:
		final_print_length += (1 + length + 1 + 1)

	final_print_length += 1
	print(H_BORDER_CHAR * final_print_length)

def print_headers(header_dict: dict[str, int]):
	for name, value in header_dict.items():
		print(f"{V_SEP_CHAR} {name}{' ' * (value - len(name))} ", end="")

	print(V_SEP_CHAR)

def print_row(header_dict: dict[str, int], row_data: dict[str, any]):
	header_names = header_dict.keys()
	header_values = header_dict.values()
	for index, name in enumerate(header_names):
		row_value = row_data[index]
		if row_value is None:
			row_value = "NULL"
		print(f"{V_SEP_CHAR} {row_value}{' ' * (header_dict[name] - len(row_value))} ", end="")

	print(V_SEP_CHAR)



def _meta_query_column_sizes(page_size, page_no):
	column_map = dict()

	for index, column in enumerate(_meta_column_names):
		column_res = cursor.execute(
			f"""
				SELECT MAX(LENGTH({column})) AS strlen_{column} FROM students LIMIT ? OFFSET ?;
			""",
			(page_size, (page_no - 1) * page_size)
		)
		column_dat = column_res.fetchone()
		if column_dat is None:
			column_map[column] = 32 # Default
		else:
			col_len = column_dat[0]
			if col_len < len(column):
				col_len = len(column)
			column_map[column] = col_len

	return column_map


def init_db():
	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS students (
			sap_id TEXT PRIMARY KEY,
			f_name TEXT NOT NULL,
			l_name TEXT,
			contact_no TEXT NOT NULL
		);
		"""
	)


def add_student():
	student_sap = input("SAP ID: ")
	db_existing = cursor.execute(
		"""SELECT 1 FROM students WHERE sap_id = ?""",
		(student_sap, )
	)
	existing_data = db_existing.fetchone()
	if existing_data is not None:
		print("SAP ID already exists!")
		return add_student()

	student_fname = input("First Name: ")
	student_lname = input("Last Name: ")
	student_contact = input("Student Contact: ")

	for string_inp in [student_sap, student_fname, student_lname, student_contact]:
		if len(string_inp) == 0:
			print("Invalid values entered!")
			return add_student()

	insert_res = cursor.execute(
		"""
		INSERT INTO students VALUES (
			?, ?, ?, ?
		) RETURNING 1;
		""",
		(student_sap, student_fname, student_lname, student_contact)
	)
	insert_success = insert_res.fetchone()
	if insert_success is not None:
		print("Student data inserted successfully!")
	else:
		print("An error occurred when inserting student data!")


def list_students():
	page_size_inp = input("Enter number of records to display: ")
	try:
		page_size = int(page_size_inp)
		if page_size <= 0:
			print("Invalid Value Entered!")
			return list_students()
		else:
			page_offset_inp = input("Enter page to search (1, 2, 3, etc.): ")
			try:
				page_offset = int(page_offset_inp)
				if page_offset < 1:
					print("Invalid Value Entered!")
					return list_students()
				else:
					column_data = _meta_query_column_sizes(page_size, page_offset)
					table_res = cursor.execute(
						"""
						SELECT * FROM students LIMIT ? OFFSET ?
						""",
						(page_size, (page_offset - 1) * page_size)
					)

					table_data = table_res.fetchall()

					print_border_row(column_data)
					print_headers(column_data)
					print_border_row(column_data)
					for row in table_data:
						print_row(column_data, row)
					print_border_row(column_data)

			except ValueError:
				print("An error occurred!")
	except ValueError:
		print("An error occurred!")


def update_student():
	student_sap = input("Enter SAP ID to update: ")
	db_existing = cursor.execute(
		"""SELECT * FROM students WHERE sap_id = ?""",
		(student_sap,)
	)
	existing_data = db_existing.fetchone()
	if existing_data is None:
		print(f"SAP ID {student_sap} does not exist!")
		return update_student()

	student_data_map = dict()

	for index, colname in enumerate(_meta_column_names):
		student_data_map[colname] = existing_data[index]

	print(f"SAP ID: {student_data_map['sap_id']}")
	updated_fname = input(f"First Name [{student_data_map['f_name']}]: ")
	updated_lname = input(f"Last Name [{student_data_map['l_name']}]: ")
	updated_contact = input(f"Contact [{student_data_map['contact_no']}]: ")

	updated_dict = {
		'f_name': updated_fname,
		'l_name': updated_lname,
		'contact_no': updated_contact
	}

	# Merge the dict
	for key, value in updated_dict.items():
		if value.strip() != "":
			student_data_map[key] = value

	update_res = cursor.execute(
		"""
			UPDATE students SET
				f_name = ?,
				l_name = ?,
				contact_no = ?
			WHERE sap_id = ? RETURNING 1
		""",
		(
			student_data_map['f_name'],
			student_data_map['l_name'],
			student_data_map['contact_no'],
			student_data_map['sap_id']
		)
	)

	update_success = update_res.fetchone()
	if update_success is None:
		print("Failed to update value!")
	else:
		print("Value updated successfully!")


def delete_student():
	student_sap = input("Enter SAP ID to delete: ")
	db_existing = cursor.execute(
		"""SELECT 1 FROM students WHERE sap_id = ?""",
		(student_sap,)
	)
	existing_data = db_existing.fetchone()
	if existing_data is None:
		print(f"SAP ID {student_sap} does not exist!")
		return delete_student()

	cursor.execute(
		"""DELETE FROM students WHERE sap_id = ?""",
		(student_sap,)
	)

	print("Data deleted successfully!")

def exit_app():
	db.commit()
	db.close()
	sys.exit(0)

if __name__ == "__main__":
	init_db()
	while True:
		dump_info()
		print(
			"""
			1. Add Student
			2. List Students
			3. Update Student
			4. Delete Student
			5. [Commit DB]

			0. Exit
			"""
		)
		choice_inp = input("Select: ")
		try:
			fn_arr = [
				exit_app,
				add_student,
				list_students,
				update_student,
				delete_student,
				db.commit
			]
			inp_val = int(choice_inp)
			if inp_val < 0 or inp_val >= len(fn_arr):
				raise ValueError()
			else:
				db_fn = fn_arr[inp_val]
				db_fn()

		except ValueError:
			print("Invalid input!")