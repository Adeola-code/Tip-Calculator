#Welcome message
print("Welcome to the tip calculator.")
#Ask for total bill
bill=float(input('What was the total bill? $'))
#Ask for tip percentage
tip=int(input('What percentage of tip would you like to give? 10, 12, or 15? '))
#Ask for amount of people splitting bill
people=int(input('How many people to split the bill? '))
#Convert tip to percentage
tip_percentage=tip/100
#Calculate the total bill (Tip inclusive)
total_bill=bill+(tip_percentage*bill)
#Calculate the amount of money each person should pay
each_person=round(total_bill/people, 2)
#Prints out the result
print(f"Each person should pay: ${each_person}")

