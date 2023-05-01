print("Welcome to tip calculator ")
total_bill = input("What was the total bill? ")
tip_perc = input("What percentage tip do you like to give? ")
total_people = input("How many people tp split the bill? ")

pay_amount = float(total_bill) * (1 + (int(tip_perc) / 100))
indivisual_amount = float(pay_amount) / int(total_people)

print(f"Each person should pay: {round(indivisual_amount,2)}")  
