
# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# The input always will be valid.

companies = {}

while True:
    company = input()
    if company == "End":
        break
    company_name, employee = company.split(" -> ")

    if company_name not in companies:
        companies[company_name] = []

    companies[company_name].append(employee)

for companay, aidi in companies.items():
    aidito = list(dict.fromkeys(aidi))
    print(companay)
    for x in aidito:
        print(f"-- {x}")