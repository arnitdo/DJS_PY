from common_utils import dump_info

class Employee:
	def __init__(self, emp_id, name):
		self.emp_id = emp_id
		self.name = name


class Developer(Employee):
	def __init__(self, emp_id, name, programming_language):
		super().__init__(emp_id, name)
		self.programming_language = programming_language


class Tester(Employee):
	def __init__(self, emp_id, name, testing_type):
		super().__init__(emp_id, name)
		self.testing_type = testing_type


class Manager(Employee):
	def __init__(self, emp_id, name):
		super().__init__(emp_id, name)
		self.managed_employees = []

	def add_developer(self, developer):
		if isinstance(developer, Developer):
			self.managed_employees.append(developer)
			print(f"Developer {developer.name} added to the team.")

	def add_tester(self, tester):
		if isinstance(tester, Tester):
			self.managed_employees.append(tester)
			print(f"Tester {tester.name} added to the team.")

	def remove_employee(self, employee):
		if employee in self.managed_employees:
			self.managed_employees.remove(employee)
			print(f"Employee {employee.name} removed from the team.")
		else:
			print(f"Employee {employee.name} not found in the team.")

	def display_managed_employees(self):
		print(f"Employees managed by {self.name}:")
		for employee in self.managed_employees:
			print(f"- {employee.name}")


dump_info()

dev1 = Developer(1, "John Doe", "Python")
tester1 = Tester(2, "Jane Doe", "Manual Testing")
manager1 = Manager(3, "Test User")

manager1.add_developer(dev1)
manager1.add_tester(tester1)

manager1.display_managed_employees()

manager1.remove_employee(dev1)

manager1.display_managed_employees()