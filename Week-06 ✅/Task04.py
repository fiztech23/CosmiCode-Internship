# Week-06/Task04.py
# Task 4: Implement a program to use the collections module to
# perform advanced data manipulation tasks.
print ("=== TASK #4 OUTPUT ===")

from collections import Counter, defaultdict, deque, namedtuple
employees = [
    {"name": "Ali", "dept": "HR", "salary": 50000},
    {"name": "Sara", "dept": "IT", "salary": 80000},
    {"name": "John", "dept": "Finance", "salary": 75000},
    {"name": "Ayesha", "dept": "IT", "salary": 82000},
    {"name": "Bilal", "dept": "HR", "salary": 52000},
    {"name": "Emma", "dept": "Finance", "salary": 70000},
    {"name": "David", "dept": "IT", "salary": 90000},
]

dept_count = Counter(emp["dept"] for emp in employees)
print(f"\nDepartment-wise employee count: {dept_count}")

group = defaultdict(list)
for emp in employees:
    group[emp["dept"]].append(emp["name"])
print(f"\nEmployees grouped by department: {dict(group)}")

employee_queue = deque([emp["name"] for emp in employees])
employee_queue.appendleft("New_Intern")
employee_queue.pop()
print(f"\nEmployee Queue: {employee_queue}")

Employee = namedtuple("Employee", ["name", "dept", "salary"])
emp1 = Employee("Rida", "IT", 95000)
emp2 = Employee("Hifsa", "Finance", 72000)
print(f"\nNew employees: {emp1}{emp2}")
employees.append(emp1._asdict())
employees.append(emp2._asdict())
print(f"\nList of employees: {employees}")