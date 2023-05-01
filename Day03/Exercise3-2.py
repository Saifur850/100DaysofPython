height= float(input("Input your height: "))
weight= float(input("Input your weight: "))

BMI= round(weight/(height*height),2)



if BMI<18.5:
  print("underwight")
elif BMI<25:
  print("normal weight")
elif BMI<30:
  print("Overweight")
elif BMI<35:
  print("Obese")
else:
  print("Clinically obese")
