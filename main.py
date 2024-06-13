#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculator!")

bill = int(input("Please enter Bill amount:\n"))

tip = int(input("How much Tip would you like to give? 10/12/15 %\n"))

split = int(input("How many people to Split the bill?\n"))

tip_amount = float((bill*tip)/100)

split_amount = float((bill + tip_amount)/ split)

print(f"Each person should pay: {split_amount}")
