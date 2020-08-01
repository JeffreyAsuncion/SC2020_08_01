import os
import sqlite3
from query_function import query_and_print


"""
THIS is the output from your queries as docstring comments
FOR GRADING PURPOSES

$ python northwind.py
********************************************************************************
PART TWO
********************************************************************************

What are the ten most expensive items (per unit price) in the database?

('Côte de Blaye', 263.5)
('Thüringer Rostbratwurst', 123.79)
('Mishi Kobe Niku', 97)
("Sir Rodney's Marmalade", 81)
('Carnarvon Tigers', 62.5)
('Raclette Courdavault', 55)
('Manjimup Dried Apples', 53)
('Tarte au sucre', 49.3)
('Ipoh Coffee', 46)
('Rössle Sauerkraut', 45.6)
What is the average age of an employee at time of hiring?
('Davolio', 'Nancy', 44)
('Fuller', 'Andrew', 40)
('Leverling', 'Janet', 29)
('Peacock', 'Margaret', 56)
('Buchanan', 'Steven', 38)
('Suyama', 'Michael', 30)
('King', 'Robert', 34)
('Callahan', 'Laura', 36)
('Dodsworth', 'Anne', 28)

3. (*Stretch*) How does the average age of employee at hire vary by city?

('Kirkland', 29.0)
('London', 32.5)
('Redmond', 56.0)
('Seattle', 40.0)
('Tacoma', 40.0)
********************************************************************************
PART THREE
********************************************************************************

1. What are the ten most expensive items (per unit price)
in the database *and* their suppliers?
('Aux joyeux ecclésiastiques', 'Côte de Blaye', 263.5)
('Plutzer Lebensmittelgroßmärkte AG', 'Thüringer Rostbratwurst', 123.79)
('Tokyo Traders', 'Mishi Kobe Niku', 97)
('Specialty Biscuits, Ltd.', "Sir Rodney's Marmalade", 81)
('Pavlova, Ltd.', 'Carnarvon Tigers', 62.5)
('Gai pâturage', 'Raclette Courdavault', 55)
("G'day, Mate", 'Manjimup Dried Apples', 53)
("Forêts d'érables", 'Tarte au sucre', 49.3)
('Leka Trading', 'Ipoh Coffee', 46)
('Plutzer Lebensmittelgroßmärkte AG', 'Rössle Sauerkraut', 45.6)

2. What is the largest category (by number of unique products in it)?
('Confections', 13)

3. (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
  (not name, region, or other fields) as the unique identifier for territories.

('King', 'Robert', 10)
"""



# Open Connection to new database file
DB_FILEPATH = 'northwind_small.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()


#Answer the following questions (each is from a single table):
print("*"*80)
print("PART TWO")
print("*"*80)
print_query = '''
What are the ten most expensive items (per unit price) in the database?
'''
query = '''
SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10; 
'''
query_and_print(query, print_query, cursor)


print_query = 'What is the average age of an employee at time of hiring?'
query = '''
SELECT LastName, FirstName, (HireDate - BirthDate) 
AS age_at_hire FROM Employee;'''
query_and_print(query, print_query, cursor)


print_query = '''
3. (*Stretch*) How does the average age of employee at hire vary by city?
'''
query = '''
SELECT City, AVG(age_at_hire) 
FROM (SELECT (HireDate - BirthDate) AS age_at_hire, City FROM Employee) 
GROUP BY City;
'''
query_and_print(query, print_query, cursor)


print("*"*80)
print("PART THREE")
print("*"*80)


print_query = '''
1. What are the ten most expensive items (per unit price) 
in the database *and* their suppliers?'''
query = '''
SELECT Supplier.CompanyName, Product.ProductName, Product.UnitPrice 
FROM Product 
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC LIMIT 10;'''
query_and_print(query, print_query, cursor)


print_query = '''
2. What is the largest category (by number of unique products in it)?'''
query = '''
SELECT 
	Category.CategoryName AS Category,
	COUNT(DISTINCT Product.ProductName) AS num_of_products
FROM Product
JOIN Category ON Product.CategoryId = Category.Id
GROUP BY Product.CategoryId 
Order BY num_of_products DESC
LIMIT 1;'''
query_and_print(query, print_query, cursor)



print_query = '''
3. (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
  (not name, region, or other fields) as the unique identifier for territories.
'''
query = '''
SELECT
	e.LastName,
	e.FirstName,
	COUNT(et.TerritoryId) AS num_of_territory
FROM EmployeeTerritory AS et
JOIN Employee AS e 
ON et.EmployeeId = e.Id
GROUP BY et.EmployeeId
ORDER BY num_of_territory DESC
LIMIT 1;'''
query_and_print(query, print_query, cursor)

