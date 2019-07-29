# Trees Ex1
class Node:
	def __init__(self, data=-float("inf"), left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def pre_order_print_node(self):
		print(self.data)

		if self.left:
			self.left.pre_order_print_node()
		if self.right:
			self.right.pre_order_print_node()


class Tree:
	def __init__(self, root=None):
		self.root = root

	def print(self):
		self.root.pre_order_print_node()


# tree = Tree(Node(1, Node(7), Node(17, Node(6), Node(3))))
# tree.print()


# Trees Ex2 and Trees Ex3
from collections import deque


class Employee:
	def __init__(self, name="", title="", direct_reports=[]):
		self.name = name
		self.title = title
		self.direct_reports = direct_reports


class OrganizationStructure:
	def __init__(self, ceo=None):
		self.ceo = ceo
		self.queue = deque()

	def print_level_by_level(self):
		if self.ceo:
			self.queue.append(self.ceo)

			employees_on_level = 0
			while self.queue:
				if employees_on_level == 0:
					print("")
					employees_on_level = len(self.queue)

				employee = self.queue.popleft()
				print('Name: ' + employee.name + ', Title: ' + employee.title)
				self.queue.extend(employee.direct_reports)

				employees_on_level -= 1

	def print_num_levels(self):
		if self.ceo:
			deepest_level = 1
			employees = self.ceo.direct_reports

			for employee in employees:
				deepest_level = max(deepest_level, self.get_num_levels(employee) + 1)

			return deepest_level
		return 0

	def get_num_levels(self, employee):
		if not employee.direct_reports:
			return 1
		return 1 + max([self.get_num_levels(direct_report) for direct_report in employee.direct_reports])


# left branch
sales_intern = Employee('K', 'Sales Intern')
sales_rep = Employee('J', 'Sales Representative', [sales_intern])
director_i = Employee("I", "Director", [sales_rep])
cfo = Employee('B', "CFO", [director_i])

# right branch
engineer_f = Employee("F", "Engineer")
engineer_g = Employee("G", "Engineer")
engineer_h = Employee("H", "Engineer")
manager_d = Employee("D", "Manager", [engineer_f, engineer_g, engineer_h])
manager_e = Employee("E", "Manager")
cto = Employee("C", "CTO", [manager_d, manager_e])

# CEO and Org.
org = OrganizationStructure(Employee('A', 'CEO', [cfo, cto]))
# org.print_level_by_level()
# print(org.print_num_levels())

# Trees Ex3 examples.
# left branch
director_i = Employee("I", "Director")
cfo = Employee('B', "CFO", [director_i])

# CEO and Org.
org = OrganizationStructure(Employee('A', 'CEO', [cfo, cto]))
print(org.print_num_levels())