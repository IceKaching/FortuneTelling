# FORTUNE telling game by Matt Hobbs

import sys

print('''Hello, welcome to the FORTUNE telling game! You are going to learn
about how to spend and invest your money in the best way to have a
comfortable and stress free life''')
print()
playerName = input('What is your name? : ')
print()
print('Hello ' + playerName +'!')
print()
print('How old are you ' + playerName +'?')

playerAge = 0
# input a number
# while 1 > playerAge or 128 < playerAge: 
while not playerAge in range (5,129):
  try:
     playerAge = int(input("Enter a whole number (5 - 128) : "))
  except ValueError:
      print("Please input whole number only...")  
      continue

print()
print((str(playerAge)) + ' is the perfect age to get started planning your future!')
print()
print('When you finish school ' + playerName +' how old will you be then?')

playerAgeAfterSchool = 0
# input a number
# while 1 > playerAgeAfterSchool or 30 < playerAgeafterSchool: 
while not playerAgeAfterSchool in range (16,31):
  try:
     playerAgeAfterSchool = int(input("Enter a whole number (16 - 30) : "))
  except ValueError:
      print("Please input whole number only...")  
      continue

print()
print('Okay ' + playerName +' I understand that you will be ' + str(playerAgeAfterSchool) + ' when you finish school')
print()
print('How old do you think you will live ' + playerName +'?')

playerDeathAge = 0
# input a number
# while 1 > playerDeathAge or 30 < playerDeathAge: 
while not playerDeathAge in range (40,129):
  try:
     playerDeathAge = int(input("Enter a whole number (40 - 128) : "))
  except ValueError:
      print("Please input whole number only...")  
      continue

print('And how old do you think you will be when you want to retire?')

playerRetirementAge = 0
# input a number
while not playerRetirementAge in range (30,129):
  try:
     playerRetirementAge = int(input("Enter a whole number (30 - 128) : "))
  except ValueError:
      print("Please input whole number only...")  
      continue

if playerRetirementAge == playerDeathAge:
    print('Oops! I guess this tool is not useful for you, goodbye!')
    sys.exit()

playerWorkingYears = playerRetirementAge - playerAgeAfterSchool
playerRetirementYears = playerDeathAge - playerRetirementAge

print()
print('That means that will be working for ' + str(playerWorkingYears)+' years')
print()
print('And it also means that you want to enjoy your retirement for '+ str(playerRetirementYears)+' years')
print()
print('How much money do you think you will make per hour when you start working?')

playerHourlyRate = 0
# input a number
while True:
  try:
     playerHourlyRate = int(input("Enter a whole number : "))
     break
  except ValueError:
      print("Please input whole number only...")  
      continue

print()
print('And how many hours per week will you work? (Typical full-time is 40)')

playerHoursPerWeek = 0
# input a number
while not playerHoursPerWeek in range (1,80):
  try:
     playerHoursPerWeek = int(input("Enter a whole number (1 - 80) : "))
  except ValueError:
      print("Please input whole number only...")  
      continue

print('How many weeks of holidays per year will you have?')

playerHolidays = 0
# input a number
while not playerHolidays in range (1,53):
  try:
     playerHolidays = int(input("Enter a whole number (1 - 52) : "))
  except ValueError:
      print("Please input whole number only...")  
      continue

playerSalary = playerHourlyRate * playerHoursPerWeek * (52 - playerHolidays)

print('That means that you will be making $' + "{:,}".format(playerSalary) +' per year.')
print()
print('How much money will you spend on housing rent per month?')

playerRentPerMonth = 0
# input a number
while True:
  try:
     playerRentPerMonth = int(input("Enter a whole number : "))
     break
  except ValueError:
      print("Please input whole number only...")  
      continue

print('How much will you spend per day on food?')

playerFoodCost = 0
# input a number
while True:
  try:
     playerFoodCost = int(input("Enter a whole number : "))
     break
  except ValueError:
      print("Please input whole number only...")  
      continue

playerTotalExpenses = playerRentPerMonth * 12 + playerFoodCost * 365 

print('Your total expenses are $'+ "{:,}".format(playerTotalExpenses)+ ' per year')
print()
print('This means that you will have $' + "{:,}".format(playerSalary - playerTotalExpenses) +' left over per year')
print()
print('''How much of this money would you like to invest per year for
your future retirement?''')

playerAnnualInvestment = 0
# input a number
while True:
  try:
     playerAnnualInvestment = int(input("Enter a whole number : "))
     break
  except ValueError:
      print("Please input whole number only...")  
      continue

playerRetirementSum = playerWorkingYears * playerAnnualInvestment

print('Awesome! That means that you will invest a total of $' +"{:,}".format(playerRetirementSum))
print('during your working years')
print()
print('You will therefore have $' +"{:,}".format(int(playerRetirementSum/playerRetirementYears)) +' per year for your retirement')
print()
print('Compared to your spending, this means you will have a $' +"{:,}".format((int(playerRetirementSum/playerRetirementYears) - playerTotalExpenses)) +' left over per year')
print()

if ((playerRetirementSum/playerRetirementYears) - playerTotalExpenses) > 0:
    print('Great, it looks like you will have enough money to last your retirement!')
else:
    print("Uh oh, looks like you won't have enough money to last through your retirement")

#print('Do you think this is enough money for you to survive?')
#playerSurvive = input()
print()
input('Press Enter to continue...')
print()
print('''But this is only if you left that investment money sitting in a bank
account earning very little interest.... instead if you properly invested it,
it can grow massively by itself. This is called "compounding"''')
print()
print('''On average, the US stock market has returned about 9% growth per year
for the past 100 years. Let\'s see what happens when we add some growth to your
investment money of $''' + "{:,}".format(playerAnnualInvestment) + ' per year.''')
print()
print('How much percentage growth do you expect per year?')

playerGrowthExpect = 0
# input a number
while not playerGrowthExpect in range (1,101):
  try:
     playerGrowthExpect = int(input("Enter a whole number (9 is typical) : "))
  except ValueError:
      print("Please input whole number only...")  
      continue

#playerGrowthExpect = input()
#playerGrowthExpect = int(playerGrowthExpect)

print('Okay you are expecting ' + str(playerGrowthExpect)+'% per year')
print()
playerGrowthExpect = playerGrowthExpect/100

#  PMT × {[(1 + r/n)^(nt) - 1] / (r/n)} × (1+r/n)
# Total = PMT × p {[(1 + r/n)^(nt) - 1] / (r/n)}

#    A = the future value of the investment/loan, including interest
#    P = the principal investment amount (the initial deposit or loan amount)
#    PMT = the monthly payment
#    r = the annual interest rate (decimal)
#    n = the number of times that interest is compounded per unit t
#    t = the time (months, years, etc) the money is invested or borrowed for

playerCompoundedTotal = playerAnnualInvestment*((((1+playerGrowthExpect/1)**(1*playerWorkingYears))-1)/(playerGrowthExpect/1))
playerCompoundedTotal = int(playerCompoundedTotal)

print('Wow! You will now have $' + "{:,}".format(playerCompoundedTotal) +' instead of $' + "{:,}".format(playerRetirementSum))
print()
print('This means that you will now have $' +"{:,}".format(int(playerCompoundedTotal/playerRetirementYears)) + ' per year')
print('and your expenses will be $' +"{:,}".format(playerTotalExpenses) +'.')
print()
print('Does this look better to you?')

playerSurvive2 = input()
