print ("hello world")

weather = input("What's the weather like today?")
weather = weather.lower()

if weather == "raining":
  print ("bring an umbrella!")
elif weather == "sunny":
  print ("bring a hat!")
elif weather == "windy":
  print ("put on a jacket!")
else:
  print ("BRING AN UMBRELLA, HAT AND JACKET!!!")
