"""
Initech is a company which has CEO Bill and a hierarchy of employees. Employees can have a list of other employees
reporting to them, which can themselves have reports, and so on. An employee with at least one report is
called a manager.

Please implement the closestCommonManager method to find the closest manager (i.e. farthest from the CEO) to two
employees. You may assume that all employees eventually report up to the CEO.

Tree structure:

Bill -> Dom, Samir, Michael

Dom -> Bob, Peter, Porter

Peter -> Milton, Nina

Sample Data:

CEO Bill has 3 employees reporting to him: {Dom, Samir, Michael}

Dom has three reports { Peter, Bob, Porter}

Samir has no reports {}

Michael has no reports {}

Peter has 2 reports {Milton, Nina}

Bob has no reports {}

Porter has no reports {}

Milton has no reports {}

Nina has no reports {}

Sample calls:

closestCommonManager(Milton, Nina) = Peter

closestCommonManager(Nina, Porter) = Dom

closestCommonManager(Nina, Samir) = Bill

closestCommonManager(Peter, Nina) = Peter

ReferenceL: https://github.com/spinundemi/closest_common_manager
"""


class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.reports = []

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_reports(self):
		return self.reports

	def add_report(self, employee):
		self.reports.append(employee)

def get_closest_manager(root, employee1, employee2):
	manager, flag1, flag2 = get_closest_manager_helper(root, employee1, employee2)
	print "Manager of %s and %s is %s" % (employee1.get_name(), employee2.get_name(), manager.get_name())
	return manager

def get_closest_manager_helper(root, employee1, employee2):
	flag1 = (root == employee1)
	flag2 = (root == employee2)
	manager = None
	for employee in root.get_reports():
		manager, eFlag1, eFlag2 = get_closest_manager_helper(employee, employee1, employee2)
		if manager is not None:
			return manager, flag1, flag2
		flag1 |= eFlag1
		flag2 |= eFlag2
		if flag1 and flag2:
			manager = root
			return manager, flag1, flag2
	return manager, flag1, flag2

def print_employees(root, header=""):
	print header, root.getName()
	for employee in root.get_reports():
		print_employees(employee, header + "  ")


if __name__ == '__main__':
	ceo = Employee(1, 'Bill')
	dom = Employee(2, 'Dom')
	samir = Employee(3, 'Samir')
	michael = Employee(4, 'Michael')
	bob = Employee(5, 'Bob')
	peter = Employee(6, 'Peter')
	porter = Employee(7, 'Porter')
	milton = Employee(8, 'Milton')
	nina = Employee(9, 'Nina')
	ceo.add_report(dom)
	ceo.add_report(samir)
	ceo.add_report(michael)
	dom.add_report(bob)
	dom.add_report(peter)
	dom.add_report(porter)
	peter.add_report(milton)
	peter.add_report(nina)
	get_closest_manager(ceo, peter, nina)
	get_closest_manager(ceo, milton, nina)
	get_closest_manager(ceo, nina, porter)