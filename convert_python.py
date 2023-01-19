gross_salary = input('Enter gross salary: ')

''''The tax rate is optional'''
tax_rate = 0.30

print("type of gross salary: ", type(gross_salary))

gross_salaryx = float(gross_salary)

total_tax = gross_salaryx * 0.30

net_salary = gross_salaryx - total_tax

print("The net salary of", "€",gross_salary, "is", "€", "%.2f" % net_salary)