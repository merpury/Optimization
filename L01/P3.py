"""
Template

Write a program to ask a user for an investment in rice production (baht/rai), an average rice production (kg/rai) and the wholesale price (baht/kwian), calculate the balance sheet, and report it.
"""

investment = int(input("Investment (baht/rai): "))

production = int(input("Rice production (kg/rai): "))

wholesale = int(input("Wholesale price (baht/kwian): "))

income = production * wholesale * 1/1000

balance = income-investment # Dummy

sheet = "Balance = income ({:,.2f}) - investment ({:,.2f}) = {:,.2f} baht/rai"

print(sheet.format(income, investment, balance))
