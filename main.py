#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculator!")

bill = input("Please enter Bill amount:\n")
bill = int(bill)

tip = input("How much Tip would you like to give? 10/12/15 %\n")
tip = int(tip)

split = input("How many people to Split the bill?\n")
split = int(split)

tip_amount = int(bill*tip)/100
tip_amount = float(tip_amount)

split_amount = (bill + tip_amount)/ split
split_amount = float(split_amount)

print(f"Each person should pay: {split_amount}")
