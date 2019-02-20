age = 67
lower_limit = 18
upper_limit = 60

if type(age) == int:
  print("Age is not a number!")

else: 
  if age < 0:
    print("Incorrect age. Go be born!")
  elif age < lower_limit:
    print("No booze!")
  elif lower_limit <= age <= upper_limit:
    print("Go nuts!")
  else:
    print("You shouldn't")

print("Thank you!")
