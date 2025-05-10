#import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
#connection = sqlite3.connect('my_database.db')

# Create a cursor object
#cursor = connection.cursor()

tax = 0.2
base_salary = 9690
credits = float(input("Enter credits: "))
days = float(input("Enter days: "))
tax_input = input("Tax (y/n): ")

print("")

if tax_input == "n":
    credits = credits / days * 12

    print("Estimated credits: " + str(round(credits, 2)))

    if credits <=36000:
        salary = credits / 340 * 100
    elif credits <=45000:
        salary = credits / 296 * 100
    elif credits <=60000:
        salary = credits / 257 * 100
    elif credits <=90000:
        salary = credits / 225 * 100
    elif credits >90000:
        salary = credits / 194 * 100

    salary = salary + base_salary

    salary = round(salary, 2)

    print("Estimated salary: ₱" + str(salary))
else:
    credits = credits / days * 12

    print("Estimated credits: " + str(round(credits, 2)))

    if credits <=36000:
        salary = credits / 340 * 100
    elif credits <=45000:
        salary = credits / 296 * 100
    elif credits <=60000:
        salary = credits / 257 * 100
    elif credits <=90000:
        salary = credits / 225 * 100
    elif credits >90000:
        salary = credits / 194 * 100

    salary = (salary + base_salary) 

    salary = salary - (salary * 0.2) - 1396.35

    salary = round(salary, 2)

    print("Estimated salary: ₱" + str(salary))


# Close the database connection
#connection.close()