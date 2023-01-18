temperature = int(input("Enter the temperature in fahrenhite: "))

convertion = ((temperature-32)*5)//9
print(temperature,"°F", "=", convertion,"°C")

if temperature <= 15:
  print("Brrr...Its a cold day! You might need a jacket.")
elif 16 < temperature < 25: 
  print("Its not a very cold day, but its not a pleasant day either. Its an okay day! Still might need a hoodie.")
elif 26 <= temperature < 40:
  print("Its a warm day. Its nice to go out with yout friends and family.")
elif 41 < temperature < 65:
  print("This is the right temperature! Its a normal day.")
else:
  print("Whew!! Its a hot day. Carry a water bottle today.")


